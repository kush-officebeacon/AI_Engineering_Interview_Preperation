from datetime import timedelta, timezone

from limiter import utc, within_window


def test_same_instant_in_another_zone_is_inside_a_short_window():
    event = utc(2026, 1, 1, 12, 0, 0)
    # 17:30:10 at UTC+05:30 is 12:00:10 UTC, ten seconds after the event.
    ist = timezone(timedelta(hours=5, minutes=30))
    now = event.astimezone(ist) + timedelta(seconds=10)
    assert within_window(event, now, 60) is True


def test_clock_faces_that_look_close_but_are_hours_apart_are_outside():
    event = utc(2026, 1, 1, 12, 0, 0)
    # 12:00:30 at UTC+05:30 is 06:30:30 UTC, not within 60 seconds of 12:00 UTC.
    ist = timezone(timedelta(hours=5, minutes=30))
    now = event.replace(tzinfo=ist)
    now = now + timedelta(seconds=30)
    assert within_window(event, now, 60) is False
