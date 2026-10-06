from fastapi.testclient import TestClient


def test_get_activities_returns_available_activities(
    client: TestClient, activities: dict
) -> None:
    # Arrange
    expected_activities = activities

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_activities
