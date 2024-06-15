# importing jar function from jar
import pytest
from jar import Jar

# defining main function
def main():
    test__init()
    test_str()
    test_deposit()
    test_withdraw()

# function to test initialize
def test__init():
    jar = Jar(2)
    assert jar.capacity == 2

# function to test string
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

# function to test deposit
def test_deposit():
    jar = Jar(12)
    jar.deposit(8)
    assert jar.size == 8
    with pytest.raises(ValueError):
         jar.deposit(14)

# function to test withdraw
def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(10)

# calling main function
if __name__ == "__main__":
    main()
