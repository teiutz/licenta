from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey,PrimaryKeyConstraint, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional
#from ..common import Tag, Allergy, Serving, Restaurant
#from ..users import User
#from ..meals import MealIngredient
#from ..pantry import PantryItem
#from ..entries import FoodEntry
class FoodItem(Base):
    __tablename__ = "food_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    brand: Mapped[str] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    user: Mapped[Optional["User"]] = relationship("User", back_populates="user_created_food_items", single_parent=True)

    base_food_id: Mapped[int] = mapped_column(ForeignKey("base_foods.id"))
    base_food: Mapped["BaseFood"] = relationship(back_populates="food_items")

    calories_100g: Mapped[Decimal] = mapped_column(Numeric(7,2), nullable=False)
    carbs_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)
    fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)
    saturated_fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)
    protein_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)
    fibre_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)
    sugar_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)
    salt_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=0.0)


    pantry_items: Mapped["PantryItem"] = relationship(back_populates="food_item")
    barcode: Mapped[str] = mapped_column(nullable=True, unique=True)
    restaurant_id: Mapped[int] = mapped_column(Integer, ForeignKey("restaurants.id"), nullable=True)

    servings: Mapped[List["FoodItemServing"]] = relationship("FoodItemServing", back_populates="food_item", cascade="all, delete-orphan")
    restaurant: Mapped["Restaurant"] = relationship("Restaurant", back_populates="food_items")
    meals_with_this: Mapped[List["MealIngredient"]] = relationship("MealIngredient", back_populates="food_item")
    grocery_list_item: Mapped["GroceryListItem"] = relationship("GroceryListItem", back_populates="food_item")
    eating_entries: Mapped[List["EatingEntry"]] = relationship("EatingEntry", back_populates="food_item")


    UniqueConstraint("name", "brand", name="uix_1")

class FoodItemServing(Base):
    __tablename__ = "food_item_servings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    food_item_id: Mapped[int] = mapped_column(ForeignKey("food_items.id"), nullable=False)
    food_item: Mapped["FoodItem"] = relationship("FoodItem", back_populates="servings")

    value: Mapped[Decimal] = mapped_column(Numeric(6,2), nullable=False)
    unit: Mapped[str] = mapped_column(String, nullable=False)

    packaging: Mapped[str] = mapped_column(String, nullable=False)
