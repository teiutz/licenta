from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional

class BaseFood(Base):
    __tablename__ = "base_foods"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("base_food_categories.id"))
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)

    calories_100g: Mapped[Decimal] = mapped_column(Numeric(7,2), nullable=False)
    carbs_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    saturated_fats_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    protein_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    fibre_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    sugar_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    salt_100g: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)

    category: Mapped["BaseFoodCategory"] = relationship(back_populates="base_foods")
    food_items: Mapped[List["FoodItem"]] = relationship(back_populates="base_food")
    pantry_item: Mapped["PantryItem"] = relationship(back_populates="base_food")
    meals_with_this: Mapped[List["MealIngredient"]] = relationship(back_populates="base_food")
    grocery_list_item: Mapped[List["GroceryListItem"]] = relationship(back_populates="base_food")
    eating_entries: Mapped[List["EatingEntry"]] = relationship(back_populates="base_food")


    base_food_allergies: Mapped[List["BaseFoodAllergy"]] = relationship(back_populates="base_food")
    base_food_diets: Mapped[List["BaseFoodDiet"]] = relationship(back_populates="base_food")
    base_food_tags: Mapped[List["BaseFoodTag"]] = relationship(back_populates= "base_food")
    base_food_servings: Mapped[List["BaseFoodServing"]] = relationship(back_populates="base_food")
    # base_food_vitamins: Mapped[List["BaseFoodVitamins"]] = relationship(back_populates="base_food_vitamins")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class BaseFoodCategory(Base):
    __tablename__ = "base_food_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False, unique=True)

    base_foods: Mapped[List["BaseFood"]] = relationship("BaseFood", back_populates="category")

class BaseFoodTag(Base):
    __tablename__ = "base_food_tags"

    base_food_id: Mapped[int] = mapped_column(ForeignKey("base_foods.id"), nullable=False, primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), nullable=False, primary_key=True)

    base_food: Mapped["BaseFood"] = relationship("BaseFood", back_populates="base_food_tags")
    tag: Mapped["Tag"] = relationship("Tag", back_populates="base_food_tags")


class BaseFoodAllergy(Base):
    __tablename__ = "base_food_allergies"

    base_food_id: Mapped[int] = mapped_column(Integer, ForeignKey("base_foods.id"), nullable=False, primary_key=True)
    allergy_id: Mapped[int] = mapped_column(Integer, ForeignKey("allergies.id"), nullable=False, primary_key=True)
    
    base_food: Mapped["BaseFood"] = relationship("BaseFood", back_populates="base_food_allergies")
    allergy: Mapped["Allergy"] = relationship("Allergy", back_populates="base_food_allergies")

class BaseFoodDiet(Base):
    __tablename__ = "base_food_diets"

    base_food_id: Mapped[int] = mapped_column(Integer, ForeignKey("base_foods.id"), nullable=False, primary_key=True)
    diet_id: Mapped[int] = mapped_column(Integer, ForeignKey("diets.id"), nullable=False, primary_key=True)
    
    base_food: Mapped["BaseFood"] = relationship("BaseFood", back_populates="base_food_diets")
    diet: Mapped["Diet"] = relationship("Diet", back_populates="base_food_diets")

# class BaseFoodVitamins(Base):
#     __tablename__ = "base_food_vitamins"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     base_food_id: Mapped[int] = mapped_column(Integer, ForeignKey("base_foods.id"), nullable=False)
    
#     base_food: Mapped["BaseFood"] = relationship(back_populates="base_food_vitamins", uselist=False)

#     vit_a_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_c_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_d_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_e_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_k_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_b1_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_b6_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_b9_100g: Mapped[int] = mapped_column(Integer, nullable=False)
#     vit_b12_100g: Mapped[Decimal] = mapped_column(Numeric(5,2), nullable=False)
#     vit_b3_100g: Mapped[int] = mapped_column(Integer, nullable=False)

class BaseFoodServing(Base):
    __tablename__ = "base_food_servings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    base_food_id: Mapped[int] = mapped_column(Integer, ForeignKey("base_foods.id"), nullable=False)
    base_food: Mapped["BaseFood"] = relationship(back_populates="base_food_servings")

    #for one packaging
    value: Mapped[Decimal] = mapped_column(Numeric(6,2), nullable=False)
    unit: Mapped[str] = mapped_column(String, nullable=False)

    packaging: Mapped[str] = mapped_column(String, nullable=False)
