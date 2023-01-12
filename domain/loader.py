from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select


class Loader(ABC):
    @abstractmethod
    def get_statement(self, filter=None):
        ...

    def load(self, session: Session, filter=None):
        statement = self.get_statement(filter)
        statement = self.apply_page_filter(statement, filter)
        return session.execute(statement).scalars().unique().all()

    def apply_page_filter(self, statement: Select, filter=None):
        if not filter or not hasattr(filter, "limit") or filter.limit == 0:
            return statement

        return statement.offset(filter.skip).unique().limit(filter.limit)
