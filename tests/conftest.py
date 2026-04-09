import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app


@pytest.fixture()
def client():
    """Provide a TestClient and restore the in-memory activities state after each test."""
    # Arrange — snapshot original state
    original = copy.deepcopy(app_module.activities)

    with TestClient(app) as c:
        yield c

    # Teardown — restore state so tests are fully isolated
    app_module.activities.clear()
    app_module.activities.update(original)
