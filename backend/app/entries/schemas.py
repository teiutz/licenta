from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional
from ..foods import FoodItemRead, FoodVitaminsRead
from ..meals import MealRead

class FoodEntryCreate(BaseModel):
    user_id: int
    entry_date: date
    

class FoodEntryRead(BaseModel):
    id: int
    food: str
    quantity_g: float
    entry_date: Optional[date]

    food: Optional[FoodItemRead]
    vitamins: Optional[FoodVitaminsRead]
    class Config:
        orm_mode = True


class MealEntryCreate(BaseModel):
    user_id: int
    entry_date: date

class MealEntryRead(BaseModel):
    id: int
    
    meal_name: str
    meal: Optional[MealRead]
    class Config:
        orm_mode = True