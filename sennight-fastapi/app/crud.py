from sqlalchemy.orm import Session
from . import models, schemas, security


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
