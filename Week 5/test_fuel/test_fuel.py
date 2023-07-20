from fuel import convert, gauge
import pytest

def test_convertInt():
    assert convert("1/2") == 50

def test_convertValueError():
    with pytest.raises(ValueError):
        convert ("3/2")

def test_convertZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert ("3/0")

def test_gaugeLabelE():
    assert gauge(1) == "E"

def test_gaugeLabelPercentage():
    assert gauge(50) == "50%"

def test_gaugeLabelF():
    assert gauge(99) == "F"