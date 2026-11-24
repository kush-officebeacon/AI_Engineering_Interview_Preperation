import pytest
from fastapi.testclient import TestClient

from app import TASKS, app


@pytest.fixture(autouse=True)
def clean_store():
    TASKS.clear()
    yield
    TASKS.clear()


@pytest.fixture
def client():
    return TestClient(app)


def test_create_and_get(client):
    created = client.post("/tasks", json={"title": "Write tests", "status": "open"})
    assert created.status_code == 201
    body = created.json()
    assert body["title"] == "Write tests"
    assert body["status"] == "open"
    assert body["id"] == "1"

    fetched = client.get("/tasks/1")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Write tests"


def test_blank_title_is_rejected(client):
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 422


def test_missing_task_is_404(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_list_returns_every_task_in_creation_order(client):
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    response = client.get("/tasks")
    assert response.status_code == 200
    titles = [item["title"] for item in response.json()]
    assert titles == ["A", "B"]
