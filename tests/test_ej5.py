import pytest
from src.P2_3.Ej5 import validatePassword

@pytest.mark.parametrize(
    "input_password, expected",
    [
        ("usuario","Correct Password!")
    ]
)
def test_validatePassword(input_password, expected):
    assert validatePassword(input_password) == expected

def test_validatePassword_Exception():
    with pytest.raises(Exception):
        validatePassword("Usuario")