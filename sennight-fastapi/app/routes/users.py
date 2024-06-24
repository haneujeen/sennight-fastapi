from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models, security

router = APIRouter()


@router.post("/users/register")
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


@router.post("/users")
async def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    authenticated_user = crud.authenticate_user(db, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = security.create_access_token(data={"sub": authenticated_user.email})

    return {
        "status": True,
        "detail": "Login successful",
        "data": {
            "email": authenticated_user.email,
            "name": authenticated_user.name,
            "start_date": authenticated_user.start_date,
            "daily_cigarettes": authenticated_user.daily_cigarettes,
            "cigarette_price": authenticated_user.cigarette_price,
            "access_token": access_token,
            "token_type": "bearer"
        }
    }


@router.patch("/users/{user_id}")
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = crud.update_user(db, user_id, user)
    return {
        "status": True,
        "detail": "User updated successfully",
        "data": {
            "email": updated_user.email,
            "name": updated_user.name,
            "start_date": updated_user.start_date,
            "daily_cigarettes": updated_user.daily_cigarettes,
            "cigarette_price": updated_user.cigarette_price,
            "updated_at": updated_user.updated_at
        }
    }


@router.get("/users/{user_id}", response_model=schemas.UserResponse)
async def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "status": True,
        "detail": "User deleted successfully",
        "data": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "deleted_at": user.deleted_at
        }
    }