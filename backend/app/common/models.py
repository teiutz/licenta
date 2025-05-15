from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List
from ..users import UserDiet, UserAllergy
from ..foods import FoodTag, FoodItem
from ..meals import MealTag
from ..movement import WorkoutTag

#       --------------- ALLERGY ---------------
class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    foods = relationship("FoodItem", secondary="food_allergies", backref="allergy")

    user_allergies: Mapped[List["UserAllergy"]] = relationship(back_populates="allergy")

    created_at = Column(DateTime, default=func.now(), nullable=False)

#       --------------- DIET ---------------
class Diet(Base):
    __tablename__ = "diets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    users: Mapped[List["UserDiet"]] = relationship(back_populates="diet")
    #is_Active = Column(Boolean, nullable=False)

#       --------------- SERVING ---------------
class Serving(Base):
    __tablename__ = "servings"

    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    food_item = relationship("FoodItem", back_populates="servings")

    size = Column(Numeric(6, 2), nullable=True) #numeric value        
    size_unit = Column(String, nullable=True) #g, ml, etc.  
    serving_unit = Column(String, nullable=True) #box, bar, piece      

    created_at = Column(DateTime, default=func.now(), nullable=False)

    
#       --------------- TAG ---------------
class TagCategory(Base):
    __tablename__ = "tag_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True, unique=True)    

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey("tag_categories.id"), nullable=False)

    food_tags: Mapped[List["FoodTag"]] = relationship(back_populates="tag")
    meal_tags: Mapped[List["MealTag"]] = relationship(back_populates="tag")
    workout_tags: Mapped[List["WorkoutTag"]] = relationship(back_populates="tag")

    category = relationship(uselist=False)

    scope = Column(String, nullable=False) #Food, Meals,Workout

#       --------------- RESTAURANT ---------------

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    city = Column(String, index=True, nullable=True)
    country = Column(String, index=True, nullable=True)
    #options? takeout? dine in?

    food_items: Mapped[List["FoodItem"]] = relationship()
