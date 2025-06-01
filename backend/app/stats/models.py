from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey,PrimaryKeyConstraint, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional
#from ..users import User
class DailyNutritionStats(Base):
    __tablename__ = "nutrition-stats-daily"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    day: Mapped[datetime] = mapped_column(Date, nullable=False, index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User",back_populates="user_daily_nutrition_stats", single_parent=True)

    calories_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    carbs_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fats_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    saturated_fats_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    protein_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fibre_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    sugar_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    salt_consumed: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class DailyVitaminsStats(Base):
    __tablename__ = "vitamin-stats-daily"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    day: Mapped[datetime] = mapped_column(Date, nullable=False, index=True)

    vit_a_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_c_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_d_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_e_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_k_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b1_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b6_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b9_consumed: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b12_consumed: Mapped[Decimal] = mapped_column(Numeric(5,2), nullable=False)
    vit_b3_consumed: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class DailyMovementStats(Base):
    __tablename__ = "movement-stats-daily"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    day: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
   
    cals_burned: Mapped[Decimal] = mapped_column(Numeric(6,1), nullable=False)
    stepCount: Mapped[int] = mapped_column(Integer, nullable=False)
    distance: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())






























'''class NutritionGoals(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    calories_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    carbs_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fats_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    saturated_fats_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    protein_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fibre_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    sugar_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    salt_goals: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MovementGoals(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    cals_burned: Mapped[Decimal] = mapped_column(Numeric(6,1), nullable=False)
    stepCount: Mapped[int] = mapped_column(Integer, nullable=False)
    distance: Mapped[int] = mapped_column(Integer, nullable=False)

    cardio_per_week: Mapped[int] = mapped_column(Integer, nullable=True) #!!!
    strength_per_week: Mapped[int] = mapped_column(Integer, nullable=True) #!!!

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
'''