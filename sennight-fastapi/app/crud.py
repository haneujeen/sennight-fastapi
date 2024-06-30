from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date
from . import models, schemas, security


# User CRUD operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.hash_password(user.password)
    db_user = models.User(email=user.email, name=user.name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.name:
        db_user.name = user.name
    if user.password:
        db_user.hashed_password = security.hash_password(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.deleted_at = datetime.now()
    db.commit()
    return db_user


# QuitLog CRUD operations
def create_quit_log(db: Session, quit_log: schemas.QuitLogCreate, user_id: int):
    db_quit_log = models.QuitLog(**quit_log.model_dump(), user_id=user_id)
    db.add(db_quit_log)
    db.commit()
    db.refresh(db_quit_log)
    return db_quit_log


def get_quit_logs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.QuitLog).filter(models.QuitLog.user_id == user_id).offset(skip).limit(limit).all()


def update_quit_log(db: Session, quit_log_id: int, quit_log: schemas.QuitLogUpdate):
    db_quit_log = db.query(models.QuitLog).filter(models.QuitLog.id == quit_log_id).first()
    if not db_quit_log:
        raise HTTPException(status_code=404, detail="QuitLog not found")

    for key, value in quit_log.model_dump(exclude_unset=True).items():
        setattr(db_quit_log, key, value)

    db.commit()
    db.refresh(db_quit_log)
    return db_quit_log


def delete_quit_log(db: Session, quit_log_id: int):
    db_quit_log = db.query(models.QuitLog).filter(models.QuitLog.id == quit_log_id).first()
    if not db_quit_log:
        raise HTTPException(status_code=404, detail="QuitLog not found")
    db.delete(db_quit_log)
    db.commit()
    return db_quit_log


# SmokingLog CRUD operations
def create_smoking_log(db: Session, smoking_log: schemas.SmokingLogCreate, user_id: int):
    db_smoking_log = models.SmokingLog(**smoking_log.model_dump(), user_id=user_id)
    db.add(db_smoking_log)
    db.commit()
    db.refresh(db_smoking_log)
    return db_smoking_log


def get_smoking_logs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.SmokingLog).filter(models.SmokingLog.user_id == user_id).offset(skip).limit(limit).all()


def update_smoking_log(db: Session, smoking_log_id: int, smoking_log: schemas.SmokingLogUpdate):
    db_smoking_log = db.query(models.SmokingLog).filter(models.SmokingLog.id == smoking_log_id).first()
    if not db_smoking_log:
        raise HTTPException(status_code=404, detail="SmokingLog not found")

    for key, value in smoking_log.model_dump(exclude_unset=True).items():
        setattr(db_smoking_log, key, value)

    db.commit()
    db.refresh(db_smoking_log)
    return db_smoking_log


def delete_smoking_log(db: Session, smoking_log_id: int):
    db_smoking_log = db.query(models.SmokingLog).filter(models.SmokingLog.id == smoking_log_id).first()
    if not db_smoking_log:
        raise HTTPException(status_code=404, detail="SmokingLog not found")
    db.delete(db_smoking_log)
    db.commit()
    return db_smoking_log


# Motivation CRUD operations
def create_motivation(db: Session, motivation: schemas.MotivationCreate):
    db_motivation = models.Motivation(**motivation.model_dump())
    db.add(db_motivation)
    db.commit()
    db.refresh(db_motivation)
    return db_motivation


def get_motivations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Motivation).offset(skip).limit(limit).all()


def delete_motivation(db: Session, motivation_id: int):
    db_motivation = db.query(models.Motivation).filter(models.Motivation.id == motivation_id).first()
    if not db_motivation:
        raise HTTPException(status_code=404, detail="Motivation not found")
    db.delete(db_motivation)
    db.commit()
    return db_motivation


# UserMotivation CRUD operations
def create_user_motivation(db: Session, user_motivation: schemas.UserMotivationCreate, user_id: int):
    db_user_motivation = models.UserMotivation(**user_motivation.model_dump(), user_id=user_id)
    db.add(db_user_motivation)
    db.commit()
    db.refresh(db_user_motivation)
    return db_user_motivation


def get_user_motivation(db: Session, user_id: int):
    return db.query(models.UserMotivation).filter(models.UserMotivation.user_id == user_id).first()


def update_user_motivation(db: Session, user_motivation_id: int, user_motivation: schemas.UserMotivationUpdate):
    db_user_motivation = db.query(models.UserMotivation).filter(models.UserMotivation.id == user_motivation_id).first()
    if not db_user_motivation:
        raise HTTPException(status_code=404, detail="UserMotivation not found")
    for key, value in user_motivation.model_dump(exclude_unset=True).items():
        setattr(db_user_motivation, key, value)
    db.commit()
    db.refresh(db_user_motivation)
    return db_user_motivation


def delete_user_motivation(db: Session, user_motivation_id: int):
    db_user_motivation = db.query(models.UserMotivation).filter(models.UserMotivation.id == user_motivation_id).first()
    if not db_user_motivation:
        raise HTTPException(status_code=404, detail="UserMotivation not found")
    db.delete(db_user_motivation)
    db.commit()
    return db_user_motivation


# Milestone CRUD operations
def create_milestone(db: Session, milestone: schemas.MilestoneCreate):
    db_milestone = models.Milestone(**milestone.model_dump())
    db.add(db_milestone)
    db.commit()
    db.refresh(db_milestone)
    return db_milestone


def get_milestones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Milestone).offset(skip).limit(limit).all()


