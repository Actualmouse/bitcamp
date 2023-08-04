from plates import is_valid

def test_all_letters():
    assert is_valid('regex') == True

def test_all_numbers():
    assert is_valid('123456') == False

def test_last_nums():
    assert is_valid('CS50') == True

def test_last_nums_zero():
    assert is_valid('CS05') == False

def test_min_length():
    assert is_valid('C') == False

def test_max_length():
    assert is_valid('CCCCCCC') == False

def test_mid_num():
    assert is_valid('CC50CC') == False

def test_lower_higher():
    assert is_valid('AwO,') == False
    assert is_valid('AAA') == True
    assert is_valid('aaa') == True