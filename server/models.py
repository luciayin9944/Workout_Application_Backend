from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from marshmallow import Schema, fields, validates_schema, ValidationError

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

    @validates("duration_minutes")
    def validate_duration_seconds(self, key, input_value):
        if input_value is not None and input_value < 0:
            raise ValueError("Duration (in minutes) cannot be negative")
        return input_value

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
    
    @validates("duration_seconds")
    def validate_duration_seconds(self, key, input_value):
        if input_value is not None and input_value < 0:
            raise ValueError("Duration (in seconds) cannot be negative")
        return input_value
    
    def __repr__(self):
        return f'<WorkoutExercises {self.id}, Sets {self.sets}, Reps {self.reps}, Duration {self.duration_seconds}>'


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    category = fields.String()
    equipment_needed = fields.Boolean()
    workout_exercises = fields.List(fields.Nested(lambda: WorkoutExercisesSchema(exclude=("exercise",))))

    @validates_schema
    def validate_exercise_name(self, data, **kwargs):
        name = data.get("name", "")
        if name.strip() == "":
            raise ValidationError("Exercise name cannot be blank or only whitespace.")
        

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date()
    duration_minutes = fields.Int()
    notes = fields.String()
    workout_exercises = fields.List(fields.Nested(lambda: WorkoutExercisesSchema(exclude=("workout",))))

    @validates_schema
    def validate_notes(self, data, **kwargs):
        notes = data.get("notes")
        if notes and len(notes) > 200:
            raise ValidationError("Notes is too long")


class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    workout = fields.Nested(lambda: WorkoutSchema(exclude=("workout_exercises",)))
    exercise = fields.Nested(lambda: ExerciseSchema(exclude=("workout_exercises",)))

    @validates_schema
    def validate_reps_sets(self, data, **kwargs):
        if data.get("reps") is None and data.get("sets") is None:
            raise ValidationError("At least one of 'reps' or 'sets' must be provided.")