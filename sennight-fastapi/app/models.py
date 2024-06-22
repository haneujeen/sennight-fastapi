from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(50))
    hashed_password = Column(String(255))
