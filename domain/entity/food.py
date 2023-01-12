from infrastructure.db import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from .food_topping import food_topping


class Food(Base):
    __tablename__ = "food"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(String)

    price = Column(Integer)

    is_special = Column(Boolean)
    is_vegan = Column(Boolean)

    is_publish = Column(Boolean)

    id_category = Column(Integer, ForeignKey("food_category.id"))
    category = relationship("FoodCategory", back_populates="foods")

    toppings = relationship("Topping", secondary=food_topping)
