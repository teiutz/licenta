from sqlalchemy import Column, Integer, Date, String, Numeric, Boolean, DateTime, func, ForeignKey, UniqueConstraint
from ..database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    profile_image_url = Column(String)

    #relationships:
    user_details = relationship("UserDetails", backref="user", uselist=False)
    goals = relationship("UserGoals", backref="user", uselist=False)
    measurements = relationship("MeasurementEntry", backref="user")
    measurement_blueprints = relationship("MeasurementBlueprint", backref="user")
    diets = relationship("Diet", backref="user")
    allergies = relationship("UserAllergy", backref="user")


    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class UserDetails(Base):
    __tablename__ = "user_details"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="user_details", cascade="all, delete-orphan")

class UserGoals(Base):
    __tablename__ = "user_goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    goal_id = Column(Integer, ForeignKey("goals.id"))
    goal_weight = Column(Numeric(5, 1), nullable=False) 
    

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    #i want to keep track of goals history
    #one active goal at a tie

    __table_args__ = (
        UniqueConstraint("user_id", "is_active", name="only_one_active_goal_per_user"),
    )

class UserDiet(Base):
    __tablename__ = "user_diet"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    diet_id = Column(Integer, ForeignKey("diets.id"), nullable=False)

    created_at = Column(DateTime, default=func.now(), nullable=False)


class UserAllergy(Base):
    __tablename__ = "user_allergies"

    allergy_id = Column(Integer, ForeignKey("allergies.id"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=func.now(), nullable=False)


class MeasurementBlueprint(Base):
    __tablename__ = "measurement_blueprint"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    is_custom = Column(Boolean, nullable=False)

    entries = relationship("MeasurementEntry", backref="blueprint")

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class MeasurementEntry(Base):
    __tablename__ = "measurement_entry"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("measurement_blueprint.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    value = Column(Numeric(5,2), nullable=False)
    date = Column(DateTime, default=func.now(), nullable=False)

class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    dark_mode = Column(Boolean, nullable=False, default=False)
    notifications_enabled = Column(Boolean, nullable=False, default=False)


    