from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import *
#from models import db, Exercise, Workout, WorkoutExercises

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
@app.route('/')
def index():
    return "Welcome to WorkOut!"





"""without applying Schema"""
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    workouts_list = []
    for w in workouts:
        w_dict = {
            "id":w.id,
            "date": w.date,
            "duration_minutes": w.duration_minutes,
            "notes": w.notes
        }
        workouts_list.append(w_dict)
    
    return jsonify(workouts_list), 200
    


@app.route('/workouts/<id>', methods=['GET'])
def get_workout_by_id():
    pass

@app.route('/workouts', methods=['POST'])
def add_workout():
    pass



@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout():
    pass


@app.route('/exercises', methods=['GET'])
def get_exercises():
    pass
    

@app.route('/exercises/<id>', methods=['GET'])
def get_exercise_by_id():
    pass


@app.route('/exercises', methods=['POST'])
def add_exercise():
    pass

@app.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id):
    pass

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST'])
def add_workout_to_exercise():
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)