from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional, List
from decimal import Decimal


class NutritionGoalsCreate(BaseModel):
    calories_goals: Decimal
    carbs_goals: Decimal
    fats_goals: Decimal
    saturated_fat_goals: Decimal
    protein_goals: Decimal
    fibre_goals: Decimal
    sugar_goals: Decimal
    salt_goals: Decimal

class NutritionGoalsRead(BaseModel):
    id: int

    user_id: int
    calories_goals: Decimal
    carbs_goals: Decimal
    fats_goals: Decimal
    protein_goals: Decimal
    fibre_goals: Decimal
    sugar_goals: Decimal
    salt_goals: Decimal

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class NutritionGoalsUpdate(BaseModel):

    calories_goals: Optional[Decimal] = None
    carbs_goals: Optional[Decimal] = None
    fats_goals: Optional[Decimal] = None
    saturated_fats_goals: Optional[Decimal] = None
    protein_goals: Optional[Decimal] = None
    fibre_goals: Optional[Decimal] = None
    sugar_goals: Optional[Decimal] = None
    salt_goals: Optional[Decimal] = None


class MovementGoalsCreate(BaseModel):
    cals_burned: Decimal
    step_count: int

    cardio_per_week_days: int
    strength_per_week_days: int

class MovementGoalsRead(BaseModel):
    id: int

    user_id: int
    cals_burned: Decimal
    step_count: int

    cardio_per_week_days: int
    strength_per_week_days: int


    class Config:
        orm_mode = True

    
class MovementGoalsUpdate(BaseModel):
    cals_burned: Optional[Decimal] = None
    step_count: Optional[int] = None

    cardio_per_week_days: Optional[int] = None
    strength_per_week_days: Optional[int] = None

