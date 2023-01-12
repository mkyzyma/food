import pytest
from infrastructure.db import get_db
from domain.food_category.repository import FoodCategoryRepository
from domain.food_category.schema import FoodCategoryBase, FoodCategoryUpdate


def test_create_food_category(session, category_repository):
    food_category = category_repository.create(
        FoodCategoryBase(name="Напитки", is_publish=True), session
    )

    session.commit()

    assert food_category.id > 0
    assert food_category.name == "Напитки"


def test_update_food_category(session, category_repository):
    food_category = category_repository.create(
        FoodCategoryBase(name="Напитки", is_publish=True), session
    )

    session.commit()

    category_repository.update(
        food_category.id, FoodCategoryUpdate(name="Гарнир"), session
    )

    session.commit()

    assert food_category.id > 0
    assert food_category.name == "Гарнир"


def test_delete_food_category(session, category_repository):
    food_category = category_repository.create(
        FoodCategoryBase(name="Киви", is_publish=True), session
    )

    session.commit()

    category_repository.delete(food_category.id, session)

    session.commit()

    food_category = category_repository.get_by_id(food_category.id, session)

    assert food_category == None
