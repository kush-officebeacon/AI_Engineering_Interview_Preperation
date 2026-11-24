from cache import LRUCache


def test_expired_key_reads_as_missing_and_can_be_replaced():
    now = {"t": 0.0}

    def clock():
        return now["t"]

    cache = LRUCache(1, time_fn=clock)
    cache.put(1, 1, ttl=5)
    assert cache.get(1) == 1
    now["t"] = 5
    assert cache.get(1) == -1
    cache.put(2, 2)
    assert cache.get(2) == 2


def test_ttl_none_does_not_expire():
    now = {"t": 0.0}
    cache = LRUCache(1, time_fn=lambda: now["t"])
    cache.put(1, 1, ttl=None)
    now["t"] = 10_000
    assert cache.get(1) == 1
