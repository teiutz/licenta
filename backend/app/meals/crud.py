from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import traceback
from . import models
from . import schemas
from ..foods.schemas import FoodReferenceMixin

def add_meal_ingredient(db: Session, meal_id: int, ingredient: schemas.MealIngredientCreate):
    try:
        db_meal_ingredient = models.MealIngredient(
            meal_id = meal_id,
            base_food_id = ingredient.base_food_id,
            food_item_id = ingredient.food_item_id,
            quantity_g = ingredient.quantity_g
        )
        db.add(db_meal_ingredient)
        db.flush()
        db.refresh(db_meal_ingredient)
        return db_meal_ingredient
    
    except Exception as e:
            print("Error adding meal ingredient:", e)
            traceback.print_exc() 
            raise HTTPException(status_code=500, detail="Ingredient adding failed")


def create_meal(db: Session, user_id: int, meal: schemas.MealCreate):

    try:
        db_meal = models.Meal(
            user_id = user_id,
            name = meal.name,
            prep_time_minutes = meal.prep_time_minutes,
            cook_time_minutes = meal.cook_time_minutes,
            instructions = meal.instructions,
            image_url = meal.image_url,
            number_of_servings = meal.number_of_servings,
        )
        db.add(db_meal)
        db.flush()
        db.refresh(db_meal)

        for ingredient in meal.ingredients:
            add_meal_ingredient(db = db, ingredient= ingredient, meal_id=db_meal.id)

        return db_meal

    except Exception as e:
        print("Error creating meal:", e)
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail="Meal creation failed")
    

def get_meal_ingredients(db: Session, meal_id: int, user_id: int):
    return (
        db.query(models.MealIngredient)
        .join(models.Meal)
        .filter(
            models.MealIngredient.meal_id == meal_id,
            models.Meal.user_id == user_id
        )
        .all()
    )

def get_meal_by_id(db: Session, meal_id: int, user_id: int):
    return (
        db.query(models.Meal)
        .filter(models.Meal.id == meal_id, 
                    models.Meal.user_id == user_id)
        .first()
    )

def get_meals_by_user(db: Session, user_id: int):
    return (
        db.query(models.Meal)
        .filter(models.Meal.user_id == user_id)
        .all()
    )

def update_meal_ingredient(db: Session,meal_id: int, user_id: int, update_data: schemas.MealIngredientUpdate, meal_ingredient_id: int):
    db_meal_ingredient = (
        db.query(models.MealIngredient)
        .join(models.Meal)
        .filter(
            models.MealIngredient.id == meal_ingredient_id,
            models.Meal.user_id == user_id,
            models.MealIngredient.meal_id == meal_id,
        )
        .first()
    )

    if not db_meal_ingredient:
        return None

    data = update_data.model_dump(exclude_unset=True)

    for field, value in data.items():
        setattr(db_meal_ingredient, field, value)

    db.commit()
    db.refresh(db_meal_ingredient)
    return db_meal_ingredient



def update_meal_by_id(db: Session, meal_id: int, user_id: int, update_data: schemas.MealUpdate):
    db_meal = (
        db.query(models.Meal)
        .filter(models.Meal.id == meal_id, models.Meal.user_id == user_id)
        .first()
    )

    if not db_meal:
        return None

    data = update_data.model_dump(exclude_unset=True, exclude={"ingredients"})

    for field, value in data.items():
        setattr(db_meal, field, value)

    db.commit()
    db.refresh(db_meal)

    if update_data.ingredients:
        for ingredient in update_data.ingredients:
            if ingredient.id:
                update_meal_ingredient(
                    db=db,
                    meal_id=meal_id,
                    user_id=user_id,
                    update_data=ingredient,
                    meal_ingredient_id=ingredient.id
                )
            else:
                add_meal_ingredient(
                    db=db,
                    meal_id=meal_id,
                    ingredient=ingredient
                )

    return db_meal


