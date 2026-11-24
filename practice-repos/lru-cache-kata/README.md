# LRU cache kata

A timed practice round modelled on the multi-part cache task candidates have **reported** at LinkedIn in 2026. Those reports are not a LinkedIn policy. See [the research](../../research/company-assessment-research.md). The shape is still worth practising: one core structure, then a harder constraint, then another, then threads. You narrate while you work.

`cache.py` is a stub. Every part raises `NotImplementedError` until you write it.

| Part | Tests | Behaviour |
| --- | --- | --- |
| 1 | `tests/test_part1_lru.py` | Capacity-n LRU. `get` returns the value or `-1`. `get` and `put` of an existing key refresh recency. |
| 2 | `tests/test_part2_ttl.py` | `put(..., ttl=seconds)` expires at `time_fn() + ttl`. `ttl=None` does not expire. Inject the clock. Do not `sleep`. |
| 3 | `tests/test_part3_size.py` | `size()` does not count expired keys, and an expired key does not occupy capacity. |
| 4 | `tests/test_part4_threads.py` | Concurrent `get` and `put` do not raise, and `size()` stays within capacity. |

Do the parts in order. A later part that breaks an earlier test is not done.

Suggested limit: 45 minutes for as many parts as you can explain. Stopping at part 2 with a clear reason beats a green part 4 you cannot read.

The reference implementation is in [SOLUTIONS.md](SOLUTIONS.md). Open it after a real attempt.

```bash
python -m pytest tests/test_part1_lru.py
python -m pytest
```

Part 4 can pass by accident on a single-threaded stub that never ran, and it fails immediately on `NotImplementedError`. A lock is the point of the part. A green part 4 with no lock, run once, is weak evidence. Say that out loud.
