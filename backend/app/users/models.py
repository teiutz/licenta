from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from decimal import Decimal
from ..database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from typing import List
from ..common import Diet, Allergy
from ..goals import Goal
from ..foods import FoodItem
from ..goals import NutritionGoals, MovementGoals
from ..meals import Meal
from ..pantry import PantryItemEntry
from ..stats import DailyNutritionStats

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    profile_image_url: Mapped[str] = mapped_column(nullable=True)

    user_details: Mapped["UserDetails"] = relationship(back_populates="user")
    user_goals: Mapped["UserGoal"] = relationship(back_populates="user")
    user_diets: Mapped[List["UserDiet"]] = relationship(back_populates="user")
    user_allergies: Mapped[List["UserAllergy"]] = relationship(back_populates="user")
    user_created_food_items: Mapped[List["FoodItem"]] = relationship(back_populates="user")
    user_created_meals: Mapped[List["Meal"]] = relationship(back_populates="user")
    nutrition_goals: Mapped["NutritionGoals"] = relationship(back_populates="user")
    movement_goals: Mapped["MovementGoals"]
    user_daily_nutrition_stats: Mapped[List["DailyNutritionStats"]] = relationship(back_populates="user")


    pantry_item_entries: Mapped[List["PantryItemEntry"]] = relationship(back_populates="pantry_item")


    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class UserDetails(Base):
    __tablename__ = "user_details"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    birthdate: Mapped[datetime] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="user_details", single_parent=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    __table_args__ = (UniqueConstraint("user_id"))

class UserGoal(Base):
    __tablename__ = "user_goals"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    goal_id: Mapped[int] = mapped_column(ForeignKey("goals.id"))

    goal_weight: Mapped[Decimal] = mapped_column(Numeric(5, 1), nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=False)
    
    user: Mapped["User"] = relationship(back_populates="user_goals")
    goal: Mapped["Goal"] = relationship(back_populates="user_goals")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class UserDiet(Base):
    __tablename__ = "user_diet"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    diet_id: Mapped[int] = mapped_column(ForeignKey("diets.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=False)

    user: Mapped["User"] = relationship(back_populates="user_diets")
    diet: Mapped["Diet"] = relationship(back_populates="user_diets")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    __table_args__ = (
    UniqueConstraint("user_id", "is_active", name="only_one_active_diet_per_user"),
)

class UserAllergy(Base):
    __tablename__ = "user_allergy"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    allergy_id: Mapped[int] = mapped_column(ForeignKey("allergies.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=False)

    user: Mapped["User"] = relationship(back_populates="user_allergies")
    allergy: Mapped["Allergy"] = relationship(back_populates="user_allergies")

    created_at: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=func.now(), onupdate=func.now())

class MeasurementBlueprint(Base):
    __tablename__ = "measurement_blueprint"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
   
    name: Mapped[str] = mapped_column(String, nullable=False)
    unit: Mapped[str] = mapped_column(String, nullable=False)

    entries: Mapped[List["MeasurementEntry"]] = relationship(backref="blueprint")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class MeasurementEntry(Base):
    __tablename__ = "measurement_entry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    blueprint_id: Mapped[int] = mapped_column(Integer, ForeignKey("measurement_blueprint.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    value: Mapped[Decimal] = mapped_column(Numeric(5,2), nullable=False)
    date: Mapped[int] = mapped_column(DateTime, default=func.now(), nullable=False)

    blueprint: Mapped["MeasurementBlueprint"] = relationship(back_populates="entries")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class UserSettings(Base):
    __tablename__ = "user_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dark_mode: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    notifications_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


    