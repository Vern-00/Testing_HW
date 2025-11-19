# COVERAGE.md

## Summary

- Command: `pytest --cov=src --cov-report=term-missing`
- Total coverage: **93%**
  - `src/order_io.py`: **90%** (missing lines 12, 15)
  - `src/pricing.py`: **95%** (missing line 20)

## Uncovered Lines

### src/order_io.py

```
12:                 continue
15:                 raise ValueError("Malformed line: " + ln.strip())
```

These branches correspond to error-handling paths for blank/malformed CSV lines. They did not execute in the current tests.

### src/pricing.py

```
20:         raise ValueError("percent must be >= 0")
```

This is the negative‑percent guard in `apply_discount`.

## Analysis

- The uncovered error branches in `order_io.py` are reasonable to leave partially uncovered if your application treats malformed input as exceptional. If desired, you can add a unit test that feeds a bad row to assert the `ValueError` branch and a test with an empty line to assert the `continue` branch.
- The uncovered negative‑percent guard in `apply_discount` can be covered by asserting that a negative percent raises `ValueError` (a unit test already exists for the negative‑percent case; once the regression bug is fixed, it will also drive coverage through this branch).

## Suggested Improvements

1. **Regression fix:** Update `apply_discount` to compute `price * (1 - percent/100.0)` and validate inputs; this will make the regression test pass and improve branch coverage.
2. **Order parsing edge cases:** Add tests that include an empty line and a malformed line in the CSV to exercise the error paths in `order_io.py`.
3. **Re‑run coverage:** After fixes, re‑run the command above and update this file with the new numbers.
