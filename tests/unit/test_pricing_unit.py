import re

def parse_price(text):
    """
    Parse a price like "$1,234.50", "12.5", or " $0.99 ".
    Valid rules:
      - Optional leading "$" and whitespace
      - Either plain digits or properly grouped thousands with commas (e.g., 1,234,567)
      - Optional decimal point with 1–2 digits
    Invalid examples: "1,23", "$,123", "12,34", "$123.", "12.345"
    """
    s = str(text).strip()
    if not s:
        raise ValueError("empty price")

    # Strict validation for proper thousands and decimal format
    pattern = r'^\$?\s*(?:([0-9]{1,3}(?:,[0-9]{3})+)|([0-9]+))(?:\.[0-9]{1,2})?$'
    if not re.match(pattern, s):
        raise ValueError(f"invalid price format: {s!r}")

    # Remove symbols and commas safely
    s = s.replace("$", "").replace(",", "").strip()
    return float(s)


def format_currency(value):
    """Format a number as currency with a dollar sign and two decimals."""
    return "$" + f"{float(value):0.2f}"


def apply_discount(price, percent):
    """
    Apply a percentage discount (e.g., 10 for 10%).
    Negative percentages raise ValueError.
    """
    price = float(price)
    percent = float(percent)
    if percent < 0:
        raise ValueError("percent must be >= 0")
    return price * (1 - percent / 100.0)


def add_tax(price, rate=0.07):
    """Add a tax rate (default 7%). Negative rates raise ValueError."""
    if rate < 0:
        raise ValueError("rate must be >= 0")
    return price * (1 + rate)


def bulk_total(prices, discount_percent=0, tax_rate=0.07):
    """
    Compute total for a list of prices, applying discount then tax.
    """
    subtotal = sum(float(p) for p in prices)
    after_discount = apply_discount(subtotal, discount_percent)
    return add_tax(after_discount, tax_rate)
