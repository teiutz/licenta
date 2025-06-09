from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional, List
from decimal import Decimal

from ..common.schemas import TagRead, DietRead, AllergyRead
class BaseFoodCreate(BaseModel):
    name: str
    category_id: int
    calories_100g: Decimal
    carbs_100g: Decimal
    fats_100g: Decimal
    saturated_fats_100g: Decimal
    protein_100g: Decimal
    fibre_100g: Decimal
    sugar_100g: Decimal
    salt_100g: Decimal

    tag_ids: Optional[List[int]] = []
    diet_ids: Optional[List[int]] = []
    allergy_ids: Optional[List[int]] = []


class BaseFoodRead(BaseModel):
    id: int
    name: str
    category_id: int
    user_id: Optional[int]  

    calories_100g: Decimal
    carbs_100g: Decimal
    fats_100g: Decimal
    saturated_fats_100g: Decimal
    protein_100g: Decimal
    fibre_100g: Decimal
    sugar_100g: Decimal
    salt_100g: Decimal

    tags: List[TagRead] = []
    allergies: List[AllergyRead] = []
    diets: List[DietRead] = []

    class Config:
        orm_mode = True

class BaseFoodUpdate(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None

    calories_100g: Optional[Decimal] = None
    carbs_100g: Optional[Decimal] = None
    fats_100g: Optional[Decimal] = None
    saturated_fats_100g: Optional[Decimal] = None
    protein_100g: Optional[Decimal] = None
    fibre_100g: Optional[Decimal] = None
    sugar_100g: Optional[Decimal] = None
    salt_100g: Optional[Decimal] = None

    tag_ids: Optional[List[int]] = None
    diet_ids: Optional[List[int]] = None
    allergy_ids: Optional[List[int]] = None

