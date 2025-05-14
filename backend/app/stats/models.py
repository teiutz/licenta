from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class DailyNutritionStats(Base):
    __tablename__ = "nutrition-stats-daily"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(Date, nullable=False, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    calories_consumed = Column(Integer, nullable=False)
    carbs_consumed = Column(Numeric(5, 2), nullable=False)
    fats_consumed = Column(Numeric(5, 2), nullable=False)
    saturated_fats_consumed = Column(Numeric(5, 2), nullable=False)
    protein_consumed = Column(Numeric(5, 2), nullable=False)
    fibre_consumed = Column(Numeric(5, 2), nullable=False)
    sugar_consumed = Column(Numeric(5, 2), nullable=False)
    salt_consumed = Column(Numeric(5, 2), nullable=False)


class DailyVitaminsStats(Base):
    __tablename__ = "vitamin-stats-daily"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(Date, nullable=False, index=True)

    vit_a_consumed = Column(Integer, nullable=False)
    vit_c_consumed = Column(Integer, nullable=False)
    vit_d_consumed = Column(Integer, nullable=False)
    vit_e_consumed = Column(Integer, nullable=False)
    vit_k_consumed = Column(Integer, nullable=False)
    vit_b1_consumed = Column(Integer, nullable=False)
    vit_b6_consumed = Column(Integer, nullable=False)
    vit_b9_consumed = Column(Integer, nullable=False)
    vit_b12_consumed = Column(Float, nullable=False)
    vit_b3_consumed = Column(Integer, nullable=False)



class DailyMovementStats(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(Date, nullable=False, index=True)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    cals_burned = Column(Numeric(6,1), nullable=False)
    stepCount = Column(Integer, nullable=False)
    distance = Column(Integer, nullable=False)

class NutritionGoals(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    calories_goals = Column(Integer, nullable=False)
    carbs_goals = Column(Numeric(5, 2), nullable=False)
    fats_goals = Column(Numeric(5, 2), nullable=False)
    saturated_fats_goals = Column(Numeric(5, 2), nullable=False)
    protein_goals = Column(Numeric(5, 2), nullable=False)
    fibre_goals = Column(Numeric(5, 2), nullable=False)
    sugar_goals = Column(Numeric(5, 2), nullable=False)
    salt_goals = Column(Numeric(5, 2), nullable=False)

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MovementGoals(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    cals_burned = Column(Numeric(6,1), nullable=False)
    stepCount = Column(Integer, nullable=False)
    distance = Column(Integer, nullable=False)

    cardio_per_week = Column(Integer, nullable=True) #!!!
    strength_per_week = Column(Integer, nullable=True) #!!!
