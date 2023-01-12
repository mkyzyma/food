from typing import List
from fastapi import Depends, status, APIRouter
from domain.food.filter import FoodFilter
from domain.food.repository import FoodRepository
from domain.topping.repository import ToppingRepository
from domain.food.schema import FoodCreate, FoodUpdate
from domain.entity import Food
from infrastructure.db import get_db
from .response import FoodResponse, FoodResponseWithToppings

router = APIRouter(tags=["Foods"])
repo = FoodRepository()


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[FoodResponseWithToppings]
)
async def get_foods(
    is_special: bool | None = None, is_vegan: bool | None = None, db=Depends(get_db)
):
    return repo.load(
        db, FoodFilter(is_publish=True, is_vegan=is_vegan, is_special=is_special)
    )


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=FoodResponseWithToppings
)
async def get_food_by_id(id: int, db=Depends(get_db)):
    return repo.get_by_id(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FoodResponse)
async def create_food(payload: FoodCreate, db=Depends(get_db)):
    food = repo.create(payload, db)
    db.commit()
    db.refresh(food)
    return food


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=FoodResponse)
async def update_food(id: int, payload: FoodUpdate, db=Depends(get_db)):
    food = repo.update(id, payload, db)
    db.commit()
    db.refresh(food)
    return food


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_food(id: int, db=Depends(get_db)):
    repo.delete(id, db)
    db.commit()


@router.patch(
    "/{id}/topping/{id_topping}",
    status_code=status.HTTP_200_OK,
    response_model=FoodResponseWithToppings,
)
async def add_topping(id: int, id_topping: int, db=Depends(get_db)):
    food = repo.get_by_id(id, db)

    topping_repository = ToppingRepository()
    topping = topping_repository.get_by_id(id_topping, db)

    food.toppings.append(topping)

    db.commit()
    db.refresh(food)

    return food
