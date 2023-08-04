from numb3rs import validate

def test_max():
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("255.256.255.255") == False