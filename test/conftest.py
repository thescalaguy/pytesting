import pytest

from model import db
from model.person import Person


@pytest.fixture(scope="session")
def create_tables():
    models = [Person]

    db.create_tables(models=models)
