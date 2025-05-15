from sqlalchemy import Integer, String, Numeric, ForeignKey
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from typing import List, Optional
from ..users import User
from ..common import Tag
from ..foods import FoodItem

class Meal(Base):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    user: Mapped[Optional["User"]] = relationship(back_populates="user_created_meals")

    #for recipe
    prep_time_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    cook_time_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    instructions: Mapped[str] = mapped_column(String, nullable=True)
    complexity: Mapped[str] = mapped_column(String, nullable=True)
    image_url: Mapped[str] = mapped_column(String, nullable=True)
    number_of_servings: Mapped[int] = mapped_column(Integer, nullable=True)

    meal_tags: Mapped[List["MealTag"]] = relationship(back_populates="meal", cascade="all, delete-orphan")
    meal_ingredients: Mapped[List["MealIngredient"]] = relationship(back_populates="meal", cascade="all, delete-orphan")

class MealTag(Base):
    __tablename__ = "meal_tags"

    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), nullable=False, primary_key=True)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.id"), nullable=False, primary_key=True)

    meal: Mapped["Meal"] = relationship(back_populates="meal_tags")
    tag: Mapped["Tag"] = relationship(back_populates="meal_tags")

class MealIngredient(Base):
    __tablename__ = "meal_ingredients"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)

    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), nullable=False)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False)

    meal: Mapped["Meal"] = relationship(back_populates="meal_ingredients")
    food_item: Mapped["FoodItem"] = relationship(back_populates="meals_with_this")

    quantity: Mapped[Decimal] = mapped_column(Numeric(5,2), nullable=False)
    quantity_unit: Mapped[str] = mapped_column(String, nullable=False)
