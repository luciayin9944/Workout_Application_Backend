# Flask_SQLAlchemy_Workout_Application_Backend

This project is a robust backend API for a Workout Tracking Application, built to help personal trainers create, manage, and track workout routines and their associated exercises. Developed with Flask, SQLAlchemy, and Marshmallow, the application demonstrates key backend development practices such as defining model relationships, seeding data, validating requests, and maintaining clean, modular code architecture.


## Installation
    # Clone the repository
    https://github.com/luciayin9944/Workout_Application_Backend.git
    cd Workout_Application_Backend/server

    # Set up virtual environment
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Set Up Environment Variables
    export FLASK_APP=app.py
    export FLASK_RUN_PORT=5555

    # Initialize the Database
    flask db init
    flask db migrate
    flask db upgrade

    # Seed the Database
    python seed.py
    
    # Run the Flask shell(Optional)
    flask shell


## 📌 API Endpoints

### 🏋️ Workouts

| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| GET    | `/workouts`          | Retrieve a list of all workouts    |
| POST   | `/workouts`          | Create a new workout               |
| GET    | `/workouts/<id>`     | Get details of a specific workout  |
| DELETE | `/workouts/<id>`     | Delete a workout                   |

### 🏃 Exercises

| Method | Endpoint              | Description                         |
|--------|-----------------------|-------------------------------------|
| GET    | `/exercises`          | Retrieve a list of all exercises    |
| POST   | `/exercises`          | Create a new exercise               |
| GET    | `/exercises/<id>`     | Get details of a specific exercise  |
| DELETE | `/exercises/<id>`     | Delete an exercise                  |


### Test the API

    # Start the Flask development server:
    flask run


Test your endpoints using Postman or curl:

- `GET http://localhost:5555/workouts`

- `GET http://localhost:5555/workouts/2`

- `POST http://localhost:5555/workouts`
  - Body: 
  {
    "date": "2025-06-25",
    "duration_minutes": 60,
    "notes": "Full body workout"
  }

- `DELETE http://localhost:5555/workouts/3`

- `GET http://localhost:5555/exercises`

- `GET http://localhost:5555/exercises/1`

- `POST http://localhost:5555/exercises`
  - Body: 
    {
      "name": "Burpee",
      "category": "Cardio",
      "equipment_needed": false
    }

- `DELETE http://localhost:5555/exercises/4`

- `POST http://127.0.0.1:5555/workouts/2/exercises/2/workout_exercises`
  - Body: 
  {
    "reps": 10,
    "sets": 4,
    "duration_seconds": 300
  }