from pydantic import BaseModel
from typing import Optional


class MilestonePostBase(BaseModel):
    user_id: int
    user_milestone_id: int
    quit_attempt_id: int
    content: str
    support_count: Optional[int] = 0


class MilestonePostCreate(MilestonePostBase):
    pass


class MilestonePostUpdate(MilestonePostBase):
    pass


class MilestonePost(MilestonePostBase):
    id: int

    class Config:
        from_attributes = True
