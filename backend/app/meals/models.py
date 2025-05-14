from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    #for recipe
    prep_time_minutes = Column(Integer, nullable=True)
    cook_time_minutes = Column(Integer, nullable=True)
    instructions = Column(String, nullable=True)
    complexity = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    number_of_servings = Column(Integer, nullable=True)

    #mmeal_serving_g = Column(Numeric(6,2), nullable=True)

    tags = relationship("Tag", secondary="meal_tags", backref="meals")
    #servings = relationship("Serving", back_populates="food", cascade="all, delete-orphan")
    foods = relationship("FoodItem", back_populates="meals", secondary="meal_foods")


class MealTag(Base):
    __tablename__ = "meal_tags"

    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('meal_id', 'tag_id'))

class MealIngredient(Base):
    __tablename__ = "meal_ingredients"

    meal_id = Column(Integer, ForeignKey("meals.id"), primary_key=True)
    food_id = Column(Integer, ForeignKey("food_items.id"), primary_key=True)

    quantity = Column(Numeric(5,2), nullable=False)
    quantity_unit = Column(String, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('meal_id', 'food_id'))
