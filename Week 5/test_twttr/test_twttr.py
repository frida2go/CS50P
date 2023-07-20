from twttr import shorten

def test_one():
    assert shorten("David") == "Dvd"

def test_two():
    assert shorten("Twitter") == "Twttr"

def test_three():
    assert shorten("OK") == "K"

def test_four():
    assert shorten("1") == "1"

def test_five():
    assert shorten("twitter...") == "twttr..."

