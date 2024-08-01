"""

    /smoking-habits
    ├── POST /
    ├── GET /{userID}
    └── PUT /{habitID}

    ------------------------------
    |       smoking_habit        |
    ------------------------------
    | id               | Integer |
    | user_id          | Integer |
    | daily_cigarettes | Integer |
    | cigarette_price  | Float   |
    | first_cigarette  | Time    |
    | smoking_years    | Integer |
    ------------------------------

"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database
from ..schemas import smoking_habit_schemas
from ..crud import smoking_habit_crud

router = APIRouter()


@router.post("/smoking-habits")
def create(
        smoking_habit: smoking_habit_schemas.SmokingHabitCreate,
        db: Session = Depends(database.get_db)
):
    new_habit = smoking_habit_crud.create(db, smoking_habit)

    return {
        "status": True,
        "detail": "Smoking habit created successfully",
        "data": new_habit
    }


@router.get("/smoking-habits/{user_id}")
async def read(user_id: int, db: Session = Depends(database.get_db)):
    smoking_habit = smoking_habit_crud.read(db, user_id)
    return {
        "status": True,
        "detail": "",
        "data": smoking_habit
    }


@router.put("/smoking-habits/{habit_id}")
async def update(
        habit_id: int,
        smoking_habit: smoking_habit_schemas.SmokingHabitUpdate,
        db: Session = Depends(database.get_db)
):
    updated_habit = smoking_habit_crud.update(db, habit_id, smoking_habit)

    return {
        "status": True,
        "detail": "Smoking habit updated successfully",
        "data": updated_habit
    }
