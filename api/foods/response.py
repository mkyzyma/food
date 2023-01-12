from typing import List
from pydantic import validator
from domain.food.schema import FoodBase


class FoodResponse(FoodBase):
    id: int


class FoodResponseWithToppings(FoodResponse):
    toppings: List[str] = []
    __extract_toppings = validator("toppings", pre=True, allow_reuse=True)(
        lambda toppings: [t.name for t in toppings]
    )
