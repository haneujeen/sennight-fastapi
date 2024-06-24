from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()


@router.post("/milestones/{user_id}")
async def add_milestone(user_id: int, milestone: schemas.MilestoneCreate, db: Session = Depends(database.get_db)):
    new_milestone = crud.create_milestone(db, milestone, user_id)
    if new_milestone is None:
        raise HTTPException(status_code=400, detail="Failed to add new milestone")

    return {
        "status": True,
        "detail": "Milestone added",
        "data": {
            "key": new_milestone.key,
            "title": new_milestone.title,
            "description": new_milestone.description
        }
    }


@router.get("/milestones/{user_id}")
async def get_milestones(user_id: int, db: Session = Depends(database.get_db)):
    milestones = crud.get_milestones(db, user_id)
    if not milestones:
        return {
            "status": True,
            "detail": "No milestone found",
            "data": []
        }
    return {
        "status": True,
        "detail": "",
        "data": milestones
    }
