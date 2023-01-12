import pytest
from domain.entity.topping import Topping
from domain.entity.food_category import FoodCategory
from domain.entity.food import Food
from infrastructure.db import get_db, recreate_db

from domain.food_category.repository import FoodCategoryRepository
from domain.food.repository import FoodRepository
from domain.topping.repository import ToppingRepository
from sqlalchemy.orm import Session


@pytest.fixture(autouse=True)
def run_around_tests(session: Session):
    recreate_db()

    session.add(Topping(name="Киви"))
    session.add(Topping(name="Ананас"))
    session.add(Topping(name="Миндаль"))

    session.commit()

    session.add(FoodCategory(name="Напитки", is_publish=True))
    session.add(FoodCategory(name="Гарниры", is_publish=True))
    session.add(FoodCategory(name="Секрет", is_publish=False))

    session.commit()

    session.add(
        Food(
            name="Лимонад",
            description="Лимонад",
            id_category=1,
            is_publish=True,
            is_special=False,
            is_vegan=True,
        )
    )
    session.add(
        Food(
            name="Сок",
            description="Сок",
            id_category=1,
            is_publish=True,
            is_special=False,
            is_vegan=False,
        )
    )
    session.add(
        Food(
            name="Кофе",
            description="Кофе",
            id_category=1,
            is_publish=False,
            is_special=False,
            is_vegan=False,
        )
    )

    session.add(
        Food(
            name="Картошка",
            description="Картошка",
            id_category=2,
            is_publish=True,
            is_special=False,
            is_vegan=False,
        )
    )
    session.add(
        Food(
            name="Капуста",
            description="Капуста",
            id_category=2,
            is_publish=True,
            is_special=True,
            is_vegan=False,
        )
    )
    session.add(
        Food(
            name="Морковка",
            description="Морковка",
            id_category=2,
            is_publish=False,
            is_special=False,
            is_vegan=False,
        )
    )
    session.add(
        Food(
            name="Бла бла бла",
            description="Бла бла бла",
            id_category=2,
            is_publish=True,
            is_special=False,
            is_vegan=False,
        )
    )

    session.add(
        Food(
            name="Секрет 1",
            description="Секрет 1",
            id_category=3,
            is_publish=False,
            is_special=False,
            is_vegan=False,
        )
    )
    session.add(
        Food(
            name="Секрет 2",
            description="Секрет 2",
            id_category=3,
            is_publish=True,
            is_special=False,
            is_vegan=False,
        )
    )

    session.commit()

    first_food = session.get(Food, 1)

    topping = session.get(Topping, 1)
    first_food.toppings.append(topping)

    topping = session.get(Topping, 2)
    first_food.toppings.append(topping)

    topping = session.get(Topping, 3)
    first_food.toppings.append(topping)

    session.commit()

    yield


@pytest.fixture
def session():
    return next(get_db())


@pytest.fixture
def topping_repository():
    return ToppingRepository()


@pytest.fixture
def food_repository():
    return FoodRepository()


@pytest.fixture
def category_repository():
    return FoodCategoryRepository()
