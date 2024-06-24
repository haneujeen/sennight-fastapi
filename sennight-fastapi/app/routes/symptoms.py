from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()


@router.post("/symptoms/{user_id}")
async def add_symptom(user_id: int, symptom: schemas.SymptomCreate, db: Session = Depends(database.get_db)):
    current_symptoms = crud.get_symptoms(db, user_id)

    for current_symptom in current_symptoms:
        if current_symptom.key == symptom.key:
            raise HTTPException(status_code=400, detail="User already added this symptom")

    new_symptom = crud.create_symptom(db, symptom, user_id)
    if new_symptom is None:
        raise HTTPException(status_code=400, detail="Failed to add new symptom")

    return {
        "status": True,
        "detail": "Factor added",
        "data": {
            "key": new_symptom.key,
            "title": new_symptom.title,
            "description": new_symptom.description
        }
    }


@router.get("/symptoms/{user_id}")
async def get_factors(user_id: int, db: Session = Depends(database.get_db)):
    symptoms = crud.get_symptoms(db, user_id)
    if not symptoms:
        return {
            "status": True,
            "detail": "No symptom found",
            "data": []
        }
    return {
        "status": True,
        "detail": "",
        "data": symptoms
    }


@router.delete("/symptoms/{symptom_id}")
async def delete_factor(symptom_id: int, db: Session = Depends(database.get_db)):
    symptom = crud.delete_symptom(db, symptom_id)

    return {
        "status": True,
        "detail": "Symptom deleted successfully",
        "data": {
            "id": symptom.id,
            "user_id": symptom.user_id,
            "key": symptom.key,
            "title": symptom.title,
            "description": symptom.description
        }
    }
