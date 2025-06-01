from pydantic import BaseModel, Field
from datetime import datetime,timezone,date
from typing import Optional
from ..common.schemas import DietRead

# ---- user credentials ----
#base
class UserBase(BaseModel):
    username: str
    email: str
    profile_image_url: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    profile_image_url: Optional[str] = None


# ---- user personal details ----
class UserDetailsCreate(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

class UserDetailsRead(UserDetailsCreate):
    id: int
    class Config:
        orm_mode = True

class UserDetailsUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birthdate: Optional[date] = None


# ---- user diet details ----
class UserDietCreate(BaseModel):
    diet_id: int

class UserDietRead(BaseModel):
    id: int
    diet: DietRead
    class Config:
        orm_mode = True

class UserDietUpdate(BaseModel):
    diet_id: Optional[int] = None


# ---- user goals ----
class UserGoalsCreate(BaseModel):
    goal_type: str
    goal_weight: float
    is_active: bool

class UserGoalsRead(UserGoalsCreate):
    id: int
    class Config:
        orm_mode = True

class UserGoalsUpdate(BaseModel):
    goal_type: Optional[str] = None
    goal_weight: Optional[float] = None
    is_active: Optional[bool] = None


# ---- user allergies ----
class UserAllergyCreate(BaseModel):
    allergy_type: str

class UserAllergyRead(UserAllergyCreate):
    id: int
    class Config:
        orm_mode = True

class UserAllergyUpdate(BaseModel):
    allergy_type: Optional[str] = None



# ---- Measurement Type (Weight, Fat(%), Waist, Hips) ----
class MeasurementTypeBase(BaseModel):
    name: str
    unit: str

class MeasurementTypeCreate(MeasurementTypeBase):
    is_custom: bool = True

class MeasurementTypeRead(MeasurementTypeBase):
    id: int
    class Config:
        orm_mode = True

class MeasurementTypeUpdate(BaseModel):
    name: Optional[str] = None
    unit: Optional[str] = None


# ---- Entering Measurement data (75.0 kg, 30 %, etc)
class MeasurementEntryBase(BaseModel):
    value: float
    date: datetime = Field(default_factory=datetime.now(timezone.utc))

class MeasurementEntryCreate(MeasurementEntryBase):
    pass

class MeasurementEntryRead(MeasurementEntryBase):
    id: int
    class Config:
        orm_mode = True

class MeasurementEntryUpdate(BaseModel):
    value: Optional[float]
    date: Optional[datetime] = Field(default=None, title="Measurement Entry Date")

