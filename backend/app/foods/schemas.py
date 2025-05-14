from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional, List


class FoodItemBase(BaseModel):
    name: str
    brand: Optional[str] = None
    category_id: int
    calories_100g: float
    carbs_100g: float
    fats_100g: float
    saturated_fats_100g: Optional[float] = None
    protein_100g: float
    fibre_100g: Optional[float]
    sugar_100g: Optional[float]
    salt_100g: Optional[float]
    barcode: Optional[str] = None

class FoodItemCreate(FoodItemBase):
    user_id: Optional[int] = None
    restaurant_id: Optional[int] = None

class FoodItemRead(FoodItemBase):
    id: int
    category: Optional[str]  
    tags: List[str] = [] #default value is an empty list
    allergies: List[str] = []

    class Config:
        orm_mode = True

class FoodItemUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    category_id: Optional[int] = None
    calories_100g: Optional[float] = None
    carbs_100g: Optional[float] = None
    fats_100g: Optional[float] = None
    saturated_fats_100g: Optional[float] = None
    protein_100g: Optional[float] = None
    fibre_100g: Optional[float] = None
    sugar_100g: Optional[float] = None
    salt_100g: Optional[float] = None
    barcode: Optional[str] = None


class FoodCategoryRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class FoodVitaminsRead(BaseModel):
    id: int
    food_id: int
    vit_a_100g: int
    vit_c_100g: int
    vit_d_100g: int
    vit_e_100g: int
    vit_k_100g: int
    vit_b1_100g: int
    vit_b6_100g: int
    vit_b9_100g: int
    vit_b12_100g: float
    vit_b3_100g: int

    class Config:
        orm_mode = True


