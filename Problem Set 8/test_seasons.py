# importing convert function from seasons
import pytest
from seasons import convert

# defining main function
def main():
    test_date()

# function to test date
def test_date():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"

# calling main function
if __name__ == "__main__":
    main()
