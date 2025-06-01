from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import crud, models, schemas
from ..security.auth import get_current_user
from .models import User


common_router = APIRouter(
    prefix="/", #for path
    tags=["Common Data"] #for docs, to find
    )

# @common_router.post("/add-diet", response_model= schemas.DietReadRead)
# def create_diet_route(
#     diet: schemas.DietCreate,
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):

#     return crud.create_diet(db, diet=diet)

@common_router.get("/get-diets", response_model=list[schemas.DietRead])
def get_all_diets_route(
    db: Session = Depends(get_db)
):
    return crud.get_all_diets(db)
    
@common_router.get("/get-allergies", response_model=list[schemas.AllergyRead])
def get_all_allergies_route(
    db: Session = Depends(get_db)
):
    return crud.get_all_allergies(db)

@common_router.get("/get-restaurants", response_model=list[schemas.RestaurantRead])
def get_all_restaurants_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user.id

    predefined_restaurants = crud.get_all_restaurants(db)
    user_defined_restaurants = crud.get_all_user_restaurants(db, user_id=user_id)

    all_restaurants = list(predefined_restaurants) + list(user_defined_restaurants)

    return all_restaurants

# @common_router.post("/create-restaurant", response_model=schemas.RestaurantRead)
# def create_restaurant_route(
#     restaurant: schemas.RestaurantCreate,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     if not current_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user_id = current_user.id
#     return crud.create_restaurant(db, restaurant=restaurant, user_id=user_id)

# @common_router.patch("/update-restaurant", response_model=schemas.RestaurantRead)
# def update_restaurant_route(
#     restaurant: schemas.RestaurantCreate,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     if not current_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user_id = current_user.id
#     return crud.create_restaurant(db, restaurant=restaurant, user_id=user_id)

