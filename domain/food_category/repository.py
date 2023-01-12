from sqlalchemy.sql import Select
from sqlalchemy.orm import selectinload, joinedload
from domain.entity import FoodCategory, Food
from domain.repository import Repository
from sqlalchemy import select
from .filter import FoodCategoryFilter


class FoodCategoryRepository(Repository[FoodCategory]):
    def __init__(self):
        super().__init__(FoodCategory)

    def get_statement(self, filter=FoodCategoryFilter):
        stmt: Select = select(FoodCategory)

        if hasattr(filter, "is_publish"):
            stmt = stmt.options(
                joinedload(
                    FoodCategory.foods.and_(Food.is_publish == filter.is_publish)
                )
            ).where(FoodCategory.is_publish == filter.is_publish)

        if hasattr(filter, "is_vegan") and filter.is_vegan != None:
            stmt = (
                stmt.join(FoodCategory.foods)
                .where(Food.is_vegan == filter.is_vegan)
                .options(
                    joinedload(
                        FoodCategory.foods.and_(Food.is_vegan == filter.is_vegan)
                    )
                )
            )

        if hasattr(filter, "is_special") and filter.is_special != None:
            stmt = (
                stmt.join(FoodCategory.foods)
                .where(Food.is_special == filter.is_special)
                .options(
                    joinedload(
                        FoodCategory.foods.and_(Food.is_special == filter.is_special)
                    )
                )
            )

        return stmt
