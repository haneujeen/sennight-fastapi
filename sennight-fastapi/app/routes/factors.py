from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()


@router.post("/factors/{user_id}")
async def add_factor(user_id: int, factor: schemas.FactorCreate, db: Session = Depends(database.get_db)):
    new_factor = crud.create_factor(db, factor, user_id)
    if new_factor is None:
        raise HTTPException(status_code=400, detail="Failed to add new factor")

    return {
        "status": True,
        "detail": "Factor added",
        "data": {
            "category": new_factor.category,
            "title": new_factor.title,
            "start_date": factor.start_date,
            "end_date": factor.end_date
        }
    }


@router.put("/factors/{factor_id}")
async def update_factor(factor_id: int, factor: schemas.FactorUpdate, db: Session = Depends(database.get_db)):
    db_factor = crud.get_factor(db, factor_id)
    if not db_factor:
        raise HTTPException(status_code=404, detail="Factor not found")

    updated_factor = crud.update_factor(db, factor_id, factor)
    if updated_factor is None:
        raise HTTPException(status_code=400, detail="Failed to update factor")

    return {
        "status": True,
        "detail": "Factor updated successfully",
        "data": {
            "category": updated_factor.category,
            "title": updated_factor.title,
            "start_date": updated_factor.start_date,
            "end_date": updated_factor.end_date
        }
    }


@router.get("/factors/{user_id}")
async def get_factors(user_id: int, db: Session = Depends(database.get_db)):
    factors = crud.get_factors(db, user_id)
    if not factors:
        return {
            "status": True,
            "detail": "No factor found",
            "data": []
        }
    return {
        "status": True,
        "detail": "",
        "data": factors
    }


@router.delete("/factors/{factor_id}")
async def delete_factor(factor_id: int, db: Session = Depends(database.get_db)):
    factor = crud.delete_factor(db, factor_id)

    return {
        "status": True,
        "detail": "User deleted successfully",
        "data": {
            "id": factor.id,
            "user_id": factor.user_id,
            "category": factor.category,
            "title": factor.title
        }
    }
