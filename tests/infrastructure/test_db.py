from domain import entity
from infrastructure.db import get_db


def test_session():
    session = next(get_db())
    assert session.is_active
