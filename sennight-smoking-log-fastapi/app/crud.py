from sqlalchemy.orm import Session
from . import models, schemas


def create_smoking_log(db: Session, log: schemas.SmokingLogCreate, user_id: int):
    db_log = models.SmokingLog(
        user_id=user_id,
        cigarettes_smoked=log.cigarettes_smoked,
        date=log.date
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def update_smoking_log(db: Session, log_id: int, log: schemas.SmokingLogUpdate, user_id: int):
    db_log = db.query(models.SmokingLog).filter(models.SmokingLog.id == log_id,
                                                models.SmokingLog.user_id == user_id).first()
    if db_log is None:
        return None

    db_log.cigarettes_smoked = log.cigarettes_smoked
    db_log.date = log.date

    db.commit()
    db.refresh(db_log)
    return db_log


def delete_smoking_log(db: Session, log_id: int, user_id: int):
    db_log = db.query(models.SmokingLog).filter(models.SmokingLog.id == log_id,
                                                models.SmokingLog.user_id == user_id).first()
    if db_log is None:
        return None

    db.delete(db_log)
    db.commit()
    return db_log


def read_smoking_logs(db: Session, user_id: int):
    return db.query(models.SmokingLog).filter(models.SmokingLog.user_id == user_id).all()