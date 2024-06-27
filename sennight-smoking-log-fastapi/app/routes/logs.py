from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database
from ..crud import create_smoking_log, update_smoking_log, delete_smoking_log, read_smoking_logs

router = APIRouter()


@router.post("/logs")
def create_log(log: schemas.SmokingLogCreate, request: Request, db: Session = Depends(database.get_db)):
    user_id = request.state.user_id
    db_log = create_smoking_log(db, log, user_id)
    return {
        "status": True,
        "detail": "Log created successfully",
        "data": {
            "id": db_log.id,
            "user_id": db_log.user_id,
            "cigarettes_smoked": db_log.cigarettes_smoked,
            "date": db_log.date
        }
    }


@router.put("/logs/{log_id}")
def update_log(log_id: int, log: schemas.SmokingLogUpdate, request: Request, db: Session = Depends(database.get_db)):
    user_id = request.state.user_id
    db_log = update_smoking_log(db, log_id, log, user_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return {
        "status": True,
        "detail": "Log updated successfully",
        "data": {
            "id": db_log.id,
            "user_id": db_log.user_id,
            "cigarettes_smoked": db_log.cigarettes_smoked,
            "date": db_log.date
        }
    }


@router.delete("/logs/{log_id}")
def delete_log(log_id: int, request: Request, db: Session = Depends(database.get_db)):
    user_id = request.state.user_id
    db_log = delete_smoking_log(db, log_id, user_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return {
        "status": True,
        "detail": "Log deleted successfully",
        "data": None
    }


@router.get("/logs")
def read_logs(request: Request, db: Session = Depends(database.get_db)):
    user_id = request.state.user_id
    db_logs = read_smoking_logs(db, user_id)
    return {
        "status": True,
        "detail": "Logs retrieved successfully",
        "data": db_logs
    }
