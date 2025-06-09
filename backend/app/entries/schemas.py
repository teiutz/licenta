from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from decimal import Decimal
from typing import Optional
from ..foods.schemas import FoodReferenceMixin

class EatingEntryCreate(FoodReferenceMixin):
    meal_id: Optional[int] = None
    meal_of_day_id: int
    quantity_g: Decimal
    entry_date: date

class MealOfDayCreate(BaseModel):
    name: str

class MealOfDayRead(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


class EatingEntryRead(FoodReferenceMixin):
    id: int
    meal_id: Optional[int] = None
    meal_of_day: MealOfDayRead
    quantity_g: Decimal
    entry_date: date
    class Config:
            orm_mode = True

class MealOfDayUpdate(FoodReferenceMixin):
    name: Optional[str] = None

class EatingEntryUpdate(FoodReferenceMixin):
    meal_id: Optional[int] = None
    meal_of_day_id: Optional[int] = None
    quantity_g: Optional[Decimal] = None
    entry_date: Optional[date] = None


# --------- FOOD ENTRY --------- #
# class FoodEntryBase(BaseModel):
#     food_id: int
#     serving_id: Optional[int] = Field(description= "Predefined serving option")
#     meal_of_the_day_id: int = Field(description= "Meal of the day(e.g breakfast, lunch, dinner, etc.)")
#     entry_date: date
#     quantity_g: Decimal = Field(description= "Quantity in grams")

# class FoodEntryCreate(FoodEntryBase):
#     pass

# class FoodEntryRead(FoodEntryBase):
#     id: int
#     user_id: int

#     # food: Optional[FoodItemRead]
#     # serving: Optional[ServingRead]
#     # meal_of_the_day: Optional[MealOfTheDayRead]
#     # user: Optional[UserRead]

#     created_at: datetime
#     updated_at: datetime
#     class Config:
#         orm_mode = True

# class FoodEntryUpdate(BaseModel):
#     serving_id: Optional[int] = None
#     meal_of_the_day_id: Optional[int] = None 
#     entry_date: Optional[date] = None
#     quantity_g: Optional[Decimal] = None

# # --------- MEAL OF THE DAY --------- #
# class MealOfTheDayBase(BaseModel):
#     name: str

# class MealOfTheDayCreate(BaseModel):
#     pass

# class MealOfTheDayRead(BaseModel):
#     id: int
#     name: str
#     class Config:
#         orm_mode = True

# class MealOfTheDayUpdate(BaseModel):
#     name: Optional[str] = None

# # --------- MEAL ENTRY --------- #
# class MealEntryBase(BaseModel):
#     meal_id: int
#     meal_of_the_day_id: int
#     quantity_g: Decimal = Field(description="Quantity in grams eaten of the meal")
#     entry_date: date
# class MealEntryCreate(BaseModel):
#     pass

# class MealEntryRead(BaseModel):
#     id: int
#     user_id: int
#     meal_of_the_day: MealOfTheDayRead

#     #meal: MealRead
#     #serving: ServingRead
#     #meal_of_the-
#     #user: Optional[UserRead]

    
#     class Config:
#         orm_mode = True

# class MealEntryUpdate(BaseModel):
#     quantity_g: Optional[Decimal]


