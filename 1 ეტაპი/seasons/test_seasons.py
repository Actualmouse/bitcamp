from seasons import check
import pytest

def test_right():
    assert check("2007-5-5") == "Eight million, five hundred thirty-seven thousand, seven hundred sixty minutes"
