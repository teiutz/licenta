from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List
from ..users import User
from ..foods import FoodItem
class PantryItemEntry(Base):
    __tablename__ = "pantry_item_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="pantry_item_entries", single_parent=True)
    
    pantry_item_id: Mapped[int] = mapped_column(Integer, ForeignKey("pantry_items.id"), nullable=False)
    pantry_item: Mapped["PantryItem"] = relationship(back_populates="entries", )

    is_owned: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    #how to define a serving?? like "a carton of milk", "a bar of chocolate"

    date_bought: Mapped[datetime] = mapped_column(Date, nullable=True)
    date_spoiled: Mapped[datetime] = mapped_column(Date, nullable=True)
    expiration_date: Mapped[datetime] = mapped_column(Date, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class PantryItem(Base):
    __tablename__ = "pantry_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("pantry_item_categories.id"), nullable=False)
    category: Mapped["PantryItemCategory"] = relationship(back_populates="pantry_items", single_parent=True)

    days_in_freezer: Mapped[int] = mapped_column(Integer, nullable=True)
    days_in_fridge: Mapped[int] = mapped_column(Integer, nullable=True)
    days_on_shelf: Mapped[int] = mapped_column(Integer, nullable=True)

    serving_size: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=True)
    serving_unit: Mapped[str] = mapped_column(String, nullable=True)

    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_items.id"), nullable=True)
    linked_food_item: Mapped["FoodItem"] = relationship(back_populates="linked_pantry_item", single_parent=True)

class PantryItemCategory(Base):
    __tablename__ = "pantry_item_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True)
    pantry_items = relationship("PantryItem", back_populates="pantry_category")


