from hypothesis import given, strategies as st
import datetime

from model.person import Person

MIN_DATE = datetime.date.today() - datetime.timedelta(days=Person.MAX_AGE * 365)
MAX_DATE = datetime.date.today()


@given(
    json=st.fixed_dictionaries(
        {
            "name": st.text(min_size=5),
            "dob": st.dates(min_value=MIN_DATE, max_value=MAX_DATE),
        }
    )
)
def test_create_person(json, test_client):
    response = test_client.post(
        "/api/person",
        json=json,
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 200
