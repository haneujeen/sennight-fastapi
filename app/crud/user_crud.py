from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models, security
from ..schemas import user_schemas


# TODO: Update functions with .model_dump()
def create(db: Session, user: user_schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email in use")
    db_user_with_apple_id = db.query(models.User).filter(models.User.apple_id == user.apple_id).first()
    if db_user_with_apple_id:
        raise HTTPException(status_code=400, detail="Duplicated Apple user identifier")

    hashed_password = security.hash_password(user.password)
    db_user = models.User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password,
        photo_filename=user.photo_filename,
        apple_id=user.apple_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email")
    if not security.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid password")
    return user


def read(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def get_user_with_apple_id(db: Session, apple_id: str):
    db_user = db.query(models.User).filter(models.User.apple_id == apple_id).first()
    return db_user

### Apple sign in stuff


def update(db: Session, user_id: int, user: user_schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.name:
        db_user.name = user.name
    if user.password:
        db_user.hashed_password = security.hash_password(user.password)
    if user.photo_filename:
        db_user.photo_filename = user.photo_filename
    db.commit()
    db.refresh(db_user)
    return db_user


def delete(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.deleted_at = datetime.now()
    db.commit()
    return db_user
