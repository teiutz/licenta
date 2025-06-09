from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime, date
from typing import List, Optional

class PantryItem(Base):
    __tablename__ = "pantry_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
   
    base_food_id: Mapped[int] = mapped_column(ForeignKey("base_foods.id"), unique=True)
    food_item_id: Mapped[Optional[int]] = mapped_column(ForeignKey("food_items.id"), unique=True)

    base_food: Mapped["BaseFood"] = relationship(back_populates="pantry_item")
    food_item: Mapped[List["FoodItem"]] = relationship(back_populates="pantry_items")

    location: Mapped[str] = mapped_column(String, nullable= False)

    days_in_freezer: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    days_in_fridge: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    days_on_shelf: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    days_in_freezer_opened: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    days_in_fridge_opened: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    days_on_shelf_opened: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    inventory_item: Mapped["PantryInventory"] = relationship(back_populates="pantry_item")

class PantryInventory(Base):
    __tablename__ = "pantry_inventory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="items_in_pantry")

    pantry_item_id: Mapped[int] = mapped_column(ForeignKey("pantry_items.id"))
    pantry_item: Mapped["PantryItem"] = relationship(back_populates="inventory_item")
    
    purchase_date: Mapped[date] = mapped_column(nullable=False)
    date_opened: Mapped[Optional[date]] = mapped_column(nullable=True)
    exp_date: Mapped[date] = mapped_column(nullable=False)
    finish_date: Mapped[Optional[date]] = mapped_column(nullable=True)

    current_qty: Mapped[Optional[Decimal]] = mapped_column(Numeric(6,2), nullable=True)
    qty_unit: Mapped[Optional[String]] = mapped_column(String, nullable=True)
    
    packaging_qty: Mapped[int] = mapped_column(nullable=False)
    packaging: Mapped[str] = mapped_column(String, nullable=False)

    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    notes: Mapped[str] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    
   