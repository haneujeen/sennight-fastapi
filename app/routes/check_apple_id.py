from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .. import database
from ..crud import user_crud

router = APIRouter()


class AppleIDRequest(BaseModel):
    apple_id: str


@router.post("/check-apple-id")
async def check_apple_id(request: AppleIDRequest, db: Session = Depends(database.get_db)):
    is_user_with_apple_id = user_crud.get_user_with_apple_id(db, request.apple_id)

    return {
        "is_user_with_apple_id": is_user_with_apple_id
    }
