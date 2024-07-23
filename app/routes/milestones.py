"""

    /milestones
    └── GET /

    -------------------------
    |      milestones      |
    -------------------------
    | id          | Integer |
    | days        | Integer |
    | message     | String  |
    -------------------------

"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database
from ..schemas import milestone_schemas
from ..crud import milestone_crud
from typing import List

router = APIRouter()


@router.get("/milestones")
async def read(db: Session = Depends(database.get_db)):
    milestones = milestone_crud.read(db)
    return {
        "status": True,
        "detail": "",
        "data": milestones
    }
