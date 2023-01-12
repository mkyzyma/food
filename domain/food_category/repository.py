from sqlalchemy.sql import Select
from sqlalchemy.orm import contains_eager, joinedload
from domain.entity import FoodCategory, Food, Topping
from domain.repository import Repository
from sqlalchemy import select
from .filter import FoodCategoryFilter


class FoodCategoryRepository(Repository[FoodCategory]):
    def __init__(self):
        super().__init__(FoodCategory)

    def get_statement(self, filter=FoodCategoryFilter):
        stmt: Select = select(FoodCategory)

        stmt = (
            stmt.join(FoodCategory.foods)
            .join(Food.toppings, isouter=True)
            .options(contains_eager(FoodCategory.foods).joinedload(Food.toppings))
        )

        if hasattr(filter, "is_publish"):
            stmt = stmt.where(Food.is_publish == filter.is_publish).where(
                FoodCategory.is_publish == filter.is_publish
            )

        if hasattr(filter, "is_vegan") and filter.is_vegan != None:
            stmt = stmt.where(Food.is_vegan == filter.is_vegan)

        if hasattr(filter, "is_special") and filter.is_special != None:
            stmt = stmt.where(Food.is_special == filter.is_special)

        if hasattr(filter, "toppings") and filter.toppings != None:
            stmt = stmt.where(Topping.name.in_(filter.toppings))

        # stmt.options(contains_eager(FoodCategory.foods))
        # if hasattr(filter, "is_publish"):
        #     stmt = stmt.options(
        #         joinedload(
        #             FoodCategory.foods.and_(Food.is_publish == filter.is_publish)
        #         )
        #     ).where(FoodCategory.is_publish == filter.is_publish)

        # if hasattr(filter, "is_vegan") and filter.is_vegan != None:
        #     stmt = (
        #         stmt.join(FoodCategory.foods)
        #         .where(Food.is_vegan == filter.is_vegan)
        #         .options(
        #             joinedload(
        #                 FoodCategory.foods.and_(Food.is_vegan == filter.is_vegan)
        #             )
        #         )
        #     )

        # if hasattr(filter, "is_special") and filter.is_special != None:
        #     stmt = (
        #         stmt.join(FoodCategory.foods)
        #         .where(Food.is_special == filter.is_special)
        #         .options(
        #             joinedload(
        #                 FoodCategory.foods.and_(Food.is_special == filter.is_special)
        #             )
        #         )
        #     )

        return stmt
