def test_create_person(test_client):
    response = test_client.post(
        "/api/person",
        json={"name": "test", "dob": "2024-01-01"},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
