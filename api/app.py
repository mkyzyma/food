from fastapi import FastAPI

from infrastructure.db import create_db, recreate_db

from .router import init_routes


def create_app():
    create_db()
    # recreate_db()

    app = FastAPI(title="Food", description="Super Mega food manager")

    init_routes(app)

    return app


app = create_app()
