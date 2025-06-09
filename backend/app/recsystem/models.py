from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey,PrimaryKeyConstraint, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional

class UserFoodFrequency(Base):
    __tablename__ = "user_foods_frequencies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    base_food_id: Mapped[int] = mapped_column(ForeignKey("base_foods.id"), nullable=False, unique=True)

    count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class UserTagFrequency(Base):
    __tablename__ = "user_tags_frequencies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.id"), unique=True)

    count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class UserMealFrequency(Base):
    __tablename__ = "user_meals_frequencies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), unique=True)

    count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class UserFoodPreference(Base):
    __tablename__ = "user_food_preferences"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    base_food_id: Mapped[Optional[int]] = mapped_column(ForeignKey("base_foods.id"), nullable=True, unique=True)
    food_item_id: Mapped[Optional[int]] = mapped_column(ForeignKey("food_items.id"), nullable=True, unique=True)


    preference: Mapped[int] = mapped_column(Integer, nullable=False, default=0) # like = 1, neutral = 0, dislike = -1

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

