# Solutions

One implementation that satisfies all four parts. Compare it with yours after you have tried. Yours can differ if the tests pass and you can explain the difference.

```python
import threading
import time
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int, time_fn=None):
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.capacity = capacity
        self.time_fn = time_fn or time.monotonic
        self._items: OrderedDict[int, tuple[int, float | None]] = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: int) -> int:
        with self._lock:
            self._drop_if_expired(key)
            if key not in self._items:
                return -1
            self._items.move_to_end(key)
            return self._items[key][0]

    def put(self, key: int, value: int, ttl: float | None = None) -> None:
        with self._lock:
            expiry = None if ttl is None else self.time_fn() + ttl
            if key in self._items:
                self._items.move_to_end(key)
                self._items[key] = (value, expiry)
            else:
                self._drop_expired()
                self._items[key] = (value, expiry)
            self._evict()

    def size(self) -> int:
        with self._lock:
            self._drop_expired()
            return len(self._items)

    def _drop_if_expired(self, key: int) -> None:
        item = self._items.get(key)
        if item is None:
            return
        _, expiry = item
        if expiry is not None and expiry <= self.time_fn():
            del self._items[key]

    def _drop_expired(self) -> None:
        now = self.time_fn()
        dead = [key for key, (_, expiry) in self._items.items() if expiry is not None and expiry <= now]
        for key in dead:
            del self._items[key]

    def _evict(self) -> None:
        while len(self._items) > self.capacity:
            self._items.popitem(last=False)
```

## Why this shape

- `OrderedDict` records recency. The front is the least recently used. `move_to_end` is the refresh. A dict plus a list also works. A dict alone does not, unless you rebuild order yourself.
- Expiry is stored next to the value. The clock is injected so tests move time without sleeping.
- `size()` and `put()` drop expired keys before they look at capacity. Otherwise an expired key still occupies the only slot and the part 3 test fails.
- The lock covers the whole read-modify-write. A lock only around `popitem` still lets two threads both decide the cache is under capacity.
- `-1` for a miss matches the tests. Do not raise `KeyError` unless you change the tests, which is out of bounds for the kata.

## What a shallow part-4 fix looks like

Catching `Exception` inside `put` makes the thread test's error list empty and hides corruption. The capacity assertion can still fail, or it can pass while `get` returns torn values. The lock is the fix. The `try` in the test is there to record failures, not to tell you to swallow them.
