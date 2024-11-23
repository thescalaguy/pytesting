import pytest

from app import create_app
from model import db
from model.person import Person


@pytest.fixture(scope="session")
def create_tables():
    models = [Person]
    db.create_tables(models=models)


@pytest.fixture(scope="session")
def test_client(create_tables):
    app = create_app()
    context = app.app_context()
    context.push()
    client = app.test_client(use_cookies=True)
    return client
