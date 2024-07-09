from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, security
from ..schemas import user_schemas
from ..crud import user_crud

router = APIRouter()


@router.post("/users/register")
async def register(user: user_schemas.UserCreate, db: Session = Depends(database.get_db)):
    new_user = user_crud.create(db, user)
    photo_filename = new_user.photo_filename if new_user.photo_filename else ""

    return {
        "status": True,
        "detail": "User registered successfully",
        "data": {
            "email": new_user.email,
            "name": new_user.name,
            "photo_filename": photo_filename,
            "created_at": new_user.created_at
        }
    }


@router.post("/users")
async def login(user: user_schemas.UserLogin, db: Session = Depends(database.get_db)):
    authenticated_user = user_crud.authenticate(db, user.email, user.password)
    access_token = security.create_access_token(data={"sub": str(authenticated_user.id)})

    return {
        "status": True,
        "detail": "Login successful",
        "data": {
            "id": authenticated_user.id,
            "email": authenticated_user.email,
            "name": authenticated_user.name,
            "access_token": access_token
        }
    }


@router.get("/users/{user_id}")
async def read(user_id: int, db: Session = Depends(database.get_db)):
    user = user_crud.read(db, user_id)
    photo_filename = user.photo_filename if user.photo_filename else ""
    return {
        "status": True,
        "detail": "",
        "data": {
            "email": user.email,
            "name": user.name,
            "photo_filename": photo_filename
        }
    }


@router.put("/users/{user_id}")
async def update(user_id: int, user: user_schemas.UserUpdate, db: Session = Depends(database.get_db)):
    updated_user = user_crud.update(db, user_id, user)
    photo_filename = updated_user.photo_filename if updated_user.photo_filename else ""

    return {
        "status": True,
        "detail": "User updated successfully",
        "data": {
            "email": updated_user.email,
            "name": updated_user.name,
            "photo_filename": photo_filename,
            "updated_at": updated_user.updated_at
        }
    }


@router.delete("/users/{user_id}")
async def delete(user_id: int, db: Session = Depends(database.get_db)):
    user = user_crud.delete(db, user_id)
    return {
        "status": True,
        "detail": "User deleted successfully",
        "data": {
            "email": user.email,
            "name": user.name,
            "deleted_at": user.deleted_at
        }
    }
