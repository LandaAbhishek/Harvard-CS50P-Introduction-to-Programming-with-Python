import pytest
from fuel import convert, gauge

def main():
    test_con()
    test_gau()
    test_value_err()
    test_zero_div()

def test_con():
    assert convert("5/10") == 50
    assert convert("90/100") == 90
    assert convert("1/100") == 1

def test_gau():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_value_err():
    with pytest.raises(ValueError):
        convert("2/1")

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__ == "__main__":
    main()
