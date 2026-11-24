"""Exercise tests. They describe the missing behaviour. They fail until you implement it.

Do not edit these tests to make them pass. If one is wrong, say why before you change it.
"""

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


def _seed(client):
    client.post("/tasks", json={"title": "A", "status": "open"})
    client.post("/tasks", json={"title": "B", "status": "done"})
    client.post("/tasks", json={"title": "C", "status": "open"})


def test_filter_by_status(client):
    _seed(client)
    response = client.get("/tasks", params={"status": "open"})
    assert response.status_code == 200
    body = response.json()
    # Contract for this exercise: a filter keeps the current bare-list response.
    assert [item["title"] for item in body] == ["A", "C"]


def test_pagination_shape_and_slice(client):
    _seed(client)
    response = client.get("/tasks", params={"offset": 1, "limit": 1})
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 3
    assert body["offset"] == 1
    assert body["limit"] == 1
    assert [item["title"] for item in body["items"]] == ["B"]


def test_limit_over_max_is_422(client):
    response = client.get("/tasks", params={"limit": 101})
    assert response.status_code == 422


def test_offset_past_end_is_empty_page(client):
    client.post("/tasks", json={"title": "A"})
    response = client.get("/tasks", params={"offset": 5, "limit": 20})
    assert response.status_code == 200
    body = response.json()
    assert body["items"] == []
    assert body["total"] == 1
