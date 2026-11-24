"""In-memory task API. List returns every task. Filtering and pagination are not implemented."""

from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
TASKS: list[dict] = []


class TaskIn(BaseModel):
    title: str
    status: str = Field(default="open")


def _reset() -> None:
    TASKS.clear()


def _create(title: str, status: str) -> dict:
    if not title.strip():
        raise HTTPException(status_code=422, detail="title is required")
    created_at = datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=len(TASKS))
    task = {
        "id": str(len(TASKS) + 1),
        "title": title,
        "status": status,
        "created_at": created_at.isoformat(),
    }
    TASKS.append(task)
    return task


@app.post("/tasks", status_code=201)
def create_task(body: TaskIn) -> dict:
    return _create(body.title, body.status)


@app.get("/tasks")
def list_tasks() -> list[dict]:
    return list(TASKS)


@app.get("/tasks/{task_id}")
def get_task(task_id: str) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="not found")