def delete_milestone(db: Session, milestone_id: int):
    db_milestone = db.query(models.Milestone).filter(models.Milestone.id == milestone_id).first()
    if not db_milestone:
        raise HTTPException(status_code=404, detail="Milestone not found")
    db.delete(db_milestone)
    db.commit()
    return db_milestone


# UserMilestone CRUD operations
def create_user_milestone(db: Session, user_milestone: schemas.UserMilestoneCreate, user_id: int):
    db_user_milestone = models.UserMilestone(**user_milestone.model_dump(), user_id=user_id)
    db.add(db_user_milestone)
    db.commit()
    db.refresh(db_user_milestone)
    return db_user_milestone


def get_user_milestones(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.UserMilestone).filter(models.UserMilestone.user_id == user_id).offset(skip).limit(
        limit).all()


def delete_user_milestone(db: Session, user_milestone_id: int):
    db_user_milestone = db.query(models.UserMilestone).filter(models.UserMilestone.id == user_milestone_id).first()
    if not db_user_milestone:
        raise HTTPException(status_code=404, detail="UserMilestone not found")
    db.delete(db_user_milestone)
    db.commit()
    return db_user_milestone


# Factor CRUD operations
def create_factor(db: Session, factor: schemas.FactorCreate):
    db_factor = models.Factor(**factor.model_dump())
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)
    return db_factor


def get_factors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Factor).offset(skip).limit(limit).all()


def delete_factor(db: Session, factor_id: int):
    db_factor = db.query(models.Factor).filter(models.Factor.id == factor_id).first()
    if not db_factor:
        raise HTTPException(status_code=404, detail="Factor not found")
    db.delete(db_factor)
    db.commit()
    return db_factor


# UserFactor CRUD operations
def create_user_factor(db: Session, user_factor: schemas.UserFactorCreate, user_id: int):
    db_user_factor = models.UserFactor(**user_factor.model_dump(), user_id=user_id)
    db.add(db_user_factor)
    db.commit()
    db.refresh(db_user_factor)
    return db_user_factor


def get_user_factors(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.UserFactor).filter(models.UserFactor.user_id == user_id).offset(skip).limit(limit).all()


def update_user_factor(db: Session, user_factor_id: int, user_factor: schemas.UserFactorUpdate):
    db_user_factor = db.query(models.UserFactor).filter(models.UserFactor.id == user_factor_id).first()
    if not db_user_factor:
        raise HTTPException(status_code=404, detail="UserFactor not found")
    for key, value in user_factor.model_dump(exclude_unset=True).items():
        setattr(db_user_factor, key, value)
    db.commit()
    db.refresh(db_user_factor)
    return db_user_factor


def delete_user_factor(db: Session, user_factor_id: int):
    db_user_factor = db.query(models.UserFactor).filter(models.UserFactor.id == user_factor_id).first()
    if not db_user_factor:
        raise HTTPException(status_code=404, detail="UserFactor not found")
    db.delete(db_user_factor)
    db.commit()
    return db_user_factor


# Symptom CRUD operations
def create_symptom(db: Session, symptom: schemas.SymptomCreate):
    db_symptom = models.Symptom(**symptom.dict())
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)
    return db_symptom


def get_symptoms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Symptom).offset(skip).limit(limit).all()


def delete_symptom(db: Session, symptom_id: int):
    db_symptom = db.query(models.Symptom).filter(models.Symptom.id == symptom_id).first()
    if not db_symptom:
        raise HTTPException(status_code=404, detail="Symptom not found")
    db.delete(db_symptom)
    db.commit()
    return db_symptom


# UserSymptom CRUD operations
def create_user_symptom(db: Session, user_symptom: schemas.UserSymptomCreate, user_id: int):
    db_user_symptom = models.UserSymptom(**user_symptom.model_dump(), user_id=user_id)
    db.add(db_user_symptom)
    db.commit()
    db.refresh(db_user_symptom)
    return db_user_symptom


def get_user_symptoms(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.UserSymptom).filter(models.UserSymptom.user_id == user_id).offset(skip).limit(limit).all()


def delete_user_symptom(db: Session, user_symptom_id: int):
    db_user_symptom = db.query(models.UserSymptom).filter(models.UserSymptom.id == user_symptom_id).first()
    if not db_user_symptom:
        raise HTTPException(status_code=404, detail="UserSymptom not found")
    db.delete(db_user_symptom)
    db.commit()
    return db_user_symptom


# Activity CRUD operations
def create_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.Activity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activity).offset(skip).limit(limit).all()


def delete_activity(db: Session, activity_id: int):
    db_activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not db_activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    db.delete(db_activity)
    db.commit()
    return db_activity


# UserActivity CRUD operations
def create_user_activity(db: Session, user_activity: schemas.UserActivityCreate, user_id: int):
    db_user_activity = models.UserActivity(**user_activity.model_dump(), user_id=user_id)
    db.add(db_user_activity)
    db.commit()
    db.refresh(db_user_activity)
    return db_user_activity


def get_user_activities(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.UserActivity).filter(models.UserActivity.user_id == user_id).offset(skip).limit(limit).all()


def delete_user_activity(db: Session, user_activity_id: int):
    db_user_activity = db.query(models.UserActivity).filter(models.UserActivity.id == user_activity_id).first()
    if not db_user_activity:
        raise HTTPException(status_code=404, detail="UserActivity not found")
    db.delete(db_user_activity)
    db.commit()
    return db_user_activity
