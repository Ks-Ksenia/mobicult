from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.crud import get_db
from database.models import Base
from database.models import Rate
from handlers.constants import days
from main import app


@fixture(scope='session', autouse=True)
def get_test_engine():
    test_url = 'sqlite:///./test_sqlite.db'
    engine_test = create_engine(test_url)
    Base.metadata.create_all(engine_test)
    return engine_test


@fixture(scope='session', autouse=True)
def get_test_session(get_test_engine):
    return sessionmaker(get_test_engine, expire_on_commit=False)


@fixture(scope='session', autouse=True)
def create_test_data(get_test_session, get_test_engine):
    with get_test_session() as db:
        EUR, USD = 70, 72

        for v in days.values():
            db.add(Rate(date_rate=v, EUR=EUR, USD=USD))

            EUR += 10
            USD += 10

        db.commit()


@fixture(scope='session', autouse=True)
def get_test_app(get_test_session):
    def get_test_db():
        db = get_test_session()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = get_test_db
    yield app


@fixture(scope='session', autouse=True)
def client(get_test_app):
    with TestClient(get_test_app) as client:
        yield client
