from domain.entity import Food
from domain.repository import Repository
from sqlalchemy import select
from sqlalchemy.sql import Select
from .filter import FoodFilter


class FoodRepository(Repository[Food]):
    def __init__(self):
        super().__init__(Food)

    def get_statement(self, filter: FoodFilter = None):
        stmt: Select = select(Food)

        if hasattr(filter, "is_special") and filter.is_special != None:
            stmt = stmt.where(Food.is_special == filter.is_special)

        if hasattr(filter, "is_vegan") and filter.is_vegan != None:
            stmt = stmt.where(Food.is_vegan == filter.is_vegan)

        if hasattr(filter, "is_publish"):
            stmt = stmt.where(Food.is_publish == filter.is_publish)

        return stmt
