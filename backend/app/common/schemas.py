from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional
from decimal import Decimal

#--------------- DIET ---------------

class DietCreate(BaseModel):
    name: str

#pt admin
class DietRead(DietCreate):
    id: int
    class Config:
        orm_mode = True

#pt admin
class DietUpdate(BaseModel):
    name: Optional[str] = None


#--------------- ALLERGY ---------------

class AllergyCreate(BaseModel):
    name: str

class AllergyRead(DietCreate):
    id: int
    class Config:
        orm_mode = True

class AllergyUpdate(BaseModel):
    name: Optional[str] = None


#--------------- SERVING ---------------

class ServingCreate(BaseModel):
    size: Decimal
    size_unit: str
    serving_unit: str

class ServingRead(ServingCreate):
    id: int
    class Config:
        orm_mode = True

class ServingUpdate(BaseModel):
    size: Optional[Decimal]=None
    size_unit: Optional[str]=None
    seving_unit: Optional[str]=None

#--------------- TAG ---------------

class TagCategoryCreate(BaseModel):
    name: str

class TagCategoryRead(BaseModel):
    id: int
    class Config:
        orm_mode = True

class TagCreate(BaseModel):
    name: str
    category_id: int

class TagRead(BaseModel):
    id: int
    name: str
    category: TagCategoryRead

    class Config:
        orm_mode = True

#--------------- RESTAURANT ---------------

class RestaurantCreate(BaseModel):
    name: str
    city: Optional[str] = None
    country: Optional[str] = None
    user_id: int

class RestaurantRead(RestaurantCreate):
    id: int
    class Config:
        orm_mode = True

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None