from hypothesis import given, strategies as st
import repository.person as pr
from model.person import Person


@given(
    text=st.text(min_size=1),
    dob=st.dates(),
)
def test_create_person(text, dob, create_tables):
    person = pr.create(name=text, dob=dob)
    assert 0 <= person.age <= Person.MAX_AGE
