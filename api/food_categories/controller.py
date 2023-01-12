from typing import List
from fastapi import Depends, status, APIRouter
from domain.food.filter import FoodFilter
from domain.food_category.repository import FoodCategoryRepository
from domain.food_category.schema import (
    FoodCategoryCreate,
    FoodCategoryUpdate,
)
from infrastructure.db import get_db
from .response import FoodCategoryResponse, FoodCategoryResponseWithFoods

router = APIRouter(tags=["FoodCategories"])
repo = FoodCategoryRepository()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[FoodCategoryResponseWithFoods],
)
def get_food_categories(
    is_special: bool | None = None, is_vegan: bool | None = None, db=Depends(get_db)
):
    categories = repo.load(
        db, FoodFilter(is_publish=True, is_vegan=is_vegan, is_special=is_special)
    )
    return categories


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=FoodCategoryResponseWithFoods,
)
async def get_food_category_by_id(id: int, db=Depends(get_db)):
    return repo.get_by_id(id, db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=FoodCategoryResponse
)
async def create_food_category(payload: FoodCategoryCreate, db=Depends(get_db)):
    food_category = repo.create(payload, db)
    db.commit()
    db.refresh(food_category)
    return food_category


@router.patch(
    "/{id}", status_code=status.HTTP_200_OK, response_model=FoodCategoryResponse
)
async def update_food_category(
    id: int, payload: FoodCategoryUpdate, db=Depends(get_db)
):
    food_category = repo.update(id, payload, db)
    db.commit()
    db.refresh(food_category)
    return food_category


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_food_category(id: int, db=Depends(get_db)):
    repo.delete(id, db)
    db.commit()
