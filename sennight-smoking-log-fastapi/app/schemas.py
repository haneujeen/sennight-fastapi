from pydantic import BaseModel
from datetime import date


class SmokingLogBase(BaseModel):
    cigarettes_smoked: int
    date: date


class SmokingLogCreate(SmokingLogBase):
    pass


class SmokingLogUpdate(SmokingLogBase):
    pass


class SmokingLogResponse(SmokingLogBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
