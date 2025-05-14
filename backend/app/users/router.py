from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import crud, models, schemas

user_router = APIRouter(
    prefix="/users", #for path
    tags=["Users"] #for docs, to find
    )

@user_router.get("/{user_id}", response_model= schemas.UserRead)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_user_by_id(db, user_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@user_router.post("/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user, hashed_password="hashed_password")

#@user_router.post("/details", response_model=schemas.UserDetailsCreate)


@user_router.patch("/update/{user_id}", response_model=schemas.UserRead)
def update_user_by_id(
    user_id: int,
    update_data: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.update_user(db, db_user=user, update_data=update_data)


@user_router.delete("/delete/{user_id}", status_code=204)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return  