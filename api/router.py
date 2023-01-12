from fastapi import FastAPI
from .toppings.controller import router as toppings_router
from .food_categories.controller import router as food_categories_router
from .foods.controller import router as foods_router


def init_routes(app: FastAPI):
    app.include_router(toppings_router, prefix="/toppings")
    app.include_router(food_categories_router, prefix="/food-categories")
    app.include_router(foods_router, prefix="/foods")
