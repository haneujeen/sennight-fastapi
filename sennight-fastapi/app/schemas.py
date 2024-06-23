from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str = Field(..., min_length=6, max_length=100)
    start_date: Optional[date] = None
    daily_cigarettes: Optional[int] = None
    cigarette_price: Optional[float] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str

