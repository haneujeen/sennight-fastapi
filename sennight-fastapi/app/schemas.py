from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class QuitLogBase(BaseModel):
    quit_date: Optional[date] = None
    daily_cigarettes: Optional[int] = None
    cigarette_price: Optional[float] = None
    is_active: Optional[bool] = True


class QuitLogCreate(QuitLogBase):
    pass


class QuitLogUpdate(QuitLogBase):
    pass


class QuitLog(QuitLogBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class SmokingLogBase(BaseModel):
    cigarettes_smoked: int
    date: Optional[date] = None


class SmokingLogUpdate(SmokingLogBase):
    pass


class SmokingLogCreate(SmokingLogBase):
    pass


class SmokingLog(SmokingLogBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class MotivationBase(BaseModel):
    category: str
    message: str


class MotivationCreate(MotivationBase):
    pass


class Motivation(MotivationBase):
    id: int

    class Config:
        from_attributes = True


class UserMotivationBase(BaseModel):
    message: Optional[str] = None


class UserMotivationCreate(UserMotivationBase):
    motivation_id: int


class UserMotivationUpdate(UserMotivationBase):
    motivation_id: int


class UserMotivation(UserMotivationBase):
    id: int
    user_id: int
    motivation_id: int
    motivation: Motivation

    class Config:
        from_attributes = True


class MilestoneBase(BaseModel):
    title: str
    content: str


class MilestoneCreate(MilestoneBase):
    pass


class Milestone(MilestoneBase):
    id: int

    class Config:
        from_attributes = True


class UserMilestoneBase(BaseModel):
    date_achieved: Optional[datetime] = None


class UserMilestoneCreate(UserMilestoneBase):
    milestone_id: int


class UserMilestone(UserMilestoneBase):
    id: int
    user_id: int
    milestone_id: int
    milestone: Milestone

    class Config:
        from_attributes = True


class FactorBase(BaseModel):
    category: str
    name: str


class FactorCreate(FactorBase):
    pass


class Factor(FactorBase):
    id: int

    class Config:
        from_attributes = True


class UserFactorBase(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class UserFactorCreate(UserFactorBase):
    factor_id: int


class UserFactorUpdate(UserFactorBase):
    pass


class UserFactor(UserFactorBase):
    id: int
    user_id: int
    factor_id: int
    factor: Factor

    class Config:
        from_attributes = True


class SymptomBase(BaseModel):
    title: str
    description: str


class SymptomCreate(SymptomBase):
    pass


class Symptom(SymptomBase):
    id: int

    class Config:
        from_attributes = True


class UserSymptomBase(BaseModel):
    pass


class UserSymptomCreate(UserSymptomBase):
    symptom_id: int


class UserSymptom(UserSymptomBase):
    id: int
    user_id: int
    symptom_id: int
    symptom: Symptom

    class Config:
        from_attributes = True


class ActivityBase(BaseModel):
    category: str
    name: str


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int

    class Config:
        from_attributes = True


class UserActivityBase(BaseModel):
    pass


class UserActivityCreate(UserActivityBase):
    activity_id: int


class UserActivity(UserActivityBase):
    id: int
    user_id: int
    activity_id: int
    activity: Activity

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    name: Optional[str] = None
    password: Optional[str] = None


class UserLogin(UserBase):
    name: Optional[str] = None
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    quit_logs: List[QuitLog] = []
    smoking_logs: List[SmokingLog] = []
    motivation: Optional[UserMotivation] = None
    milestones: List[UserMilestone] = []
    factors: List[UserFactor] = []
    symptoms: List[UserSymptom] = []
    activities: List[UserActivity] = []

    class Config:
        from_attributes = True
