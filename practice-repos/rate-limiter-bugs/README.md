# Rate limiter bugs

Four defects, four test modules. `pytest` fails. Your job is a cause for each failure, then the smallest fix, then a re-run.

| Test module | Contract the tests lock |
| --- | --- |
| `tests/test_window_bounds.py` | 5 calls in the window are allowed. The 6th is not. A call after the window moves is allowed. |
| `tests/test_buffer.py` | Two window queries do not share storage. |
| `tests/test_timezones.py` | Instants compare in real time, not by the numbers on the clock face. |
| `tests/test_concurrency.py` | Two threads cannot both take the last slot. `after_check` exists so the test can force the interleaving. Removing the seam without changing the lock scope is not a fix, and a correct lock scope must not deadlock this test. |

A change that makes one assertion pass by editing the test, or by lowering `limit` from 5 to 4, has missed the defect. The sixth-call test and the fifth-call test are a pair. Read both before you patch.

Do not open [SOLUTIONS.md](SOLUTIONS.md) until you have a green run you can explain, or until you are stuck after a real attempt.

```bash
python -m pytest
```

Requires pytest. No third-party packages.
