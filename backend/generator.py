from dataclasses import dataclass
from typing import Optional
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random

from backend.db import get_connection

@dataclass
class Exercise:
  exercise_id: int
  name: str
  primary_muscle: str
  secondary_muscles: Optional[str]   # comma-separated, can be empty
  equipment: str
  difficulty: str
  goal: str
  sets_min: int
  sets_max: int
  reps_min: int
  reps_max: int

def _fetch_exercises() -> list[Exercise]:
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("SELECT * FROM Exercises")
  rows = cur.fetchall()
  cur.close()
  conn.close()
  return [Exercise(*row) for row in rows]

def _exercise_to_dict(exercise: Exercise) -> dict:
  d = {
    "primary_muscle": exercise.primary_muscle,
    "equipment": exercise.equipment,
    "goal": exercise.goal,
    "difficulty": exercise.difficulty,
  }

  if exercise.secondary_muscles:
    for muscle in exercise.secondary_muscles.split(","):
      d[f"sec_{muscle.strip()}"] = 1
  return d

_all_exercises = _fetch_exercises()
_vectorizer = DictVectorizer(sparse=False)
_vectorizer.fit([_exercise_to_dict(e) for e in _all_exercises])

def build_feature_vector(exercise : Exercise):
  return _vectorizer.transform([_exercise_to_dict(exercise)])[0]

def build_query_vector(goal : str, difficulty : str, target_muscles : list[str]):
  d = {
    "goal": goal,
    "difficulty": difficulty,
    "primary_muscle": target_muscles[0],  # most important muscle for this slot
  }
  # treat remaining target muscles as secondary
  for muscle in target_muscles[1:]:
    d[f"sec_{muscle}"] = 1

  return _vectorizer.transform([d])[0]

def score_exercises(exercises : list[Exercise], query_vector) -> list[tuple[float, Exercise]]:
  matrix = np.array([build_feature_vector(e) for e in exercises])
  scores = cosine_similarity(matrix, query_vector.reshape(1, -1)).flatten()
  return sorted(zip(scores, exercises), key=lambda x: x[0], reverse=True)

SPLIT_MUSCLES = {
  "ppl": {
    "push": ["chest", "shoulders", "triceps"],
    "pull": ["back", "lats", "biceps"],
    "legs": ["quads", "hamstrings", "calves", "glutes"],
  },
  "upper_lower": {
    "upper": ["chest", "back", "shoulders", "biceps", "triceps"],
    "lower": ["quads", "hamstrings", "calves", "glutes"],
  },
  "full_body": {
    "full": ["chest", "back", "quads", "hamstrings", "shoulders"],
  },
}

# how many exercises to pick per muscle group
MUSCLE_EXERCISE_COUNT = {
  "chest": 2,
  "back": 2,
  "lats": 2,
  "quads": 3,
  "hamstrings": 2,
  "shoulders": 2,
  "biceps": 2,
  "triceps": 2,
  "calves": 1,
  "glutes": 1,
  "rear delts": 1,
}

def select_workout(
  goal: str,
  difficulty: str,
  split_type: str,  # "ppl", "upper_lower", "full_body"
  day: str          # "push", "pull", "legs", "upper", "lower", "full"
) -> list[Exercise]:
  target_muscles = SPLIT_MUSCLES.get(split_type, {}).get(day, [])
  if not target_muscles:
    raise ValueError(f"Invalid split_type '{split_type}' or day '{day}'")

  query_vector = build_query_vector(goal, difficulty, target_muscles)
  scored = score_exercises(_all_exercises, query_vector)

  selected = []
  used_ids = set()

  for muscle in target_muscles:
    count = MUSCLE_EXERCISE_COUNT.get(muscle, 1)
    picked = 0
    for score, exercise in scored:
      if exercise.exercise_id in used_ids:
        continue
      if exercise.primary_muscle == muscle:
        selected.append(exercise)
        used_ids.add(exercise.exercise_id)
        picked += 1
        if picked >= count:
          break

  return selected

def randomize_sets_reps(exercise: Exercise) -> dict:
  return {
    "sets": random.randint(exercise.sets_min, exercise.sets_max),
    "reps": random.randint(exercise.reps_min, exercise.reps_max),
  }

def generate_workout(
  goal: str,
  difficulty: str,
  split_type: str,
  day: str
) -> dict:
  exercises = select_workout(goal, difficulty, split_type, day)

  workout = {
    "goal": goal,
    "difficulty": difficulty,
    "split_type": split_type,
    "day": day,
    "exercises": [
      {
        "exercise_id": e.exercise_id,
        "name": e.name,
        "primary_muscle": e.primary_muscle,
        "secondary_muscles": e.secondary_muscles,
        "equipment": e.equipment,
        **randomize_sets_reps(e),
      }
      for e in exercises
    ]
  }

  return workout
