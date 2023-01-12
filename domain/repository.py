from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from .loader import Loader

ENTITY = TypeVar("ENTITY")


class Repository(Loader, Generic[ENTITY]):
    def __init__(self, entity_factory):
        self._entity_factory = entity_factory

    def get_by_id(self, id: int, session: Session) -> ENTITY:
        return session.get(self._entity_factory, id)

    def create(self, new: BaseModel, session: Session) -> ENTITY:
        entity = self._entity_factory(**new.dict())
        session.add(entity)
        return entity

    def update(self, id: int, updates: BaseModel, session: Session) -> ENTITY:
        entity = self.get_by_id(id, session)
        self.change(entity, updates)
        return entity

    def delete(self, id: int, session: Session):
        entity = self.get_by_id(id, session)

        if not entity:
            return

        session.delete(entity)

    def change(self, entity: ENTITY, updates: BaseModel) -> ENTITY:
        for key, val in updates.dict().items():
            if val:
                setattr(entity, key, val)
        return entity
