from pathlib import Path


def test_pagination_configuration_contract():
    source = Path(__file__).parents[1] / "src" / "pagination.py"
    content = source.read_text(encoding="utf-8")
    assert "page_size = 50" in content
    assert 'ordering = ("created_at", "id")' in content
