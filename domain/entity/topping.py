from infrastructure.db import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


class Topping(Base):
    __tablename__ = "topping"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
