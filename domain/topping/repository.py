from domain.entity.topping import Topping
from domain.repository import Repository
from sqlalchemy import select


class ToppingRepository(Repository[Topping]):
    def __init__(self):
        super().__init__(Topping)

    def get_statement(self, filter=None):
        return select(Topping)
