"""LRU cache kata. Methods raise until you implement them. See README for the four parts."""

import time


class LRUCache:
    def __init__(self, capacity: int, time_fn=None):
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.capacity = capacity
        self.time_fn = time_fn or time.monotonic

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int, ttl: float | None = None) -> None:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError
