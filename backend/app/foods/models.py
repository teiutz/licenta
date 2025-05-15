from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey,PrimaryKeyConstraint, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional
from ..common import Tag, Allergy, Serving, Restaurant
from ..users import User
from ..meals import MealIngredient
from ..pantry import PantryItem

class FoodItem(Base):
    __tablename__ = "food_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    brand: Mapped[str] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    user: Mapped[Optional["User"]] = relationship(back_populates="user_created_food_items", single_parent=True)

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_categories.id"))
    category = relationship("FoodCategory", back_populates="food_items", single_parent=True)
    
    food_vitamins = relationship(back_populates="food_item", uselist=False, cascade="all, delete-orphan")

    calories_100g: Mapped[Decimal] = mapped_column(Numeric(7,2), nullable=False)
    carbs_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    saturated_fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    protein_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fibre_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    sugar_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    salt_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)

    barcode: Mapped[str] = mapped_column(nullable=True, unique=True)
    restaurant_id: Mapped[int] = mapped_column(Integer, ForeignKey("restaurant.id"), nullable=True)

    food_tags: Mapped[List["FoodTag"]] = relationship(back_populates="food_item", cascade="all, delete-orphan")
    food_allergies: Mapped[List["FoodAllergy"]] = relationship(back_populates="food_item", cascade="all, delete-orphan")
    servings: Mapped[List["Serving"]] = relationship(back_populates="food_item", cascade="all, delete-orphan")
    restaurant: Mapped["Restaurant"] = relationship(back_populates="food_tiems")
    meals_with_this: Mapped[List["MealIngredient"]] = relationship(back_populates="food_item")
    linked_pantry_item: Mapped["PantryItem"] = relationship(back_populates="linked_food_item", single_parent=True)

class FoodCategory(Base):
    __tablename__ = "food_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False, unique=True)

    food_items: Mapped[List["FoodItem"]] = relationship(back_populates="category")
class FoodTag(Base):
    __tablename__ = "food_tags"

    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False, primary_key=True)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.id"), nullable=False, primary_key=True)

    food_item: Mapped["FoodItem"] = relationship(back_populates="food_tags")
    tag: Mapped["Tag"] = relationship(back_populates="food_tags")   

class FoodAllergy(Base):
    __tablename__ = "food_allergies"

    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False, primary_key=True)
    allergy_id: Mapped[int] = mapped_column(Integer, ForeignKey("allergies.id"), nullable=False, primary_key=True)
    
    food_item: Mapped["FoodItem"] = relationship(back_populates="food_allergies")
    allergy: Mapped["Allergy"] = relationship(back_populates="food_allergies")

    __table_args__ = (PrimaryKeyConstraint('food_id', 'allergy_id'))

class FoodVitamins(Base):
    __tablename__ = "food_vitamins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False)
    
    food_item: Mapped["FoodItem"] = relationship(back_populates="food_vitamins", uselist=False)

    vit_a_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_c_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_d_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_e_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_k_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b1_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b6_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b9_100g: Mapped[int] = mapped_column(Integer, nullable=False)
    vit_b12_100g: Mapped[Decimal] = mapped_column(Numeric(5,2), nullable=False)
    vit_b3_100g: Mapped[int] = mapped_column(Integer, nullable=False)


    