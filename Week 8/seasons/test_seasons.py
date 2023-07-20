from seasons import minsCalculator
import pytest

def test_oneYear():
    assert minsCalculator("2022-07-12") == "Five hundred twenty-five thousand, six hundred minutes"

def test_twoYear():
    assert minsCalculator("2021-07-12") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid():
    with pytest.raises(SystemExit):
        minsCalculator("202207-12")
