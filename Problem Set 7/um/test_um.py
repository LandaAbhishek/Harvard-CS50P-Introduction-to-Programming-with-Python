# importing libraries
import pytest
from um import count

# defining main function
def main():
    test_count()

# function to test count
def test_count():
    assert count("Um, thanks for the album.") == 1
    assert count("um") == 1
    assert count("Um, thanks, um, what about you") == 2
    assert count("Um?") == 1

# calling main function
if __name__ == "__main__":
    main()
