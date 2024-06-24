from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()


@router.post("/activities/{user_id}")
async def add_activity(user_id: int, activity: schemas.ActivityCreate, db: Session = Depends(database.get_db)):
    current_activities = crud.get_activities(db, user_id)

    for current_activity in current_activities:
        if current_activity.key == activity.key:
            raise HTTPException(status_code=400, detail="User already added this activity")

    new_activity = crud.create_activity(db, activity, user_id)
    if new_activity is None:
        raise HTTPException(status_code=400, detail="Failed to add new activity")

    return {
        "status": True,
        "detail": "Activity added",
        "data": {
            "key": new_activity.key,
            "category": new_activity.category,
            "title": new_activity.title
        }
    }


@router.get("/activities/{user_id}")
async def get_activities(user_id: int, db: Session = Depends(database.get_db)):
    activities = crud.get_activities(db, user_id)
    if not activities:
        return {
            "status": True,
            "detail": "No activity found",
            "data": []
        }
    return {
        "status": True,
        "detail": "",
        "data": activities
    }


@router.delete("/activities/{activity_id}")
async def delete_factor(activity_id: int, db: Session = Depends(database.get_db)):
    activity = crud.delete_activity(db, activity_id)

    return {
        "status": True,
        "detail": "Symptom deleted successfully",
        "data": {
            "id": activity.id,
            "user_id": activity.user_id,
            "key": activity.key,
            "category": activity.category,
            "title": activity.title
        }
    }
