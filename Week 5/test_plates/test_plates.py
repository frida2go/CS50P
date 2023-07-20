from plates import is_valid



def test_zero_placement():
    assert not is_valid("CS05")

def test_length():
    assert not is_valid("C")

def test_number():
    assert not is_valid("CS50C")

def test_alphanumeric():
    assert not is_valid("PI3.14")

def test_alphabetical():
    assert not is_valid("123444")
