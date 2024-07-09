from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from .smoking_habit_schemas import SmokingHabit
from .quit_attempt import QuitAttempt
from .smoking_log import SmokingLog
from .motivation import UserMotivation
from .milestone import UserMilestone
from .aid_product import UserAidProduct
from .symptom import UserSymptom
from .activity import UserActivity


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str
    photo_filename: Optional[str] = None


class UserUpdate(UserBase):
    name: Optional[str] = None
    password: Optional[str] = None
    photo_filename: Optional[str] = None


class UserLogin(UserBase):
    name: Optional[str] = None
    password: str


class User(UserBase):
    id: int
    photo_filename: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    smoking_habit: Optional[SmokingHabit] = None
    quit_attempts: List[QuitAttempt] = []
    smoking_logs: List[SmokingLog] = []
    motivation: Optional[UserMotivation] = None
    milestones: List[UserMilestone] = []
    aid_products: List[UserAidProduct] = []
    symptoms: List[UserSymptom] = []
    activities: List[UserActivity] = []

    class Config:
        from_attributes = True
