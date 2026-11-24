# Task tracker API

A small FastAPI service. Tasks live in a module-level list. `POST /tasks`, `GET /tasks`, and `GET /tasks/{id}` work. Blank titles are rejected.

`pytest tests/test_tasks.py` should pass before you change anything.

`pytest tests/test_exercise.py` should fail. That file is the specification for the feature you will add:

- `GET /tasks?status=open` returns a bare JSON list of only those tasks. Do this first, without changing the unfiltered body.
- Pagination is a second slice. `offset` and `limit` return `{"items", "offset", "limit", "total"}`. `limit` above 100 is 422. An offset past the end is 200 and an empty `items` list.
- The exercise file tests those behaviours. The order above matches [a controlled implementation](../../interview-preparation/training-roadmap.md). You may implement filter and pagination as separate changes. You will have to decide what `GET /tasks?status=open&limit=1` returns. Write that decision down before you code it. The exercise tests do not cover the combination.

There is no solution file in this repository. The point is the diff you can explain. A later level extends this service again. Keep the history if you use git.

## Run

```bash
python -m pip install -r requirements.txt
pytest tests/test_tasks.py
pytest tests/test_exercise.py
```

Created timestamps are deterministic: each new task is one second after the previous one, starting at 2026-01-01T00:00:00Z. Ids are `"1"`, `"2"`, and so on.
