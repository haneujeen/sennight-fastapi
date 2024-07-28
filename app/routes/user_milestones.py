"""

    /user-milestones
    ├── POST /
    └── GET /{userID}

    ------------------------------
    |       user_milestone       |
    ------------------------------
    | id              | Integer  |
    | user_id         | Integer  |
    | milestone_id    | Integer  |
    | quit_attempt_id | Integer  |
    | date_achieved   | DateTime |
    ------------------------------

"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from .. import database
from ..schemas import milestone_schemas
from ..crud import user_milestone_crud
from typing import List

router = APIRouter()


# TODO: Update route names...
@router.post("/user-milestones")
async def create(
        user_milestone: milestone_schemas.UserMilestoneCreate,
        db: Session = Depends(database.get_db)
):
    new_user_milestone = user_milestone_crud.create(db, user_milestone)

    return {
        "status": True,
        "detail": "User's milestone created successfully",
        "data": new_user_milestone
    }


@router.get("/user-milestones/{user_id}")
async def get_milestones(user_id: int, db: Session = Depends(database.get_db)):
    user_milestones = user_milestone_crud.get_milestones(db, user_id)
    return {
        "status": True,
        "detail": "",
        "data": user_milestones
    }


@router.get("/user-milestones/max-id/{user_id}")
async def get_max_milestone_id(user_id: int, db: Session = Depends(database.get_db)):
    max_milestone_id = user_milestone_crud.get_max_milestone_id(db, user_id)
    return {
        "status": True,
        "detail": "",
        "data": max_milestone_id
    }
