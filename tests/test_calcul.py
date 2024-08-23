import pytest
from calcul import add

def test_add():
    assert add(2, 3) == 5  # Vérifie que 2 + 3 donne bien 5
    assert add(-1, 1) == 0  # Vérifie que -1 + 1 donne bien 0
    assert add(0, 0) == 0   # Vérifie que 0 + 0 donne bien 0

@pytest.mark.parametrize("a,b,resultat_attendu", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add2(a, b, resultat_attendu):
    assert add(a, b) == resultat_attendu
