from bank import value

def test_hello():
    assert value("Hello, there") == 0

def test_h():
    assert value("Hey, there") == 20

def test_none():
    assert value("What's up?") == 100