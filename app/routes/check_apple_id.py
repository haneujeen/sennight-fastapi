from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .. import database, security
from ..crud import user_crud

router = APIRouter()


class AppleIDRequest(BaseModel):
    apple_id: str


@router.post("/apple-sign-in")
async def apple_sign_in(request: AppleIDRequest, db: Session = Depends(database.get_db)):
    user_with_apple_id = user_crud.get_user_with_apple_id(db, request.apple_id)
    access_token = security.create_access_token(data={"sub": str(user_with_apple_id.id)}) if user_with_apple_id else None

    return {
        "is_user_with_apple_id": user_with_apple_id is not None,
        "detail": "Sign in with Apple",
        "data": {
            "id": user_with_apple_id.id,
            "email": user_with_apple_id.email,
            "name": user_with_apple_id.name,
            "access_token": access_token
        } if user_with_apple_id else None
    }
