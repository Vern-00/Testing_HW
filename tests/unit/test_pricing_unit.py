import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

@pytest.mark.parametrize("text,expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.50),
    (" $0.99 ", 0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == pytest.approx(expected, rel=1e-9)

@pytest.mark.parametrize("text", ["", "abc", "$12,34,56"])
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)

@pytest.mark.parametrize("value,expected", [
    (0, "$0.00"),
    (1.234, "$1.23"),
    (1.235, "$1.24"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected

@pytest.mark.parametrize("price,percent,expected", [
    (100.0, 0, 100.0),
    (100.0, 10, 90.0),
    (50.0, 200, -50.0),  # if your function clamps/raises, adjust accordingly
])
def test_apply_discount_basic(price, percent, expected):
    # If negative/huge percentages should raise instead, replace with raises tests
    assert apply_discount(price, percent) == pytest.approx(expected, rel=1e-9)

@pytest.mark.parametrize("price,tax,expected", [
    (100.0, 0.1, 110.0),
    (100.0, 0.0, 100.0),
])
def test_add_tax_ok(price, tax, expected):
    assert add_tax(price, tax) == pytest.approx(expected, rel=1e-9)

@pytest.mark.parametrize("price,tax", [
    (100.0, -0.01),
    (100.0, -1.0),
])
def test_add_tax_negative_raises(price, tax):
    with pytest.raises(ValueError):
        add_tax(price, tax)

def test_bulk_total_simple_list():
    prices = [1.00, 2.50, 3.25]
    assert bulk_total(prices, discount_percent=0, tax_rate=0.0) == pytest.approx(6.75, rel=1e-9)
