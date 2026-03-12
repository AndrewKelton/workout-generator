from typing import Literal
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.generator import generate_workout

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "https://workout.andrewkelton.com",
    "https://andrewkelton.com",
  ],
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/workout")
def get_workout(
  goal: Literal["hypertrophy", "strength", "endurance"],
  difficulty: Literal["beginner", "intermediate", "advanced"],
  split_type: Literal["ppl", "upper_lower", "full_body"],
  day: Literal["push", "pull", "legs", "upper", "lower", "full"]
):
  try:
    return generate_workout(goal, difficulty, split_type, day)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))
