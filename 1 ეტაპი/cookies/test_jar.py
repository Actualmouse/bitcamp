from jar import Jar

jar = Jar()

def test_init():
    jar = Jar(12)
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert str(jar) == "🍪"