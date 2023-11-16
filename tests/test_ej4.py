import pytest
from src.P2_3.Ej4 import convierteAEntero

@pytest.mark.parametrize(
    "input_entrada, expected",
    [
        (1,1),
        (33,33),
        (100,100),
        (20,20)
    ]
)
def test_convierteAEntero(input_entrada, expected):
    assert convierteAEntero(input_entrada) == expected

def test_convierteAEntero_Exception():
    with pytest.raises(Exception):
        convierteAEntero(2.2)
        convierteAEntero("hola")