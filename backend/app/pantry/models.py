from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class PantryItemEntry(Base):
    __tablename__ = "pantry_item_entries"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pantry_item_id = Column(Integer, ForeignKey("pantry_items.id"), nullable=False)

   #how to define a serving?? like "a carton of milk", "a bar of chocolate"

    date_bought = Column(Date, nullable=True)
    date_spoiled = Column(Date, nullable=True)
    expiration_date = Column(Date, nullable=True)


class PantryItem(Base):
    __tablename__ = "pantry_items"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("pantry_item_categories.id"), nullable=False)

    days_in_freezer = Column(Integer, nullable=True)
    days_in_fridge = Column(Integer, nullable=True)
    days_on_shelf = Column(Integer, nullable=True)

    serving_size = Column(Numeric(6, 2), nullable=True)
    serving_unit = Column(String, nullable=True)

    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=True)

    pantry_category = relationship("PantryItemCategory")

class PantryItemCategory(Base):
    __tablename__ = "pantry_item_categories"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    pantry_items = relationship("PantryItem", back_populates="pantry_category")


