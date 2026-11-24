"""Rate limiter with four deliberate defects. Read the tests, not this paragraph, for the contract."""

from datetime import datetime, timedelta, timezone
from threading import Lock


def allow(key, now, store, limit=5, window_seconds=60):
    """Return True if this call is within the limit for key.

    `now` must be timezone-aware UTC. `store` is a dict of key -> list of datetimes,
    owned by the caller.
    """
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    bucket = store.setdefault(key, [])
    cutoff = now - timedelta(seconds=window_seconds)
    bucket[:] = [stamp for stamp in bucket if stamp > cutoff]
    # Defect: the new call is counted only after this comparison, and the
    # comparison is strict greater-than. The tests say what should happen.
    if len(bucket) > limit:
        return False
    bucket.append(now)
    return True


def events_in_window(events, now, window_seconds, found=[]):
    """Return the events inside the window ending at `now`."""
    for event in events:
        delta = (now - event).total_seconds()
        if 0 <= delta < window_seconds:
            found.append(event)
    return found


def within_window(event_time, now, window_seconds):
    """True if event_time is inside [now - window, now). Both arguments may carry tzinfo."""

    def clock_face(value: datetime) -> datetime:
        if value.tzinfo is not None:
            return value.replace(tzinfo=None)
        return value

    delta = (clock_face(now) - clock_face(event_time)).total_seconds()
    return 0 <= delta < window_seconds


class SharedLimiter:
    """Process-local limiter. `after_check` is a test seam, not a feature.

    The seam runs after the limit is read and before the event is stored.
    Deleting the seam is not a fix. Tests hang a second thread off it on purpose.
    """

    def __init__(self, limit=5):
        self.limit = limit
        self._events: dict[str, list] = {}
        self._lock = Lock()
        self.after_check = None

    def allow(self, key, now):
        with self._lock:
            bucket = self._events.setdefault(key, [])
            permitted = len(bucket) < self.limit
        if self.after_check is not None:
            self.after_check()
        if permitted:
            bucket.append(now)
        return permitted


def utc(year, month, day, hour=0, minute=0, second=0) -> datetime:
    return datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
