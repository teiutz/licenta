from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List
from ..users import UserGoal, User

class Goal(Base):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False) #weight_loss, weight_gain, maintain, chill
    
    user_goals: Mapped[List["UserGoal"]] = relationship(back_populates="goal")
    
    #is_active: Mapped[] = mapped_column(Boolean, nullable=False)

class NutritionGoals(Base):
    __tablename__ = "nutrition_goals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="nutrition_goals", single_parent=True)

    calories_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    carbs_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fats_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    saturated_fats_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    protein_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fibre_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    sugar_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    salt_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class MovementGoals(Base):
    __tablename__ = "movement_goals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped[int] = relationship(back_populates="movement_goals", single_parent=True)

    cals_burned: Mapped[Decimal] = mapped_column(Numeric(6,1), nullable=False)
    stepCount: Mapped[int] = mapped_column(Integer, nullable=False)
    distance: Mapped[int] = mapped_column(Integer, nullable=False)

    cardio_per_week: Mapped[int] = mapped_column(Integer, nullable=True) #!!!
    strength_per_week: Mapped[int] = mapped_column(Integer, nullable=True) #!!!

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())



    
