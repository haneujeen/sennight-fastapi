from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class QuitAttemptBase(BaseModel):
    user_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool = True


class QuitAttemptCreate(QuitAttemptBase):
    pass


class QuitAttemptUpdate(QuitAttemptBase):
    pass


class QuitAttempt(QuitAttemptBase):
    id: int

    class Config:
        from_attributes = True
