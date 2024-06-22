from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models

router = APIRouter()

@router.post("/user/register")
async def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email in use")

    new_user = crud.create_user(db, user)
    return {
        "status": True,
        "detail": "User registered successfully",
        "data": {
            "email": new_user.email,
            "created_at": new_user.created_at
        }
    }

@router.post("/user")
async def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    authenticated_user = crud.authenticate_user(db, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {
        "status": True,
        "detail": "Login successful",
        "data": {
            "email": authenticated_user.email,
            "name": authenticated_user.name,
            "start_date": authenticated_user.start_date,
            "daily_cigarettes": authenticated_user.daily_cigarettes,
            "cigarette_price": authenticated_user.cigarette_price
        }
    }
