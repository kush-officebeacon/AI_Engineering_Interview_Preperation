import threading

from cache import LRUCache


def test_concurrent_puts_stay_within_capacity_and_do_not_raise():
    cache = LRUCache(8)
    errors = []

    def writer(start):
        try:
            for key in range(start, start + 100):
                cache.put(key, key)
                cache.get(key)
        except Exception as exc:  # noqa: BLE001 - the test wants any thread failure
            errors.append(exc)

    threads = [threading.Thread(target=writer, args=(n * 100,)) for n in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert errors == []
    assert 0 < cache.size() <= 8
