from sqlalchemy.orm import Session
from .. import models
from ..schemas import milestone_schemas


def create(db: Session, user_milestone: milestone_schemas.UserMilestoneCreate):
    db_user_milestone = models.UserMilestone(**user_milestone.model_dump())
    db.add(db_user_milestone)
    db.commit()
    db.refresh(db_user_milestone)
    return db_user_milestone


def read(db: Session, user_id: int):
    return db.query(models.UserMilestone).filter(models.UserMilestone.user_id == user_id).all()
