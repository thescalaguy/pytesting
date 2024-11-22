import datetime

from model.person import Person
from util.string import sanitize


def create(name: str, dob: datetime.date) -> Person:
    """
    Create a new person instance with the given name and date of birth.
    :param name: Name of the person.
    :param dob: Date of birth of the person.
    :return: A Person instance.
    """
    name = sanitize(name)

    assert name, f"name cannot by empty"
    assert 0 <= (datetime.date.today().year - dob.year) <= Person.MAX_AGE

    return Person.create(name=name, dob=dob)
