from infrastructure.db import Base
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship


class FoodCategory(Base):
    __tablename__ = "food_category"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_publish = Column(Boolean)

    foods = relationship("Food", back_populates="category")
