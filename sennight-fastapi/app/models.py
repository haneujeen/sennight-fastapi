from sqlalchemy import Column, Integer, String, Date, Float, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
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

    # Relationships
    primary_goal = relationship("PrimaryGoal", back_populates="user", uselist=False, cascade="all, delete-orphan")
    milestones = relationship("Milestone", back_populates="user", cascade="all, delete-orphan")
    factors = relationship("Factors", back_populates="user", cascade="all, delete-orphan")
    symptoms = relationship("Symptoms", back_populates="user", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="user", cascade="all, delete-orphan")

    def soft_delete(self):
        self.deleted_at = func.now()


class PrimaryGoal(Base):
    __tablename__ = "primary_goals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    category = Column(String(50))
    description = Column(String(255))

    user = relationship("User", back_populates="primary_goal")


class Milestone(Base):
    __tablename__ = "milestones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    key = Column(String(6))
    title = Column(String(50))
    description = Column(String(255))
    date_achieved = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="milestones")


class Factor(Base):
    __tablename__ = "factors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    category = Column(String(50))
    title = Column(String(255))

    user = relationship("User", back_populates="factors")


class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String(50))
    description = Column(String(255))

    user = relationship("User", back_populates="symptoms")


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    category = Column(String(50))
    title = Column(String(255))

    user = relationship("User", back_populates="activities")
