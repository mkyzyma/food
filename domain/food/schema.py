from pydantic_partial import create_partial_model
from domain.base.orm_base_model import OrmBaseModel


class FoodBase(OrmBaseModel):
    name: str
    description: str | None = None
    is_special: bool = False
    is_vegan: bool = False
    price: int = 0


class FoodCreate(FoodBase):
    is_publish: bool = True
    id_category: int


FoodUpdate = create_partial_model(FoodCreate)
