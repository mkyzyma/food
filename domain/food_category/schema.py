from typing import List
from pydantic import BaseModel
from pydantic_partial import create_partial_model

from domain.base.orm_base_model import OrmBaseModel


class FoodCategoryBase(OrmBaseModel):
    name: str
    is_publish: bool = False


class FoodCategoryCreate(FoodCategoryBase):
    ...


FoodCategoryUpdate = create_partial_model(FoodCategoryCreate)
