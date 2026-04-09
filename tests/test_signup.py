"""Tests for POST /activities/{activity_name}/signup endpoint."""


def test_signup_success_returns_200(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200


def test_signup_success_returns_message(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert "message" in response.json()


def test_signup_adds_participant_to_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    client.post(f"/activities/{activity}/signup?email={email}")
    activities = client.get("/activities").json()

    # Assert
    assert email in activities[activity]["participants"]


def test_signup_duplicate_email_returns_400(client):
    # Arrange — use a participant already in the initial data
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    activity = "Underwater Basket Weaving"
    email = "anyone@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
