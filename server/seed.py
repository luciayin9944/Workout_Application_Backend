#!/usr/bin/env python3

from app import app
from models import *
from datetime import date

with app.app_context():

	# reset data and add new example data, committing to db 

   # Clearing tables
    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    # Seeding exercises
    e1 = Exercise(name="Push Up", category="Strength", equipment_needed=True)
    e2 = Exercise(name="Squat", category="Strength", equipment_needed=False)
    e3 = Exercise(name="Jump Rope", category="Cardio", equipment_needed=True)

    db.session.add_all([e1, e2, e3])
    db.session.commit()

    # Seeding workouts
    w1 = Workout(date=date(2025, 6, 20), duration_minutes=30, notes="Morning session")
    w2 = Workout(date=date(2025, 6, 21), duration_minutes=45, notes="Evening session")

    db.session.add_all([w1, w2])
    db.session.commit()

    # Seeding workout_exercises
    we1 = WorkoutExercises(workout=w1, exercise=e1, reps=15, sets=3, duration_seconds=180)
    we2 = WorkoutExercises(workout=w1, exercise=e2, reps=10, sets=4, duration_seconds=240)
    we3 = WorkoutExercises(workout=w2, exercise=e3, reps=20, sets=2, duration_seconds=300)
    we4 = WorkoutExercises(workout=w2, exercise=e1, reps=12, sets=3, duration_seconds=360)

    db.session.add_all([we1, we2, we3, we4])
    db.session.commit()

    print("Seeding complete.")