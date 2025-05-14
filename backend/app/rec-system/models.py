from sqlalchemy import Column, Integer, Float, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class UserFoodFrequency(Base):
    __tablename__ = "user_foods_frequencies"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))

    count = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('user_id', 'food_id'))

class UserTagFrequency(Base):
    __tablename__ = "user_tags_frequencies"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    count = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('user_id', 'tag_id'))

class UserMealFrequency(Base):
    __tablename__ = "user_meals_frequencies"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    meal_id = Column(Integer, ForeignKey("meals.id"))

    count = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('user_id', 'meal_id'))

class UserFoodPreference(Base):
    __tablename__ = "user_meals_frequencies"

    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("foods.id"))

    preference = Column(Integer, nullable=False, default=0) # like = 1, neutral = 0, dislike = -1

