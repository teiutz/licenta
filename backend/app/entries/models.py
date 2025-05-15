from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List

class FoodEntry(Base):
    __tablename__ = "food_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=False)
    quantity_g: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False) #what quantity
    serving_id: Mapped[int] = mapped_column(Integer, ForeignKey("servings.id"), nullable=True) #what type of serving, if there was

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    entry_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MealEntry(Base):
    __tablename__ = "food_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), nullable=False)
    quantity_g: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False) #what quantity
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    entry_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)