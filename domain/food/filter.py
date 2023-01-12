from typing import List
from pydantic import BaseModel


class FoodFilter(BaseModel):
    is_vegan: bool | None = None
    is_special: bool | None = None
    is_publish: bool | None = None

    toppings: List[str] | None = None
