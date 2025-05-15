from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey,PrimaryKeyConstraint, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional
from ..common import Tag
# SCHIMBARIII CU MAP

class Workout(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("workout_categories.id"), nullable=False)
    category: Mapped["WorkoutCategory"] = relationship(back_populates="workouts", single_parent=True)

    cals_burned_per_hour: Mapped[Decimal] = mapped_column(Numeric(6,1), nullable=False) #??
    workout_tags: Mapped[List["WorkoutTag"]] = relationship(back_populates="workout", cascade="all, delete-orphan")

    entries: Mapped[List["WorkoutEntry"]] = relationship(back_populates="workout")
class WorkoutTag(Base):
    __tablename__ = "workout_tags"

    workout_id: Mapped[int] = mapped_column(ForeignKey("workouts.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)

    workout: Mapped["Workout"] = relationship(back_populates="workout_tags")
    tag: Mapped["Tag"] = relationship(back_populates="workout_tags")

class WorkoutCategory(Base):
    __tablename__ = "workout_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)

    workouts: Mapped[List["Workout"]] = relationship(back_populates="category")

class WorkoutEntry(Base):
    __tablename__ = "workout_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workout_id: Mapped[int] = mapped_column(Integer, ForeignKey("workouts.id"), nullable=False)
    workout: Mapped["Workout"] = relationship(back_populates="entries", single_parent=True)

    time_min: Mapped[int] = mapped_column(Integer, nullable=True)

    reps: Mapped[int] = mapped_column(Integer, nullable=True)
    sets: Mapped[int] = mapped_column(Integer, nullable=True)
    rest_seconds: Mapped[int] = mapped_column(Integer, nullable=True)

    cals_burned: Mapped[Decimal] = mapped_column(Numeric(6,1), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

