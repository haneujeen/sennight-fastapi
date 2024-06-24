from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from datetime import datetime, date
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


# Motivation CRUD operations

def create_motivation(db: Session, motivation: schemas.MotivationCreate, user_id: int):
    db_motivation = models.Motivation(
        user_id=user_id,
        key=motivation.key,
        category=motivation.category,
        description=motivation.description
    )
    db.add(db_motivation)
    db.commit()
    db.refresh(db_motivation)
    return db_motivation


def get_motivations(db: Session, user_id: int):
    return db.query(models.Motivation).filter(models.Motivation.user_id == user_id).all()


def delete_motivation(db: Session, motivation_id: int):
    db_motivation = db.query(models.Motivation).filter(models.Motivation.id == motivation_id).first()
    if not db_motivation:
        raise NoResultFound("Motivation not found")

    db.delete(db_motivation)
    db.commit()
    return db_motivation


# Milestone CRUD operations

def create_milestone(db: Session, milestone: schemas.MilestoneCreate, user_id: int):
    db_milestone = models.Milestone(
        user_id=user_id,
        key=milestone.key,
        title=milestone.title,
        description=milestone.description
    )
    db.add(db_milestone)
    db.commit()
    db.refresh(db_milestone)
    return db_milestone


def get_milestones(db: Session, user_id: int):
    return db.query(models.Milestone).filter(models.Milestone.user_id == user_id).all()


def get_milestone(db: Session, milestone_id: int):
    return db.query(models.Milestone).filter(models.Milestone.id == milestone_id).first()


# Factors CRUD operations

def create_factor(db: Session, factor: schemas.FactorCreate, user_id: int):
    db_factor = models.Factor(
        user_id=user_id,
        category=factor.category,
        title=factor.title,
        start_date=factor.start_date,
        end_date=factor.end_date
    )
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)
    return db_factor


def update_factor(db: Session, factor_id: int, factor: schemas.FactorUpdate):
    db_factor = db.query(models.Factor).filter(models.Factor.id == factor_id).first()

    update_data = factor.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_factor, key, value)

    db.commit()
    db.refresh(db_factor)
    return db_factor


def get_factors(db: Session, user_id: int):
    return db.query(models.Factor).filter(models.Factor.user_id == user_id).all()


def get_factor(db: Session, factor_id: int):
    return db.query(models.Factor).filter(models.Factor.id == factor_id).first()


def delete_factor(db: Session, factor_id: int):
    db_factor = db.query(models.Factor).filter(models.Factor.id == factor_id).first()
    if not db_factor:
        raise HTTPException(status_code=404, detail="Factor not found")

    db.delete(db_factor)
    db.commit()
    return db_factor


# Symptoms CRUD operations

def create_symptom(db: Session, symptom: schemas.SymptomCreate, user_id: int):
    db_symptom = models.Symptom(
        user_id=user_id,
        key=symptom.key,
        title=symptom.title,
        description=symptom.description
    )
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)
    return db_symptom


def get_symptoms(db: Session, user_id: int):
    return db.query(models.Symptom).filter(models.Symptom.user_id == user_id).all()


def get_symptom(db: Session, symptom_id: int):
    return db.query(models.Symptom).filter(models.Symptom.id == symptom_id).first()


def delete_symptom(db: Session, symptom_id: int):
    db_symptom = db.query(models.Symptom).filter(models.Symptom.id == symptom_id).first()
    if not db_symptom:
        raise NoResultFound("Symptom not found")

    db.delete(db_symptom)
    db.commit()
    return db_symptom


# Activity CRUD operations

def create_activity(db: Session, activity: schemas.ActivityCreate, user_id: int):
    db_activity = models.Activity(
        user_id=user_id,
        key=activity.key,
        category=activity.category,
        title=activity.title
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_activities(db: Session, user_id: int):
    return db.query(models.Activity).filter(models.Activity.user_id == user_id).all()


def get_activity(db: Session, activity_id: int):
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()


def delete_activity(db: Session, activity_id: int):
    db_activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not db_activity:
        raise NoResultFound("Activity not found")

    db.delete(db_activity)
    db.commit()
    return db_activity
