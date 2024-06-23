from sqlalchemy import Column, Integer, String, Date, Float, DateTime, func
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(50))
    hashed_password = Column(String(255))
    start_date = Column(Date, nullable=True)
    daily_cigarettes = Column(Integer, nullable=True)
    cigarette_price = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = func.now()
