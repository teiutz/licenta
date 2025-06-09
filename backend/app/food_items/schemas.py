from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional, List
from decimal import Decimal

class FoodItemCreate(BaseModel):
    name: str
    brand: Optional[str] = None
    base_food_id: int

    calories_100g: Decimal
    carbs_100g: Optional[Decimal] = 0.0
    fats_100g: Optional[Decimal] = 0.0
    saturated_fats_100g: Optional[Decimal] = 0.0
    protein_100g: Optional[Decimal] = 0.0
    fibre_100g: Optional[Decimal] = 0.0
    sugar_100g: Optional[Decimal] = 0.0
    salt_100g: Optional[Decimal] = 0.0

    barcode: Optional[str] = None
    restaurant_id: Optional[int] = None


class FoodItemRead(BaseModel):
    id: int
    name: str
    brand: Optional[str]
    base_food_id: int
    user_id: Optional[int]
    
    calories_100g: Decimal
    carbs_100g: Decimal
    fats_100g: Decimal
    saturated_fats_100g: Decimal
    protein_100g: Decimal
    fibre_100g: Decimal
    sugar_100g: Decimal
    salt_100g: Decimal

    barcode: Optional[str]
    restaurant_id: Optional[int]

    class Config:
        orm_mode = True

class FoodItemUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    base_food_id: Optional[int] = None

    calories_100g: Optional[Decimal] = None
    carbs_100g: Optional[Decimal] = None
    fats_100g: Optional[Decimal] = None
    saturated_fats_100g: Optional[Decimal] = None
    protein_100g: Optional[Decimal] = None
    fibre_100g: Optional[Decimal] = None
    sugar_100g: Optional[Decimal] = None
    salt_100g: Optional[Decimal] = None

    barcode: Optional[str] = None
    restaurant_id: Optional[int] = None


# class FoodVitaminsRead(BaseModel):
#     id: int
#     food_id: int
#     vit_a_100g: int
#     vit_c_100g: int
#     vit_d_100g: int
#     vit_e_100g: int
#     vit_k_100g: int
#     vit_b1_100g: int
#     vit_b6_100g: int
#     vit_b9_100g: int
#     vit_b12_100g: float
#     vit_b3_100g: int

#     class Config:
#         orm_mode = True


