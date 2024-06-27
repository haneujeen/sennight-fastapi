from sqlalchemy import Column, Integer, Date
from datetime import datetime, timezone
from .database import Base


class SmokingLog(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    cigarettes_smoked = Column(Integer, nullable=False)
    date = Column(Date, default=lambda: datetime.now(timezone.utc).date())
