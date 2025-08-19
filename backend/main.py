from typing import Annotated
import datetime
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import User, Workouts, Nutrition, Progress
from databse import SessionDep, create_db_and_tables

app = FastAPI()

@app.include_router("/auth", tags=["auth"])
@app.include_router("/auth", tags=["auth"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#_________________________________________________________________________

@app.get("/exercise/{user_id}")
def read_exercises(user_id: int, session: SessionDep) -> User:
    user = session.get(Workouts, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="exercise not found")
    return user

@app.post("/users/")
def create_user(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.put("/exercise/{exercise_id}", responses={403: {"description": "Operation forbidden"}})
async def update_exercise(exercise_id: str):
    if not exercise_id:
        raise HTTPException(
            status_code=403, detail="You can only update the exercise"
        )
    return {"exercise_id": exercise_id, "name": "Updated successfully"}

def read_progress(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Progress]:
    exercises = session.exec(select(Progress).offset(offset).limit(limit)).all()
    return exercises


@app.delete("/exercise/{exercise_id}")
def delete_exercise(exercise_id: int, session: SessionDep):
    exerccise = session.get(Progress, exercise_id)
    if not exerccise:
        raise HTTPException(status_code=404, detail="exercise not found")
    session.delete(exerccise)
    session.commit()
    return {"ok": True}

#_________________________________________________________________________

@app.get("/nutrition/{user_id}")
def read_nutrition(user_id: int, session: SessionDep) -> User:
    user = session.get(Nutrition, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="exercise not found")
    return user


@app.put("/nutrition/{nutrition_id}", responses={403: {"description": "Operation forbidden"}})
async def update_nutrition(nutrition: str):
    if not nutrition:
        raise HTTPException(
            status_code=403, detail="You can only update the nutrition"
        )
    return {"nutrition": nutrition, "name": "Updated successfully"}

@app.delete("/nutrition/{nutrition_id}")
def delete_nutrition(nutrition_id: int, session: SessionDep):
    exerccise = session.get(Nutrition, nutrition_id)
    if not exerccise:
        raise HTTPException(status_code=404, detail="nutrition not found")
    session.delete(exerccise)
    session.commit()
    return {"ok": True}

#_________________________________________________________________________
