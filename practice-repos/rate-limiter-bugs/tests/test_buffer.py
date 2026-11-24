from datetime import timedelta

from limiter import events_in_window, utc


def test_two_calls_do_not_share_a_buffer():
    start = utc(2026, 1, 1, 12, 0, 0)
    later = start + timedelta(seconds=1)
    first = events_in_window([start], start, 60)
    second = events_in_window([later], later, 60)
    assert first == [start]
    assert second == [later]
    assert first is not second
