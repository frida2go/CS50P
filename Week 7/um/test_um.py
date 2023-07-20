from um import count

def test_1():
    assert count("um") == 1

def test_2():
    assert count("This is, um... CS50.") == 1

def test_3():
    assert count("Um... what are regular expressions?") == 1

def test_4():
    assert count("Um, thanks, um, regular expressions make sense now.") == 2

def test_5():
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

