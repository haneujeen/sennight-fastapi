from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Milestone schemas
class MilestoneBase(BaseModel):
    title: str
    content: str


class MilestoneCreate(MilestoneBase):
    pass


class MilestoneUpdate(MilestoneBase):
    pass


class Milestone(MilestoneBase):
    id: int

    class Config:
        from_attributes = True


# UserMilestone schemas
class UserMilestoneBase(BaseModel):
    date_achieved: Optional[datetime] = None


class UserMilestoneCreate(UserMilestoneBase):
    user_id: int
    milestone_id: int


class UserMilestone(UserMilestoneBase):
    id: int
    user_id: int
    milestone_id: int
    milestone: Milestone

    class Config:
        from_attributes = True
