from src.pricing import apply_discount

def test_apply_discount_regression_correct_percent_math():
    # Expected: 10% off 100 -> 90.0
    assert apply_discount(100.0, 10) == 90.0
