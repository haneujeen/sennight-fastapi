from fastapi import APIRouter
from ..schemas import user_schemas
from .. import security
from datetime import datetime, timezone

router = APIRouter()


@router.post("/mock/users/register")
async def register_user(user: user_schemas.UserCreate):
    created_at = datetime.now(timezone.utc)
    return {
        "status": True,
        "detail": "User registered successfully",
        "data": {
            "email": user.email,
            "created_at": created_at.isoformat()
        }
    }


@router.post("/mock/users")
async def login_user(user: user_schemas.UserLogin):
    access_token = security.create_access_token(data={"sub": str(1)})
    return {
        "status": True,
        "detail": "Login successful",
        "data": {
            "email": user.email,
            "name": user.name,
            "access_token": access_token,
            "token_type": "bearer"
        }
    }
