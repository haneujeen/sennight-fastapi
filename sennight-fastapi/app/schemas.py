from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import date, datetime


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


class UserUpdate(BaseModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    daily_cigarettes: Optional[int] = None
    cigarette_price: Optional[float] = None


class PrimaryGoalResponse(BaseModel):
    id: int
    user_id: int
    category: str
    description: str

    class Config:
        orm_mode = True


class MilestoneResponse(BaseModel):
    id: int
    user_id: int
    key: str
    title: str
    description: str
    date_achieved: date

    class Config:
        orm_mode = True


class FactorsResponse(BaseModel):
    id: int
    user_id: int
    category: str
    title: str

    class Config:
        orm_mode = True


class SymptomsResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class ActivityResponse(BaseModel):
    id: int
    user_id: int
    category: str
    title: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    start_date: Optional[date] = None
    daily_cigarettes: Optional[int] = None
    cigarette_price: Optional[float] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    primary_goal: Optional[PrimaryGoalResponse] = None
    milestones: List[MilestoneResponse] = []
    factors: List[FactorsResponse] = []
    symptoms: List[SymptomsResponse] = []
    activities: List[ActivityResponse] = []

    class Config:
        orm_mode = True


class PrimaryGoalCreate(BaseModel):
    category: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)


class PrimaryGoalUpdate(BaseModel):
    category: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=255)


class MilestoneCreate(BaseModel):
    key: str = Field(..., max_length=6)
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)


class FactorsCreate(BaseModel):
    category: str = Field(..., max_length=50)
    title: str = Field(..., max_length=255)


class SymptomsCreate(BaseModel):
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)


class ActivityCreate(BaseModel):
    category: str = Field(..., max_length=50)
    title: str = Field(..., max_length=255)
