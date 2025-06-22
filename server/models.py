from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from marshmallow import Schema, fields

#db = SQLAlchemy()

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# Define Models here
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship('WorkoutExercises', back_populates='exercise')
    workouts = association_proxy('workout_exercises', 'workout')

    @validates('name')
    def validate_name(self, key, input_name):
        if not input_name :
            raise ValueError("Exercise name cannot be empty")
        return input_name
    
    def __repr__(self):
        return f"<Exercise {self.id}, {self.name}, {self.category}>"
    



class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)
    
    workout_exercises = db.relationship('WorkoutExercises', back_populates='workout')
    exercises = association_proxy('workout_exercises', 'exercise')

    def __repr__(self):
        return f"<Workout {self.id}, {self.date}, {self.duration_minutes}>"
    


class WorkoutExercises(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    @validates('reps', 'sets')
    def validate_positive_int(self, key, input_int):
        if input_int is not None and input_int <= 0:
            raise ValueError(f"{key} must be a positive integer")
        return input_int
    
    def __repr__(self):
        return f'<WorkoutExercises {self.id}, Sets {self.sets}, Reps {self.reps}, Duration {self.duration_seconds}>'
    
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    category = fields.String()
    equipment_needed = fields.Boolean()
    workout_exercises = fields.List(fields.Nested(lambda: WorkoutExercisesSchema(exclude=("exercise",))))


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date()
    duration_minutes = fields.Int()
    notes = fields.String()
    workout_exercises = fields.List(fields.Nested(lambda: WorkoutExercisesSchema(exclude=("workout",))))
    

class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    workout = fields.Nested(lambda: WorkoutSchema(exclude=("workout_exercises",)))
    exercise = fields.Nested(lambda: ExerciseSchema(exclude=("workout_exercises",)))