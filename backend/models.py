import datetime
from sqlmodel import Field, SQLModel
import datetime

class User(SQLModel, table=True):

    __tablename__ = "user"
    id: int | None = Field(default=None, primary_key=True) 
    username: str = Field(index=True)
    email: str 
    password: str 
    age: int | None = Field(default=None, index=True) 
    weight: int 
    height: int 
    goals: str

class Workouts(SQLModel, table=True):

    __tablename__ = "workouts"
    id: int | None = Field(default=None, primary_key=True) 
    user_id: int 
    plan_name: str 
    date: datetime 
    exercises: int 
    duration: int

class Nutrition(SQLModel, table=True):

    __tablename__ = "nutrition"
    id: int | None = Field(default=None, primary_key=True) 
    user_id:int
    date:datetime
    meals: str
    calories: str
    macros: str

class Progress:
    __tablename__ = "progress"
    id: int | None = Field(default=None, primary_key=True) 

    user_id: int
    workout_id: int
    sets: int
    reps: int
    weights: int
    notes: str

    id: int
    user_id: int
    workout_id: int
    sets: int
    reps: int
    weights: int
    notes: str