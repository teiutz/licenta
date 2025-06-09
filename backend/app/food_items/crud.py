from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import traceback
from . import models
from . import schemas

def create_food_item(db: Session, food_item: schemas.FoodItemCreate, user_id: int):
    try:
        db_food_item = models.FoodItem(
            name = food_item.name,
            brand = food_item.brand,
            user_id = user_id,
            base_food_id = food_item.base_food_id,
            calories_100g = food_item.calories_100g,
            carbs_100g= food_item.carbs_100g,
            fats_100g= food_item.fats_100g,
            saturated_fats_100g= food_item.saturated_fats_100g,
            protein_100g= food_item.protein_100g,
            fibre_100g= food_item.fibre_100g,
            sugar_100g= food_item.sugar_100g,
            salt_100g= food_item.salt_100g,

            barcode= food_item.barcode,
            restaurant_id= food_item.restaurant_id
            )
        
        db.add(db_food_item)
        db.flush()
        db.refresh(db_food_item)
        return db_food_item
    except Exception as e:
        print("Error creating food item:", e)
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail="Food item creation failed")
   
def get_food_item_by_id(db: Session, food_id: int, user_id: int):
    return db.query(models.FoodItem).filter((models.FoodItem.id == food_id) & (models.FoodItem.user_id == user_id)).first()   

def get_food_items_by_user(db: Session, user_id: int):
    return db.query(models.FoodItem).filter(models.FoodItem.user_id == user_id).all()

def update_food_item_by_id(db: Session, food_item_id: int, user_id: int, updat_data: schemas.FoodItemUpdate):
    db_food_item = db.query(models.FoodItem).filter(models.FoodItem.id == food_item_id).first()
    
    if db_food_item.user_id != user_id:
        raise HTTPException(status_code=500, detail="Food item does not belong to current user")
    else:
        data = updat_data.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(db_food_item, field, value)

        db.commit()
        db.refresh()
    
        return db_food_item
    return
    
def delete_food_item(db: Session, food_item_id: int):
    db_food_item = db.query(models.FoodItem).filter(models.FoodItem.id == food_item_id).first()

    if db_food_item:
        db.delete(db_food_item)
        db.commit()
    return