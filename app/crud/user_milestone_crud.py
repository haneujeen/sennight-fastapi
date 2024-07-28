from sqlalchemy.orm import Session
from sqlalchemy import desc
from .. import models
from ..schemas import milestone_schemas


def create(db: Session, user_milestone: milestone_schemas.UserMilestoneCreate):
    db_user_milestone = models.UserMilestone(**user_milestone.model_dump())
    db.add(db_user_milestone)
    db.commit()
    db.refresh(db_user_milestone)
    return db_user_milestone


def get_milestones(db: Session, user_id: int):
    return db.query(models.UserMilestone).filter(models.UserMilestone.user_id == user_id).all()


def get_max_milestone_id(db: Session, user_id: int):
    return (db.query(models.UserMilestone)
            .filter(models.UserMilestone.user_id == user_id)
            .order_by(desc(models.UserMilestone.milestone_id))
            .first()
            .milestone_id)