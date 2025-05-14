from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship
# SCHIMBARIII CU MAP
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    cals_burned_per_hour = Column(Numeric(6,1), nullable=False) #??

    tags = relationship("Tag", secondary="workout_tags", back_populates="workouts")

class WorkoutTag(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

class WorkoutCategory(Base):
    __tablename__ = "workout_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)

class WorkoutEntry(Base):
    __tablename__ = "workout_entries"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"), nullable=False)
    time_min = Column(Integer, nullable=True)

    #if strength training
    reps = Column(Integer, nullable=True)
    sets = Column(Integer, nullable=True)
    rest_seconds = Column(Integer, nullable=True)

    cals_burned = Column(Numeric(6,1), nullable=False)