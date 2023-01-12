import pytest
from infrastructure.db import get_db
from domain.topping.repository import ToppingRepository
from domain.topping.schema import ToppingBase


def test_create_topping(session, topping_repository):
    topping = topping_repository.create(ToppingBase(name="Киви"), session)

    session.commit()

    assert topping.id > 0
    assert topping.name == "Киви"


def test_update_topping(session, topping_repository):
    topping = topping_repository.create(ToppingBase(name="Киви"), session)

    session.commit()

    topping_repository.update(topping.id, ToppingBase(name="Ананас"), session)

    session.commit()

    assert topping.id > 0
    assert topping.name == "Ананас"


def test_delete_topping(session, topping_repository):
    topping = topping_repository.create(ToppingBase(name="Киви"), session)

    session.commit()

    topping_repository.delete(topping.id, session)

    session.commit()

    topping = topping_repository.get_by_id(topping.id, session)

    assert topping == None
