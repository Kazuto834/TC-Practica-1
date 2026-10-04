import itertools


def prefijos(cadena):
    return [cadena[:i] for i in range(len(cadena) + 1)]

def sufijos(cadena):
    return [cadena[i:] for i in range(len(cadena) + 1)]

def subcadenas(cadena):
    subcadenas = set()
    subcadenas.add("") #por la cadena vacía

    for i in range(len(cadena)):
        for j in range(i + 1, len(cadena) + 1):
            subcadenas.add(cadena[i:j])

    return list(subcadenas)

def cerradura_Kleene(alfabeto, maxlength):
    resultado = []

    for long in range(maxlength + 1):
        combinaciones = itertools.product(alfabeto, repeat=long)
        for comb in combinaciones:
            resultado.append(" ".join(comb))
    return resultado

def cerradura_positiva(alfabeto, maxlength):
    resultado = []

    for long in range(1, maxlength + 1):
        combinaciones = itertools.product(alfabeto, repeat=long)
        for comb in combinaciones:
            resultado.append(" ".join(comb))
    return resultado