import threading

from limiter import SharedLimiter, utc


def test_two_threads_cannot_both_take_the_last_slot():
    """The seam parks both threads after the check and before the append.

    A correct limiter never lets both threads sit in that gap, because the
    check and the append are one critical section. This test then sees one
    success and one rejection without using the seam at all.
    """
    limiter = SharedLimiter(limit=1)
    now = utc(2026, 1, 1, 12, 0, 0)
    both_past_the_check = threading.Barrier(2)
    release = threading.Event()

    def hold():
        both_past_the_check.wait(timeout=2)
        release.wait(timeout=2)

    limiter.after_check = hold
    results = []

    def worker():
        results.append(limiter.allow("user", now))

    threads = [threading.Thread(target=worker) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=0.3)
    release.set()
    for thread in threads:
        thread.join(timeout=2)

    assert not any(thread.is_alive() for thread in threads)
    assert sorted(results) == [False, True]
