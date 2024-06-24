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


class MotivationResponse(BaseModel):
    id: int
    user_id: int
    category: str
    description: str

    class Config:
        from_attributes = True


class MilestoneResponse(BaseModel):
    id: int
    user_id: int
    key: str
    title: str
    description: str
    date_achieved: datetime

    class Config:
        from_attributes = True


class FactorResponse(BaseModel):
    id: int
    user_id: int
    category: str
    title: str
    start_date: date
    end_date: Optional[date]

    class Config:
        from_attributes = True


class SymptomResponse(BaseModel):
    id: int
    user_id: int
    key: str
    title: str
    description: str

    class Config:
        from_attributes = True


class ActivityResponse(BaseModel):
    id: int
    user_id: int
    key: str
    category: str
    title: str

    class Config:
        from_attributes = True


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
    motivations: List[MotivationResponse] = []
    milestones: List[MilestoneResponse] = []
    factors: List[FactorResponse] = []
    symptoms: List[SymptomResponse] = []
    activities: List[ActivityResponse] = []

    class Config:
        from_attributes = True


class MotivationCreate(BaseModel):
    key: str = Field(..., max_length=6)
    category: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)


class MilestoneCreate(BaseModel):
    key: str = Field(..., max_length=6)
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)


class FactorCreate(BaseModel):
    category: str
    title: str
    start_date: date
    end_date: Optional[date] = None


class FactorUpdate(BaseModel):
    category: str
    title: str
    start_date: date
    end_date: Optional[date] = None


class SymptomCreate(BaseModel):
    key: str = Field(..., max_length=6)
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)


class ActivityCreate(BaseModel):
    key: str = Field(..., max_length=6)
    category: str = Field(..., max_length=50)
    title: str = Field(..., max_length=255)
