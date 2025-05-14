from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class FoodItem(Base):
    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    brand = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("food_categories"))

    category = relationship("FoodCategory", back_populates="foods")

    calories_100g = Column(Numeric(7,2), nullable=False)
    carbs_100g = Column(Numeric(5, 2), nullable=False)
    fats_100g = Column(Numeric(5, 2), nullable=False)
    saturated_fats_100g = Column(Numeric(5, 2), nullable=False)
    protein_100g = Column(Numeric(5, 2), nullable=False)
    fibre_100g = Column(Numeric(5, 2), nullable=False)
    sugar_100g = Column(Numeric(5, 2), nullable=False)
    salt_100g = Column(Numeric(5, 2), nullable=False)

    barcode = Column(String, nullable=True, unique=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"), nullable=True)

    tags = relationship("Tag", secondary="food_tags", backref="foods")
    allergies = relationship("Allergy", secondary="food_allergies",  backref="foods")
    servings = relationship("Serving", back_populates="food", cascade="all, delete-orphan")

class FoodCategory(Base):
    __tablename__ = "food_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    foods = relationship("FoodItem", back_populates="category")

class FoodTag(Base):
    __tablename__ = "food_tags"

    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('food_id', 'tag_id'))

class FoodAllergy(Base):
    __tablename__ = "food_allergies"

    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    allergy_id = Column(Integer, ForeignKey("allergies.id"), nullable=False)
    
    __table_args__ = (PrimaryKeyConstraint('food_id', 'allergy_id'))

class FoodVitamins(Base):
    __tablename__ = "food_vitamins"

    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    
    vit_a_100g = Column(Integer, nullable=False)
    vit_c_100g = Column(Integer, nullable=False)
    vit_d_100g = Column(Integer, nullable=False)
    vit_e_100g = Column(Integer, nullable=False)
    vit_k_100g = Column(Integer, nullable=False)
    vit_b1_100g = Column(Integer, nullable=False)
    vit_b6_100g = Column(Integer, nullable=False)
    vit_b9_100g = Column(Integer, nullable=False)
    vit_b12_100g = Column(Float, nullable=False)
    vit_b3_100g = Column(Integer, nullable=False)


    