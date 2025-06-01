from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import traceback
from . import models
from . import schemas

#--------------- DIET ---------------

# def create_diet(db: Session, diet: schemas.DietCreate):
#     try:
#             db_diet = models.Diet(
#                 name=diet.name
#             )
#             db.add(db_diet)
#             db.flush()
#             db.refresh(db_diet)
#             return db_diet
    
#     except Exception as e:
#         print("Error creating diet:", e)
#         traceback.print_exc() 
#         raise HTTPException(status_code=500, detail="Diet creation failed")


def get_all_diets(db: Session):
    return db.query(models.Diet).all()

# def update_diet(db: Session, new_diet: schemas.DietUpdate, diet_id: int):
#     db_diet = db.query(models.Diet).filter(models.Diet.id == diet_id)

#     setattr(db_diet, "name", new_diet.name)

#     db.commit()
#     db.refresh()

#     return db_diet

# def delete_diet(db: Session, diet_id: int):
#     db_diet = db.query(models.Diet).filter(models.Diet.id == diet_id)

#     if db_diet:
#         db.delete(db_diet)
#         db.commit()
#     return 


#--------------- ALLERGY ---------------

# def create_allergy(db: Session, allergy: schemas.DietCreate):
#     try:
#             db_allergy = models.Allergy(
#                 name=allergy.name
#             )
#             db.add(db_allergy)
#             db.flush()
#             db.refresh(db_allergy)
#             return db_allergy
    
#     except Exception as e:
#         print("Error creating allergy:", e)
#         traceback.print_exc() 
#         raise HTTPException(status_code=500, detail="Allergy creation failed")


def get_all_allergies(db: Session):
    return db.query(models.Allergy).all()

# def update_allergy(db: Session, new_allergy: schemas.AllergyUpdate, allergy_id: int):
#     db_allergy = db.query(models.Allergy).filter(models.Allergy.id == allergy_id)

#     setattr(db_allergy, "name", new_allergy.name)

#     db.commit()
#     db.refresh()

#     return db_allergy

# def delete_allergy(db: Session, allergy_id: int):
#     db_allergy = db.query(models.Allergy).filter(models.Allergy.id == allergy_id)

#     if db_allergy:
#         db.delete(db_allergy)
#         db.commit()
#     return 


#--------------- RESTAURANT ---------------

def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate, user_id: int):
    try:
            db_restaurant = models.Restaurant(
                name=restaurant.name,
                city=restaurant.city,
                country=restaurant.country,
                user_id=user_id
            )
            db.add(db_restaurant)
            db.flush()
            db.refresh(db_restaurant)
            return db_restaurant
    
    except Exception as e:
        print("Error creating restaurant:", e)
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail="Restaurant creation failed")


def get_all_restaurants(db: Session):
    return db.query(models.Restaurant).all()

def get_all_user_restaurants(db: Session, user_id: int):
    return db.query(models.Restaurant).filter(models.Restaurant.user_id == user_id).all()

def update_restaurant(db: Session, new_restaurant: schemas.RestaurantUpdate, restaurant_id: int):
    data = new_restaurant.model_dump(exclude_unset=True)

    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id)
    for field, value in data.items():
        setattr(db_restaurant, field, value)

    db.commit()
    db.refresh()

    return db_restaurant

def delete_restaurant(db: Session, restaurant_id: int):
    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id)

    if db_restaurant:
        db.delete(db_restaurant)
        db.commit()
    return 
