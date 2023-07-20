from bank import value

def test_one():
    assert value("Hello") == 0

def test_two():
    assert value("What's up") == 100

def test_three():
    assert value("hey") == 20

def test_four():
    assert value("What's up") == value("WHAT'S UP")
