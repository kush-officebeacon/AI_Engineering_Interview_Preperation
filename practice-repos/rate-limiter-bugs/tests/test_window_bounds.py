from datetime import timedelta

from limiter import allow, utc


def test_fifth_call_is_allowed():
    store = {}
    start = utc(2026, 1, 1, 12, 0, 0)
    results = [allow("user", start + timedelta(seconds=i), store, limit=5) for i in range(5)]
    assert results == [True, True, True, True, True]


def test_sixth_call_inside_the_window_is_rejected():
    store = {}
    start = utc(2026, 1, 1, 12, 0, 0)
    for i in range(5):
        assert allow("user", start + timedelta(seconds=i), store, limit=5) is True
    assert allow("user", start + timedelta(seconds=5), store, limit=5) is False


def test_call_after_the_window_slides_is_allowed():
    store = {}
    start = utc(2026, 1, 1, 12, 0, 0)
    for i in range(5):
        allow("user", start + timedelta(seconds=i), store, limit=5)
    later = start + timedelta(seconds=61)
    assert allow("user", later, store, limit=5, window_seconds=60) is True
