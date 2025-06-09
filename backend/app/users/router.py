from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import crud, models, schemas
from ..security.auth import get_current_user
from .models import User
from ..security.hashing import hash_password

user_router = APIRouter(
    prefix="/users", #for path
    tags=["Users"] #for docs, to find
    )

@user_router.get("/me", response_model= schemas.UserRead)
def get_user_route(current_user: User = Depends(get_current_user)):
    return current_user

@user_router.patch("/update", response_model=schemas.UserRead)
def update_user_by_id(
    update_data: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.update_user(db, db_user=current_user, update_data=update_data)


@user_router.delete("/delete", status_code=204)
def delete_user_by_id(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(current_user)
    db.commit()
    return  

@user_router.post("/add-details")
def create_user_details_route(user_details: schemas.UserDetailsCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_user_details(db, user_details, current_user_id=current_user.id)

@user_router.get("/get-details", response_model=schemas.UserDetailsRead)
def get_user_details_route(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.get_user_details_by_id(db, current_user.id)

@user_router.patch("/update-details", response_model=schemas.UserDetailsRead)
def update_user_details_route(update_data: schemas.UserDetailsUpdate,  db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not crud.get_user_details_by_id(db=db, user_id=current_user.id):
        raise HTTPException(status_code=404, detail="User details not found")

    return crud.update_user_details(db, db.query(models.UserDetails).filter(models.UserDetails.user_id == current_user.id).first(), update_data)

@user_router.post("/add-diet")
def create_user_details_route(user_diet: schemas.UserDietCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_user_diet(db, user_diet, current_user_id=current_user.id)
