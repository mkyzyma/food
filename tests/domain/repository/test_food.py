import pytest
from domain.food_category.schema import FoodCategoryBase
from infrastructure.db import get_db
from domain.food.repository import FoodRepository
from domain.food_category.repository import FoodCategoryRepository
from domain.food.schema import FoodCreate, FoodUpdate


def test_create_food(session, category_repository, food_repository):
    category = category_repository.get_by_id(1, session)

    food = food_repository.create(
        FoodCreate(name="Лимонад", id_category=category.id), session
    )

    session.commit()
    session.refresh(food)

    assert food.id > 0
    assert food.name == "Лимонад"

    assert food.category.name == "Напитки"


def test_update_food(session, category_repository, food_repository):
    session = next(get_db())

    category = category_repository.get_by_id(1, session)

    food = food_repository.create(
        FoodCreate(name="Лимонад", id_category=category.id), session
    )

    session.commit()

    food_repository.update(food.id, FoodUpdate(name="Сок"), session)

    session.commit()

    assert food.id > 0
    assert food.name == "Сок"


def test_delete_food(session, category_repository, food_repository):
    category = category_repository.get_by_id(1, session)

    food = food_repository.create(
        FoodCreate(name="Лимонад", id_category=category.id), session
    )

    session.commit()

    food_repository.delete(food.id, session)

    session.commit()

    food = food_repository.get_by_id(food.id, session)

    assert food == None


def test_add_topping(session, food_repository, category_repository, topping_repository):
    category = category_repository.get_by_id(1, session)

    food = food_repository.create(
        FoodCreate(name="Лимонад", id_category=category.id), session
    )

    topping = topping_repository.get_by_id(1, session)

    food.toppings.append(topping)

    session.commit()
    session.refresh(food)

    assert len(food.toppings) > 0
