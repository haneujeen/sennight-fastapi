from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()


@router.post("/logs")
def create_smoking_log(log: schemas.SmokingLogCreate, request: Request, db: Session = Depends(database.get_db)):
    user_id = request.state.user_id
    db_log = models.SmokingLog(
        user_id=user_id,
        cigarettes_smoked=log.cigarettes_smoked,
        date=log.date
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

