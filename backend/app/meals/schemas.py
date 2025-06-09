from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime,timezone,date
from typing import Optional, List
from decimal import Decimal
from ..foods.schemas import FoodReferenceMixin

class MealIngredientCreate(FoodReferenceMixin):
    quantity_g: Decimal

class MealCreate(BaseModel):
    name: str
    prep_time_minutes: Optional[int] = None
    cook_time_minutes: Optional[int] = None
    instructions: Optional[str] = None

    image_url: Optional[str] = None
    number_of_servings: int

    ingredients: List[MealIngredientCreate] = []

class MealIngredientRead(FoodReferenceMixin):
    id: int
    food_name: str  # coming from the related food
    quantity_g: Decimal
    class Config:
        orm_mode = True

class NutritionalInfo(BaseModel):
    calories: Decimal
    carbs: Decimal
    fats: Decimal
    protein: Decimal
    fibre: Decimal
    sugar: Decimal
    salt: Decimal
class MealRead(BaseModel):
    id: int
    name: str

    prep_time_minutes: Optional[int]
    cook_time_minutes: Optional[int]
    instructions: Optional[str]
    image_url: Optional[HttpUrl]
    number_of_servings: int

    per_100g: NutritionalInfo
    per_serving: NutritionalInfo

    ingredients: List[MealIngredientRead]
    class Config:
        orm_mode = True


class MealIngredientUpdate(FoodReferenceMixin):
    id: Optional[int] = None
    quantity_g: Optional[Decimal] = None

class MealUpdate(BaseModel):
    name: Optional[str] = None
    prep_time_minutes: Optional[int] = None
    cook_time_minutes: Optional[int] = None
    instructions: Optional[str] = None
    image_url: Optional[HttpUrl] = None
    number_of_servings: Optional[int] = None

    ingredients: Optional[List[MealIngredientUpdate]] = None

