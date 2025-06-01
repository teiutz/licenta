from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List
#from ..users.models import UserDiet, UserAllergy
#from ..foods.models import FoodTag, FoodItem
#from ..meals.models import MealTag
#from ..movement.models import WorkoutTag

#       --------------- ALLERGY ---------------
class Allergy(Base):
    __tablename__ = "allergies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    #foods: Mapped[List["FoodItem"]] = relationship("FoodItem", secondary="food_allergies", backref="allergy")

    user_allergies: Mapped[List["UserAllergy"]] = relationship("UserAllergy",back_populates="allergy")
    food_allergies: Mapped[List["FoodAllergy"]] = relationship("FoodAllergy", back_populates="allergy")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


#       --------------- DIET ---------------
class Diet(Base):
    __tablename__ = "diets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    user_diets: Mapped[List["UserDiet"]] = relationship("UserDiet", back_populates="diet")
    

#       --------------- SERVING ---------------
class Serving(Base):
    __tablename__ = "servings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False)
    food_item: Mapped["FoodItem"] = relationship("FoodItem", back_populates="servings")

    size: Mapped[Decimal] = mapped_column(Numeric(6,2), nullable=True)    
    size_unit: Mapped[str] = mapped_column(String, nullable=True) #g, ml, etc.  
    serving_unit: Mapped[str] = mapped_column(String, nullable=True) #box, bar, piece      

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


    
#       --------------- TAG ---------------
class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("tag_categories.id"), nullable=False)

    food_tags: Mapped[List["FoodTag"]] = relationship(back_populates="tag")
    meal_tags: Mapped[List["MealTag"]] = relationship(back_populates="tag")
    workout_tags: Mapped[List["WorkoutTag"]] = relationship(back_populates="tag")

    category: Mapped["TagCategory"] = relationship(uselist=False)

    scope = Column(String, nullable=False) #Food, Meals,Workout

class TagCategory(Base):
    __tablename__ = "tag_categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True, unique=True)    

#       --------------- RESTAURANT ---------------

class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True, unique=True, nullable=False)
    city: Mapped[str] = mapped_column(String, index=True, nullable=True)
    country: Mapped[str] = mapped_column(String, index=True, nullable=True)
    #options? takeout? dine in?

    food_items: Mapped[List["FoodItem"]] = relationship("FoodItem")
