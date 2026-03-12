CREATE TABLE Exercises (
    exercise_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    primary_muscle VARCHAR(50) NOT NULL,
    secondary_muscles VARCHAR(100),
    equipment VARCHAR(50),
    difficulty VARCHAR(20) CHECK (difficulty IN ('beginner','intermediate','advanced')),
    goal VARCHAR(20) CHECK (goal IN ('hypertrophy','strength','endurance')),
    sets_min INT NOT NULL,
    sets_max INT NOT NULL,
    reps_min INT NOT NULL,
    reps_max INT NOT NULL
);

-- INSERT EXERCISES

-- Back + Biceps
INSERT INTO Exercises (name, primary_muscle, secondary_muscles, equipment, difficulty, goal, sets_min, sets_max, reps_min, reps_max) VALUES
('Panatta High Row', 'back', 'biceps', 'machine', 'intermediate', 'hypertrophy', 3, 4, 6, 8),
('Panatta Lat Pulldown (Converging)', 'lats', 'biceps', 'machine', 'intermediate', 'hypertrophy', 3, 3, 8, 12),
('Panatta Super Row', 'back', 'biceps', 'machine', 'intermediate', 'hypertrophy', 3, 3, 8, 10),
('Plate Loaded Row', 'back', 'biceps', 'machine', 'intermediate', 'hypertrophy', 3, 3, 8, 10),
('Panatta Lat Pullover Machine', 'lats', 'traps', 'machine', 'intermediate', 'hypertrophy', 3, 3, 10, 12),
('Panatta Preacher Curl Machine', 'biceps', '', 'machine', 'intermediate', 'hypertrophy', 3, 4, 8, 12),
('Incline DB Curl', 'biceps', '', 'dumbbell', 'intermediate', 'hypertrophy', 3, 3, 10, 12),
('Hammer Curl Machine', 'biceps', 'forearms', 'machine', 'intermediate', 'hypertrophy', 2, 3, 10, 12),
('Cable Bayesian Curl', 'biceps', '', 'cable', 'intermediate', 'hypertrophy', 3, 3, 12, 15);

-- Legs
INSERT INTO Exercises (name, primary_muscle, secondary_muscles, equipment, difficulty, goal, sets_min, sets_max, reps_min, reps_max) VALUES
('Panatta Hack Squat', 'quads', 'glutes', 'machine', 'intermediate', 'hypertrophy', 4, 5, 8, 12),
('Panatta Leg Press', 'quads', 'glutes', 'machine', 'intermediate', 'hypertrophy', 3, 3, 10, 12),
('Panatta Leg Extension', 'quads', '', 'machine', 'intermediate', 'hypertrophy', 3, 4, 12, 15),
('Sissy Squat Machine', 'quads', '', 'machine', 'intermediate', 'hypertrophy', 2, 3, 10, 15),
('Pendulum Squat', 'quads', 'glutes', 'machine', 'intermediate', 'hypertrophy', 2, 3, 8, 12),
('Lying Leg Curl', 'hamstrings', '', 'machine', 'intermediate', 'hypertrophy', 3, 3, 10, 12),
('RDL (Barbell or Panatta Glute Machine)', 'hamstrings', 'glutes', 'barbell', 'intermediate', 'hypertrophy', 4, 4, 6, 8),
('Standing Calf Raise', 'calves', '', 'machine', 'intermediate', 'hypertrophy', 3, 5, 12, 20),
('Donkey Calf Raise', 'calves', '', 'machine', 'intermediate', 'hypertrophy', 3, 5, 12, 20);

-- Chest + Shoulders + Triceps
INSERT INTO Exercises (name, primary_muscle, secondary_muscles, equipment, difficulty, goal, sets_min, sets_max, reps_min, reps_max) VALUES
('Panatta Super Incline / Super Chest Press', 'chest', 'delts,triceps', 'machine', 'intermediate', 'hypertrophy', 4, 4, 6, 8),
('Panatta Super Upper Chest Fly', 'chest', '', 'machine', 'intermediate', 'hypertrophy', 3, 3, 8, 12),
('Panatta Lateral Raise Machine', 'shoulders', '', 'machine', 'intermediate', 'hypertrophy', 3, 4, 12, 15),
('Panatta Super Pec Back (Rear Delts)', 'rear delts', 'traps', 'machine', 'intermediate', 'hypertrophy', 3, 4, 12, 15),
('Panatta Overhead Triceps Extension Machine', 'triceps', '', 'machine', 'intermediate', 'hypertrophy', 3, 3, 10, 12),
('Panatta Triceps Pushdown Machine', 'triceps', '', 'machine', 'intermediate', 'hypertrophy', 3, 3, 12, 15),
('Panatta Dip Machine', 'chest', 'triceps', 'machine', 'intermediate', 'hypertrophy', 1, 2, 8, 12),
('Barbell Incline Bench', 'chest', 'delts,triceps', 'barbell', 'intermediate', 'hypertrophy', 4, 4, 6, 8),
('Panatta Flat Chest Press', 'chest', 'triceps', 'machine', 'intermediate', 'hypertrophy', 3, 3, 8, 10),
('Panatta Incline Fly Machine', 'chest', '', 'machine', 'intermediate', 'hypertrophy', 3, 3, 10, 12),
('Panatta Shoulder Press (Converging)', 'shoulders', 'triceps', 'machine', 'intermediate', 'hypertrophy', 3, 3, 8, 10),
('Panatta Rear Delt Machine', 'rear delts', '', 'machine', 'intermediate', 'hypertrophy', 3, 4, 12, 15);