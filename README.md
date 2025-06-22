# Workout_Application_Backend


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
    
    # Run the Flask server
    flask run


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
