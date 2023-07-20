from jar import Jar
import pytest

def test_int():
    jar = Jar()

    assert jar.capacity == 12

def test_str():
    jar = Jar()

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()

    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()

    jar.deposit(7)

    jar.withdraw(5)

    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

