from plates import is_valid

def test_all_letters():
    assert is_valid('regex') == True

def test_all_numbers():
    assert is_valid('123456') == False

def test_last_nums():
    assert is_valid('CS50') == True

def test_last_nums_zero():
    assert is_valid('CS05') == False