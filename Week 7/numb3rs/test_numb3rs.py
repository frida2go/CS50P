from numb3rs import validate

def test_tooLargeIp():
    assert validate("257.257.257.257") == False

def test_onlyFirstIpValidated():
    assert validate("2.257.257.257") == False

def test_string():
    assert validate("cat") == False

def test_toofewIP():
    assert validate("256") == False

def test_CorrectIp():
    assert validate("25.25.25.1") == True