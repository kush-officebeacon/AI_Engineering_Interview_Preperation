# Practice repositories

Small Python projects for the [training roadmap](../interview-preparation/training-roadmap.md). Each one has a `SOLUTIONS.md`. Do the work before you open it.

| Directory | Level | What is wrong on purpose |
| --- | --- | --- |
| [task-tracker-api](task-tracker-api/) | 3 and 5 | The list endpoint has no filter and no pagination. Existing tests pass. The exercise tests fail. |
| [rate-limiter-bugs](rate-limiter-bugs/) | 4 | Four bugs. The suite fails. A shallow patch can turn one test green and leave the defect. |
| [lru-cache-kata](lru-cache-kata/) | 6 | Stubs only. Four parts, in order: LRU, TTL, expired size, thread safety. |

Run a repository from its own directory so imports resolve:

```bash
cd practice-repos/task-tracker-api
python -m pip install -r requirements.txt
pytest
```

The limiter and the cache need only pytest.

Open-source repositories for Level 2 are not vendored here. The roadmap names them and tells you what to trace. Clone them yourself when you start that level.
