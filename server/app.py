from flask import Flask, make_response, jsonify, request
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


@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    result = WorkoutSchema(many=True).dump(workouts)
    return jsonify(result), 200
    

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout_by_id(id):
    workout = Workout.query.filter_by(id=id).first()
    if not workout:
        return jsonify({"error": "Workout not found"}), 404
    result = WorkoutSchema().dump(workout)
    return jsonify(result), 200


@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    workout_schema = WorkoutSchema()

    try:
        validated_data = workout_schema.load(data)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    
    new_workout = Workout(**validated_data)
    db.session.add(new_workout)
    db.session.commit()

    return jsonify(workout_schema.dump(new_workout)), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    delete_workout = Workout.query.filter_by(id=id).first()
    if not delete_workout:
        return jsonify({"error": "Workout not found"}), 404
    
    for we in delete_workout.workout_exercises:
        db.session.delete(we)

    db.session.delete(delete_workout)
    db.session.commit()
    return jsonify({"message": f"Workout {id} deleted successfully."}), 200


@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    result = ExerciseSchema(many=True).dump(exercises)
    return jsonify(result), 200
    

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise_by_id(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404
    result = ExerciseSchema().dump(exercise)
    return jsonify(result), 200


# @app.route('/exercises', methods=['POST'])
# def add_exercise():
#     pass

# @app.route('/exercises/<int:id>', methods=['DELETE'])
# def delete_exercise(id):
#     pass

# @app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
# def add_workout_to_exercise():
#     pass



if __name__ == '__main__':
    app.run(port=5555, debug=True)




#"""without applying Schema"""
# @app.route('/workouts', methods=['GET'])
# # @app.route('/workouts')
# def get_workouts():
#     workouts = Workout.query.all()
#     workouts_list = []
#     for w in workouts:
#         w_dict = {
#             "id": w.id,
#             "date": w.date,
#             "duration_minutes": w.duration_minutes,
#             "notes": w.notes
#         }
#         workouts_list.append(w_dict)
    
#     return jsonify(workouts_list), 200