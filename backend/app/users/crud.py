from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from . import models
from . import schemas

# ------- User Credentials --------
def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    try:
        with db.begin():
            db_user = models.User(
                username=user.username,
                email=user.email,
                hashed_password=hashed_password,
                profile_image_url=user.profile_image_url
            )
            db.add(db_user)
            db.flush()
        db.refresh(db_user)
        return db_user
    except Exception:
        raise HTTPException(status_code=500, detail="User creation failed")
    

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, db_user: models.User, update_data: schemas.UserUpdate):
    data = update_data.model_dump(exclude_unset=True)

    for field, value in data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db:Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


#-------- User Details -----------

def add_user_details(db: Session, user_details: schemas.UserDetailsCreate):
     try:
        with db.begin():
            db_user_details = models.UserDetails(
                first_name=user_details.first_name,
                last_name=user_details.last_name,
                birthdate= user_details.birthdate
            )
            db.add(db_user_details)
            db.flush()
        db.refresh(db_user_details)
        return db_user_details
     except Exception:
        raise HTTPException(status_code=500, detail="User creation failed")
     
def get_user_details_by_id(db: Session, user_id: int):
    db_user_details = db.query(models.UserDetails).filter(user_id == user_id).first()

    return db_user_details


def update_user_details(db:Session, db_user_details: models.User, user_details: schemas.UserDetailsUpdate):
    data = user_details.model_dump(exclude_unset=True)

    for field, value in data.items():
        setattr(db_user_details, field, value)

    db.commit()
    db.refresh(db_user_details)

    return db_user_details



# -------- MEASUREMENT TYPE (Blueprint) CRUD --------

def create_measurement_type(db: Session, user_id: int, data: schemas.MeasurementTypeCreate):
    blueprint = models.MeasurementBlueprint(
        user_id=user_id,
        name=data.name,
        unit=data.unit,
        is_custom=data.is_custom
    )
    db.add(blueprint)
    db.commit()
    db.refresh(blueprint)
    return blueprint


def update_measurement_type(db: Session, blueprint_id: int, update_data: schemas.MeasurementTypeUpdate):
    data = update_data.model_dump(exclude_unset=True)
     
    db_blueprint = db.query(models.MeasurementBlueprint).filter(models.MeasurementBlueprint.id == blueprint_id).first()
    
    if db_blueprint:
        for field, value in data.items():
            setattr(db_blueprint, field, value)

        db.commit()
        db.refresh(db_blueprint)
        return db_blueprint
    else:
        return None 

def get_measurement_types_by_user(db: Session, user_id: int):
    return db.query(models.MeasurementBlueprint).filter(models.MeasurementBlueprint.user_id == user_id).all()


def create_measurement_entry(db: Session, user_id: int, type_id: int, data: schemas.MeasurementEntryCreate):
    entry = models.MeasurementEntry(
        user_id=user_id,
        type_id=type_id,
        value=data.value,
        date=data.date
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def update_measurement_entry(db: Session, entry_id: int, data: schemas.MeasurementEntryUpdate):
   update_entry = data.model_dump(exclude_unset=True)

   entry_to_be_updated = db.query(models.MeasurementEntry).filter(models.MeasurementEntry.id == entry_id).first()

   if entry_to_be_updated: 
        for field, value in update_entry.items():
            setattr(entry_to_be_updated, field, value)
        
        db.commit()
        db.refresh(entry_to_be_updated)
        return(entry_to_be_updated)
   else:
       return None

def get_measurements_by_user(db: Session, user_id: int):
    return db.query(models.MeasurementEntry).filter(models.MeasurementEntry.user_id == user_id).all()
