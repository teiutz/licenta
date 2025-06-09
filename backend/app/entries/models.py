from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime, date
from typing import List, Optional
#from ..foods import FoodItem
#from ..users import User
#from ..meals import Meal
class EatingEntry(Base):
    __tablename__ = "eating_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
   
    base_food_id: Mapped[int] = mapped_column(Integer, ForeignKey("base_foods.id"))
    food_item_id: Mapped[Optional[int]] = mapped_column(ForeignKey("food_items.id"), nullable=True)
    meal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("meals.id"), nullable=True)
    meal_of_day_id: Mapped[int] = mapped_column(Integer, nullable=False)

    base_food: Mapped["BaseFood"] = relationship(back_populates="eating_entries")
    food_item: Mapped["FoodItem"] = relationship(back_populates="eating_entries")
    meal: Mapped["Meal"] = relationship("Meal", back_populates="eating_entries")

    quantity_g: Mapped[Decimal] = mapped_column(nullable=False)
    entry_date: Mapped[date] = mapped_column(nullable=False)
   
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MealOfDay(Base):
    __tablename__ = "meals_of_day"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable= False)
    