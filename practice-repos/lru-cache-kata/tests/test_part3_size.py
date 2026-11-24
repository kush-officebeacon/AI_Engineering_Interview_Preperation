from cache import LRUCache


def test_size_ignores_expired_entries_and_frees_capacity():
    now = {"t": 0.0}
    cache = LRUCache(1, time_fn=lambda: now["t"])
    cache.put(1, 1, ttl=5)
    assert cache.size() == 1
    now["t"] = 5
    assert cache.size() == 0
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.size() == 1
