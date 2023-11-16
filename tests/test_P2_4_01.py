import pytest
from src.P2_4.Ej1 import ordenarLista

@pytest.mark.parametrize(
    "input_lista, expected",
    [
        ([],[]),
        ([20,11,-12,76,33],[-12,11,20,33,76])
    ]
)

def test_ordenarLista(input_lista, expected):
    assert ordenarLista(input_lista) == expected