# importing packages
from numb3rs import validate

# Function to test Valid
def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("11.88.22.99") == True
    assert validate("256.255.255.255") == False
    assert validate("199.911.288.882") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("rat") == False

