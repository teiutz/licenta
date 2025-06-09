from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import crud, models, schemas
from ..security.auth import get_current_user
from .models import User

food_item_router = APIRouter(
    prefix="/food-items",
    tags=["Food Items"]
)

