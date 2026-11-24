# Solutions

Open this after you have tried. Each section says the cause, the shallow patch that is not enough, and the real fix.

## Window bound

`allow` rejects only when `len(bucket) > limit`. The new timestamp is appended after that check. With `limit` 5 and five stamps already stored, `5 > 5` is false, so the sixth stamp is stored and the call returns `True`.

Lowering the default `limit` to 4 makes the sixth call fail and makes the fifth call fail too. That is not the requirement.

Fix: reject when `len(bucket) >= limit` **before** appending. Keep `limit` at 5. The slide test should still pass because stamps older than the window are dropped first. The cutoff comparison is `stamp > cutoff`, which drops a stamp exactly `window_seconds` old. The tests do not lock the exact-edge stamp. If you change that comparison, say so.

## Shared buffer

`events_in_window` uses a mutable default list, `found=[]`. That list is created once and reused. The second call appends to the same list the first call returned, so the first result grows and `first is second`.

Calling `found.clear()` at the top makes the two results equal to the right events only until a caller keeps the list. The next call clears the list the caller still holds. `assert first is not second` still fails if you return the same list.

Fix: `found = []` inside the function. Do not use a default value for it. Delete the parameter.

## Time zones

`within_window` strips `tzinfo` and subtracts the clock faces. 12:00 UTC and 17:30 IST are the same moment plus ten seconds in the first test, and the function treats them as five hours apart. 12:00 UTC and 12:00:30 at UTC+05:30 look thirty seconds apart and are about five and a half hours apart.

Fix: convert both values to UTC before subtracting.

```python
def _as_utc(value):
    if value.tzinfo is None:
        raise ValueError("timezone-aware datetimes required")
    return value.astimezone(timezone.utc)
```

Then compare `_as_utc(now) - _as_utc(event_time)`. Do not `replace(tzinfo=timezone.utc)` on a value that already has a different zone. That labels the clock face as UTC without shifting it, which is the same bug in a new costume.

## Last slot

`SharedLimiter.allow` reads the length under the lock, releases the lock, runs `after_check`, then appends. Both threads can observe an empty bucket. The seam exists so the test can park both threads in that gap. If you delete `after_check` and leave the append outside the lock, the defect stays and this test no longer demonstrates it.

Fix: hold the lock from the read through the append. Decide under the lock. Do not call `after_check` while holding the lock if the hook waits for the other thread: that deadlocks. Run the hook only in the unlocked gap if you keep the seam for the buggy version. The fixed version has no gap, so the hook cannot observe two threads both inside it. One thread gets `True`. The other waits on the lock, observes the new length, and gets `False`.

A lock that covers only the append, after both threads have already decided `permitted = True`, still stores two events.

## Check

From this directory, `python -m pytest` is green after all four fixes, and red before them. `tests/test_window_bounds.py::test_fifth_call_is_allowed` is green even on the buggy code. A green file is not a green function. Run the whole suite.
