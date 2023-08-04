from fuel import convert, gauge
import pytest

def test_conv():
    assert convert('3/4') == 75
    assert convert('1/100') == 1
    with pytest.raises(ValueError):
        convert("x/z")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"