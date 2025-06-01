from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime, date
from typing import List
#from ..foods import FoodItem
#from ..users import User
#from ..meals import Meal

class FoodEntry(Base):
    __tablename__ = "food_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False)
    food: Mapped["FoodItem"] = relationship("FoodItem",back_populates="entries", single_parent=True)

    quantity_g: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False) #what quantity
    serving_id: Mapped[int] = mapped_column(Integer, ForeignKey("servings.id"), nullable=True) #what type of serving, if there was

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="food_entries", single_parent="True")

    meal_of_the_day_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals_of_the_day.id"), nullable=False)
    meal_of_the_day: Mapped["MealOfTheDay"] = relationship(back_populates="food_entries", single_parent=True)

    entry_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MealEntry(Base):
    __tablename__ = "meal_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), nullable=False)
    meal: Mapped["Meal"] = relationship("Meal", back_populates="entries", single_parent=True)

    quantity_g: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False) #what quantity
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="meal_entries")

    meal_of_the_day_id: Mapped[int] = mapped_column(ForeignKey("meals_of_the_day.id"))
    meal_of_the_day: Mapped["MealOfTheDay"] = relationship(back_populates="meal_entries", single_parent=True)

    entry_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class MealOfTheDay(Base):
    __tablename__ = "meals_of_the_day"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable= False)
    day: Mapped[date] = mapped_column(index=True, nullable=False)

    food_entries: Mapped[List["FoodEntry"]] = relationship(back_populates="meal_of_the_day")
    meal_entries: Mapped[List["MealEntry"]] = relationship(back_populates="meal_of_the_day")