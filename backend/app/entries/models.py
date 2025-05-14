from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class FoodEntry(Base):
    __tablename__ = "food_entries"

    id = Column(Integer, primary_key=True, index=True)

    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    quantity_g = Column(Numeric(6, 2), nullable=False) #what quantity
    serving_id = Column(Integer, ForeignKey("servings.id"), nullable=True) #what type of serving, if there was

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    entry_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MealEntry(Base):
    __tablename__ = "food_entries"

    id = Column(Integer, primary_key=True, index=True)

    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    quantity_g = Column(Numeric(6, 2), nullable=False) #what quantity
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    entry_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)