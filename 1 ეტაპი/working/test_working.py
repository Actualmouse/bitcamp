from working import convert
import pytest

def test_min_out():
    with pytest.raises(ValueError):
        assert convert("2:10 AM to 4:60 PM")

def test_format():
    with pytest.raises(ValueError):
        assert convert("2:10 AM - 4:60 PM")

def test_hr_out():
    with pytest.raises(ValueError):
        assert convert("15:10 AM to 13:10 PM")

def test_correct():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
