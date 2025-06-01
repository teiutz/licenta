from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..users import crud, schemas, models
from .hashing import hash_password, verify_password
from .token import create_token
from .schemas import LoginRequest

security_router = APIRouter(
    prefix="", #for path
    tags=["security"] #for docs, to find
    )


@security_router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user.password)
    new_user = crud.create_user(db, user, create_hashed_password=hashed)
    return {"msg": "User created", "user_id": new_user.id}


@security_router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(user.id)
    return {"access_token": token, "token_type": "bearer", "user_id": user.id}
