from src.order_io import load_order, write_receipt
from src.pricing import bulk_total

def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    items = load_order(input_file)
    total = bulk_total([p for _, p in items], discount_percent=10, tax_rate=0.1)

    output_path = tmp_path / "receipt.txt"
    write_receipt(output_path, items, discount_percent=10, tax_rate=0.1)

    output_text = output_path.read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "TOTAL:" in output_text
    # Optionally assert numeric total formatting appears
    assert f"{total:.2f}" in output_text
