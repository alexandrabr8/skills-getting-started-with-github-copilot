"""Tests for DELETE /activities/{activity_name}/participants endpoint."""


def test_unregister_success_returns_200(client):
    # Arrange — use a participant already in the initial data
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 200


def test_unregister_success_returns_message(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert "message" in response.json()


def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    client.delete(f"/activities/{activity}/participants?email={email}")
    activities = client.get("/activities").json()

    # Assert
    assert email not in activities[activity]["participants"]


def test_unregister_participant_not_in_activity_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "ghost@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity = "Underwater Basket Weaving"
    email = "anyone@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
