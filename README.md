# Homework 5 – Testing

### Vern Toor | 017945044

## Q1:

- **Unit test:** Tests a single function or module in isolation to confirm correctness of small units.
- **Integration test:** Verifies that multiple parts of the system work together correctly (e.g., reading/writing files).
- **Regression test:** Ensures that a previously fixed bug does not reappear.

## Q2:

Pytest automatically discovers any file named `test_*.py` or `*_test.py`, and within them, any function named `test_*`.  
A _fixture_ provides reusable setup data or state for tests (e.g., `tmp_path` or custom fixtures defined in `conftest.py`).

## Pytest features used

- `@pytest.mark.parametrize` for parameterized tests.
- Built-in fixture `tmp_path` for temporary file creation.
- Custom fixtures for shared data.

## Coverage

See `COVERAGE.md` for the latest coverage summary and analysis.
