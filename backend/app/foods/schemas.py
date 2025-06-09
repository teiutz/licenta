from pydantic import BaseModel, Field, HttpUrl, model_validator
from datetime import datetime,timezone,date
from typing import Optional, List
from decimal import Decimal

class FoodReferenceMixin(BaseModel):
    base_food_id: Optional[int] = None
    food_item_id: Optional[int] = None

    @model_validator(mode="after")
    def validate_food_reference(cls, model):
        if (model.base_food_id is None and model.food_item_id is None) or \
           (model.base_food_id is not None and model.food_item_id is not None):
            raise ValueError("Provide either base_food_id or food_item_id, not both.")
        return model