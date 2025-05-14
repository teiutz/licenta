from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

#       --------------- ALLERGY ---------------
class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    foods = relationship("FoodItem", secondary="food_allergies", backref="allergies")

    created_at = Column(DateTime, default=func.now(), nullable=False)

#       --------------- DIET ---------------
class Diet(Base):
    __tablename__ = "diets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_Active = Column(Boolean, nullable=False)

#       --------------- SERVING ---------------
class Serving(Base):
    __tablename__ = "servings"

    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)

    size = Column(Numeric(6, 2), nullable=True) #numeric value        
    size_unit = Column(String, nullable=True) #g, ml, etc.  
    serving_unit = Column(String, nullable=True) #box, bar, piece      

    created_at = Column(DateTime, default=func.now(), nullable=False)

    food = relationship("FoodItem", back_populates="servings")

#       --------------- TAG ---------------
class TagCategory(Base):
    __tablename__ = "tag_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True, unique=True)    

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey("tag_categories.id"), nullable=False)

    foods = relationship("FoodItem", secondary="food_tags", backref="tags")
    meals = relationship("Meal", secondary="meal_tags", backref="tags" )
    workouts = relationship("Workout", secondary="workout_tags", backref="tags")
    category = relationship(uselist=False)

    scope = Column(String, nullable=False) #Food, Meals,Workout

#       --------------- RESTAURANT ---------------

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    city = Column(String, index=True, nullable=True)
    country = Column(String, index=True, nullable=True)
    #options? takeout? dine in?
