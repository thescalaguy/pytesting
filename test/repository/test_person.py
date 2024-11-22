import datetime

import pytest
from hypothesis import given, strategies as st, example

import repository.person as pr
from model.person import Person


MIN_DATE = datetime.date.today() - datetime.timedelta(days=Person.MAX_AGE * 365)
MAX_DATE = datetime.date.today()


@given(text=st.text(alphabet=["\x00"]))
def test_create_person_null_text(text, create_tables):
    with pytest.raises(AssertionError):
        pr.create(name=text, dob=MIN_DATE)


@given(
    text=st.text(min_size=1),
    dob=st.dates(min_value=datetime.date(2025, 1, 1)),
)
def test_create_person_future_dob(text, dob, create_tables):
    with pytest.raises(AssertionError):
        pr.create(name=text, dob=dob)


@given(
    text=st.text(min_size=1),
    dob=st.dates(max_value=MIN_DATE - datetime.timedelta(days=365)),
)
def test_create_person_past_dob(text, dob, create_tables):
    with pytest.raises(AssertionError):
        pr.create(name=text, dob=dob)


@given(
    text=st.text(min_size=5),
    dob=st.dates(
        min_value=MIN_DATE,
        max_value=MAX_DATE,
    ),
)
def test_create_person(text, dob, create_tables):
    person = pr.create(name=text, dob=dob)
    assert 0 <= person.age <= Person.MAX_AGE
