from cache import LRUCache


def test_evicts_least_recently_used():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    assert cache.get(1) == 1


def test_update_refreshes_recency():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 9)
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(1) == 9


def test_missing_key_is_minus_one():
    cache = LRUCache(1)
    assert cache.get(1) == -1
