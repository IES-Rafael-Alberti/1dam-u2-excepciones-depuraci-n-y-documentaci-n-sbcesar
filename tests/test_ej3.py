import pytest
from src.P2_3.Ej3 import cuentaRegresiva

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (1,0),
        (33,0),
        (100,0),
        (20,0)
    ]
)
def test_cuentaRegresiva(input_num, expected):
    assert cuentaRegresiva(input_num) == expected

def test_cuentaRegresiva_ValueError():
    with pytest.raises(ValueError):
        cuentaRegresiva(-1)
        cuentaRegresiva(0)