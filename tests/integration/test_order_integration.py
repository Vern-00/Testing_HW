import pytest
from src.order_io import load_order, write_receipt

def test_load_order_skips_blank_and_raises_on_malformed(tmp_path):
    p = tmp_path / "order.csv"
    p.write_text("widget,$10.00\n\nbadline-without-comma\n", encoding="utf-8")
    # First, confirm it fails on malformed line:
    with pytest.raises(ValueError):
        load_order(p)

def test_write_receipt_contents_exact(tmp_path):
    p_in = tmp_path / "order.csv"
    p_out = tmp_path / "receipt.txt"
    p_in.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    items = load_order(p_in)
    write_receipt(p_out, items, discount_percent=10, tax_rate=0.10)

    out = p_out.read_text(encoding="utf-8").splitlines()
    # Each line formatted with two decimals:
    assert "widget: $10.00" in out
    assert "gizmo: $5.50" in out
    # TOTAL line present and formatted:
    assert any(line.startswith("TOTAL: $") for line in out)
