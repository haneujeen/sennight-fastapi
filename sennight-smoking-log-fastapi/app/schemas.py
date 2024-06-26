from pydantic import BaseModel
from datetime import date
from typing import Optional


class SmokingLogBase(BaseModel):
    cigarettes_smoked: Optional[int] = None
    date: Optional[date] = None


class SmokingLogCreate(SmokingLogBase):
    cigarettes_smoked: int


class SmokingLogUpdate(SmokingLogBase):
    pass


class SmokingLogResponse(SmokingLogBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
