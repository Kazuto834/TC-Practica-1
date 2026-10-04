import pytest

from lenguajes import (
    prefijos,
    sufijos,
    subcadenas,
    cerradura_Kleene,
    cerradura_positiva,
)


# 1. Pruebas con cadena vacía
def test_cadena_vacia():
    assert prefijos("") == [""]
    assert sufijos("") == [""]
    assert subcadenas("") == [""]


# 2. Pruebas con cadena de longitud 1
def test_cadena_longitud_uno():
    assert set(prefijos("a")) == {"", "a"}
    assert set(sufijos("a")) == {"", "a"}
    assert set(subcadenas("a")) == {"", "a"}


# 3. Diferencia entre cerradura de Kleene y positiva para longitud cero
def test_diferencia_kleene_y_positiva_longitud_cero():
    alfabeto = {"a", "b"}

    res_kleene = cerradura_Kleene(alfabeto, maxlength=0)
    res_positiva = cerradura_positiva(alfabeto, maxlength=0)

    # La cadena vacía se representa como "" (no como un espacio).
    assert res_kleene == [""]
    assert res_positiva == []
    assert res_kleene != res_positiva


# 4. Pruebas con alfabeto de un solo símbolo
def test_alfabeto_un_simbolo():
    alfabeto = {"a"}

    res_kleene = cerradura_Kleene(alfabeto, maxlength=6)
    assert set(res_kleene) == {
        "", "a", "a a", "a a a", "a a a a",
        "a a a a a", "a a a a a a"
    }

    res_positiva = cerradura_positiva(alfabeto, maxlength=6)
    assert set(res_positiva) == {
        "a", "a a", "a a a", "a a a a",
        "a a a a a", "a a a a a a"
    }
