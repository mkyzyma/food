from typing import List
from api.foods.response import FoodResponseWithToppings
from domain.food_category.schema import FoodCategoryBase


class FoodCategoryResponse(FoodCategoryBase):
    id: int


class FoodCategoryResponseWithFoods(FoodCategoryResponse):
    foods: List[FoodResponseWithToppings]
