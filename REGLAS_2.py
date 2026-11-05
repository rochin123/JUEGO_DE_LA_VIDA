# PARTE 2: Reglas 
def contar_vecinos(tablero):
    """
    Devuelve una matriz del mismo tamaño donde cada número es
    la cantidad de vecinas vivas de esa celda.

    Truco: se rodea el tablero con un borde de ceros y se suman
    las 8 versiones desplazadas del tablero.
    """
    p = np.pad(tablero, 1)  # borde de ceros
    vecinos = (
        p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:]    # fila de arriba
        + p[1:-1, :-2] + p[1:-1, 2:]               # izquierda y derecha
        + p[2:, :-2] + p[2:, 1:-1] + p[2:, 2:]     # fila de abajo
    )
    return vecinos


def siguiente_generacion(tablero):
    vecinos = contar_vecinos(tablero)

    sobrevive = (tablero == 1) & ((vecinos == 2) | (vecinos == 3))
    nace = (tablero == 0) & (vecinos == 3)

    return (sobrevive | nace).astype(int)
