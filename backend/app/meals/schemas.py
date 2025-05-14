from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional, List

class MealBase(BaseModel):
    name: str
    prep_time_minutes: Optional[str]
    cook_time_minutes: Optional[str]
    instructions: Optional[str]
    complexity: Optional[str]
    image_url: Optional[str]
    number_of_servings: Optional[str]

class MealCreate(MealBase):
    user_id: Optional[int] = None

class MealRead(MealBase):
    id: int
    ingredients: List[str] = []
    tags: List[str] = []

    class Config:
        orm_mode = True

class MealUpdate(BaseModel): #only user's meals
    name: Optional[str] = None
    prep_time_minutes: Optional[str] = None
    cook_time_minutes: Optional[str] = None
    instructions: Optional[str] = None
    complexity: Optional[str] = None
    image_url: Optional[str] = None
    number_of_servings: Optional[str] = None