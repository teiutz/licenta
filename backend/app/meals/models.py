from sqlalchemy import Integer, String, Numeric, ForeignKey
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from typing import List, Optional
#from ..users import User
#from ..common import Tag
#from ..foods import FoodItem
#from ..entries import MealEntry

class Meal(Base):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    user: Mapped[Optional["User"]] = relationship("User", back_populates="user_created_meals")

    #for recipe
    prep_time_minutes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    cook_time_minutes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    instructions: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    image_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    number_of_servings: Mapped[int] = mapped_column(Integer, nullable=False)
    total_g: Mapped[Decimal] = mapped_column(Numeric(6,2), nullable=False)

    calories_100g: Mapped[Decimal] = mapped_column(Numeric(7,2), nullable=False)
    carbs_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    saturated_fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    protein_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fibre_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    sugar_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    salt_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)


    meal_tags: Mapped[List["MealTag"]] = relationship(back_populates="meal", cascade="all, delete-orphan")
    meal_ingredients: Mapped[List["MealIngredient"]] = relationship(back_populates="meal", cascade="all, delete-orphan")
    eating_entries: Mapped[List["EatingEntry"]] = relationship(back_populates="meal")


class MealTag(Base):
    __tablename__ = "meal_tags"

    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), nullable=False, primary_key=True)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.id"), nullable=False, primary_key=True)

    meal: Mapped["Meal"] = relationship("Meal", back_populates="meal_tags")
    tag: Mapped["Tag"] = relationship("Tag", back_populates="meal_tags")

class MealIngredient(Base):
    __tablename__ = "meal_ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), nullable=False)
    meal: Mapped["Meal"] = relationship("Meal", back_populates="meal_ingredients")

    base_food_id: Mapped[int] = mapped_column(Integer, ForeignKey("base_foods.id"))
    base_food: Mapped["BaseFood"] = relationship("BaseFood", back_populates="meals_with_this")

    food_item_id: Mapped[Optional[int]] = mapped_column(ForeignKey("food_items.id"), nullable=True)
    food_item: Mapped["FoodItem"] = relationship("FoodItem", back_populates="meals_with_this")

    quantity_g: Mapped[Decimal] = mapped_column(Numeric(5,2), nullable=False)
