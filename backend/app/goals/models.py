from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False) #weight_loss, weight_gain, maintain, chill
    #is_active = Column(Boolean, nullable=False)


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


    
