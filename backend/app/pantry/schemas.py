from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime,timezone,date
from typing import Optional, List
from decimal import Decimal
from ..foods.schemas import FoodReferenceMixin

class PantryItemCreate(FoodReferenceMixin):

    location: str

    days_in_freezer: Optional[int] = None
    days_in_fridge: Optional[int] = None
    days_on_shelf: Optional[int] = None

    days_in_freezer_opened: Optional[int] = None
    days_in_fridge_opened: Optional[int] = None
    days_on_shelf_opened: Optional[int] = None



class PantryItemRead(FoodReferenceMixin):
    id: int
    food_name: str
    location: str

    days_in_freezer: Optional[int] = None
    days_in_fridge: Optional[int] = None
    days_on_shelf: Optional[int] = None

    days_in_freezer_opened: Optional[int] = None
    days_in_fridge_opened: Optional[int] = None
    days_on_shelf_opened: Optional[int] = None

    class Config:
        orm_mode = True


class PantryItemUpdate(FoodReferenceMixin):
    location: Optional[str] = None

    days_in_freezer: Optional[int] = None
    days_in_fridge: Optional[int] = None
    days_on_shelf: Optional[int] = None

    days_in_freezer_opened: Optional[int] = None
    days_in_fridge_opened: Optional[int] = None
    days_on_shelf_opened: Optional[int] = None