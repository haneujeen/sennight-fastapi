from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from datetime import datetime
from . import models, schemas, security


# User CRUD operations

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.hash_password(user.password)
    db_user = models.User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password,
        start_date=user.start_date,
        daily_cigarettes=user.daily_cigarettes,
        cigarette_price=user.cigarette_price,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise NoResultFound("User not found")

    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise NoResultFound("User not found")

    db_user.deleted_at = datetime.now()
    db.commit()
    return db_user

