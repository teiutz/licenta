from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List, Optional

class GroceryList(Base):
    __tablename__ = "grocery_list"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())



class GroceryListItem(Base):
    __tablename__ = "grocery_list_items"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    grocery_list_id: Mapped[int] = mapped_column(ForeignKey("grocery_list.id"))

    base_food_id: Mapped[int] = mapped_column(ForeignKey("base_foods.id"), unique=True)
    food_item_id: Mapped[Optional[int]] = mapped_column(ForeignKey("food_items.id"), unique=True)

    base_food: Mapped["BaseFood"] = relationship(back_populates="grocery_list_item")
    food_item: Mapped["FoodItem"] = relationship(back_populates="grocery_list_item")

    quantity: Mapped[Decimal] = mapped_column(nullable=False)
    unit: Mapped[str] = mapped_column(nullable=False)

    notes: Mapped[Optional[str]] = mapped_column(nullable=True)