from typing import List
from fastapi import Depends, status, APIRouter
from domain.topping.repository import ToppingRepository
from domain.topping.schema import ToppingBase
from infrastructure.db import get_db
from .response import ToppingResponse


router = APIRouter(tags=["Toppings"])
repo = ToppingRepository()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ToppingResponse])
async def get_toppings(db=Depends(get_db)):
    return repo.load(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ToppingResponse)
async def get_topping_by_id(id: int, db=Depends(get_db)):
    return repo.get_by_id(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ToppingResponse)
async def create_topping(payload: ToppingBase, db=Depends(get_db)):
    topping = repo.create(payload, db)
    db.commit()
    db.refresh(topping)
    return topping


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=ToppingResponse)
async def update_topping(id: int, payload: ToppingBase, db=Depends(get_db)):
    topping = repo.update(id, payload, db)
    db.commit()
    db.refresh(topping)
    return topping


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_topping(id: int, db=Depends(get_db)):
    repo.delete(id, db)
    db.commit()
