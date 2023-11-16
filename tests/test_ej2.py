import pytest
from src.P2_3.Ej2 import pedirNum

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (1,1),
        (33,33),
        (100,99)
    ]
)
def test_pedirNum(input_num, expected):
    assert pedirNum(input_num) == expected

def test_pedirNum_ValueError():
    with pytest.raises(ValueError):
        pedirNum(-1)
        pedirNum(0)