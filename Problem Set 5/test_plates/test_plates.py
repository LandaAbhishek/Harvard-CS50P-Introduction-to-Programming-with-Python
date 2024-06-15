from plates import is_valid

def main():
    test_firsttwoletters()
    test_len()
    test_number()
    test_punctuation()

def test_firsttwoletters():
    assert is_valid("AB") == True
    assert is_valid("42") == False
    assert is_valid("B3") == False
    assert is_valid("7") == False

def test_len():
    assert is_valid("ABDR47") == True
    assert is_valid("KD") == True
    assert is_valid("HELLOCS50") == False

def test_number():
    assert is_valid("AAA777") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA077") == False

def test_punctuation():
    assert is_valid("DB47!") == False

if __name__ == "__main__":
    main()
