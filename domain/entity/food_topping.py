from sqlalchemy import Table, Column, ForeignKey

from infrastructure.db import Base

food_topping = Table(
    "food_topping",
    Base.metadata,
    Column("food_id", ForeignKey("food.id"), primary_key=True),
    Column("topping_id", ForeignKey("topping.id"), primary_key=True),
)
