from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class QuitAttemptBase(BaseModel):
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool = True


class QuitAttemptCreate(QuitAttemptBase):
    user_id: int


class QuitAttemptUpdate(QuitAttemptBase):
    pass


class QuitAttempt(QuitAttemptBase):
    id: int

    class Config:
        from_attributes = True
