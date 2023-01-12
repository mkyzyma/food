import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///tests/test.db"

connect_args = {"check_same_thread": False} if DATABASE_URL.count("sqlite") > 0 else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=False,
)

# if not database_exists(engine.url):
#     create_database(engine.url)


# db_session = scoped_session(
#     sessionmaker(autocommit=False, autoflush=False, bind=engine)
# )

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()
Base.metadata.bind = engine


def create_db():
    Base.metadata.create_all(engine)


def recreate_db():
    Base.metadata.drop_all(engine)
    create_db()


def get_db():
    print(DATABASE_URL)

    db = Session()

    try:
        yield db
    finally:
        db.close()
