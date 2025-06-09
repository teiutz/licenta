from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import traceback
from . import models
from . import schemas


def update_nutrition_goals(db: Session, nutrition_goals_id: int, user_id: int, update_data: schemas.NutritionGoalsUpdate):
    db_nutrition_goals = (
        db.query(models.NutritionGoals)
        .filter(models.NutritionGoals.id == nutrition_goals_id,
                models.NutritionGoals.user_id == user_id)
        .first()
    )
    if not db_nutrition_goals:
        raise HTTPException(status_code=404, detail="Nutrition goals not found") 
    
    elif db_nutrition_goals.is_custom is False:
        raise HTTPException(status_code=403, detail="Nutrition goals are not customizable")
    
    else:
        data = update_data.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(db_nutrition_goals, field, value)

        db.commit()
        db.refresh(db_nutrition_goals)

        return db_nutrition_goals

     

def update_movement_goals(db: Session, movement_goals_id: int, user_id: int, update_data: schemas.MovementGoalsUpdate):
    db_movement_goals = (
        db.query(models.MovementGoals)
        .filter(models.MovementGoals.id == movement_goals_id,
                models.MovementGoals.user_id == user_id)
        .first()
    )
    if not db_movement_goals:
        raise HTTPException(status_code=404, detail="Movement goals not found") 
    
    elif db_movement_goals.is_custom is False:
        raise HTTPException(status_code=403, detail="Movement goals are not customizable")
    
    else:
        data = update_data.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(db_movement_goals, field, value)

        db.commit()
        db.refresh(db_movement_goals)

        return db_movement_goals



     
