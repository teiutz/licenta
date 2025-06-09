from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from decimal import Decimal
from typing import Optional
from ..foods.schemas import FoodReferenceMixin

class DailyNutritionStatsCreate(BaseModel):
    day: date
    user_id: int
    calories_consumed: int
    carbs_consumed: Decimal
    fats_consumed: Decimal
    saturated_fats_consumed: Decimal
    protein_consumed: Decimal
    fibre_consumed: Decimal
    sugar_consumed: Decimal
    salt_consumed: Decimal

    class Config:
            orm_mode = True

