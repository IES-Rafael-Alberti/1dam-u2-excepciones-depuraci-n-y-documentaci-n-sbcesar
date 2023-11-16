import pytest
from src.P2_3.Ej1 import imprimirEdad

@pytest.mark.parametrize(
    "input_edad, expected",
    [
        (20,20),
        (100,100),
        (23,23),
        (33,33)
    ]
)
def test_introducir_edad(input_edad, expected):
    assert imprimirEdad(input_edad) == expected

def test_introducir_edad_ValueError():
    with pytest.raises(ValueError):
        imprimirEdad(-1)