from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()


@router.post("/motivations/{user_id}")
async def add_motivation(user_id: int, motivation: schemas.MotivationCreate, db: Session = Depends(database.get_db)):
    current_motivations = crud.get_motivations(db, user_id)

    for current_motivation in current_motivations:
        if current_motivation.key == motivation.key:
            raise HTTPException(status_code=400, detail="User already added this motivation")

    new_motivation = crud.create_motivation(db, motivation, user_id)
    return {
        "status": True,
        "detail": "Motivation added",
        "data": {
            "key": new_motivation.key,
            "category": new_motivation.category,
            "description": new_motivation.description
        }
    }


@router.get("/motivations/{user_id}")
async def get_motivations(user_id: int, db: Session = Depends(database.get_db)):
    motivations = crud.get_motivations(db, user_id)
    if not motivations:
        raise HTTPException(status_code=404, detail="Motivations not found")

    return {
        "status": True,
        "detail": "",
        "data": motivations
    }


@router.delete("/motivations/{motivation_id}")
async def delete_motivation(motivation_id: int, db: Session = Depends(database.get_db)):
    motivation = crud.delete_motivation(db, motivation_id)
    if not motivation:
        raise HTTPException(status_code=404, detail="Motivation not found")

    return {
        "status": True,
        "detail": "Motivation deleted successfully",
        "data": {
            "id": motivation.id
        }
    }
