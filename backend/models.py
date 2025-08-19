from typing import List
import datetime

class Users:
    id: int 
    username: str 
    email: str 
    password: str 
    age: int 
    weight: int 
    height: int 
    goals: List[str]

class Workouts:
    id: int 
    user_id: int 
    plan_name: str 
    date: datetime 
    exercises: int 
    duration: int

class Nutrition:
    id:int
    user_id:int
    date:datetime
    meals: List[str]
    calories: List[str]
    macros: List[str]

class Progress:
    id: int
    user_id: int
    workout_id: int
    sets: int
    reps: int
    weights: int
    notes: List[str]