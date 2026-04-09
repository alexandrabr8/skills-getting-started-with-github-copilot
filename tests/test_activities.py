"""Tests for GET /activities endpoint."""


def test_get_activities_returns_200(client):
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_nine_activities(client):
    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert len(activities) == 9


def test_get_activities_each_has_required_keys(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for name, details in activities.items():
        missing = required_keys - details.keys()
        assert not missing, f"Activity '{name}' is missing keys: {missing}"


def test_get_activities_participants_is_list(client):
    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for name, details in activities.items():
        assert isinstance(details["participants"], list), (
            f"Activity '{name}' participants should be a list"
        )


def test_get_activities_max_participants_is_positive_int(client):
    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for name, details in activities.items():
        assert isinstance(details["max_participants"], int), (
            f"Activity '{name}' max_participants should be an int"
        )
        assert details["max_participants"] > 0, (
            f"Activity '{name}' max_participants should be positive"
        )
