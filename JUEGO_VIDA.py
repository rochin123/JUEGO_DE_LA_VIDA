"""
Juego de la Vida - versión sencilla con numpy
Ejecutar:  streamlit run juego_simple_numpy.py
"""

import time

import numpy as np
import streamlit as st

FILAS = 40
COLUMNAS = 60
TAM_CELDA = 12  # píxeles por celda al dibujar


# =====================================================
# PARTE 1: TABLERO
# Matriz de numpy: 0 = célula muerta, 1 = célula viva.
# =====================================================
def crear_tablero_vacio():
    return np.zeros((FILAS, COLUMNAS), dtype=int)


def crear_tablero_aleatorio():
    # números al azar entre 0 y 1; si son menores a 0.25 la celda vive
    return (np.random.random((FILAS, COLUMNAS)) < 0.25).astype(int)


# =====================================================
# PARTE 2: REGLAS
# =====================================================
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


# =====================================================
# PARTE 3: INTERFAZ (Streamlit)
# =====================================================
def tablero_a_imagen(tablero):
    """Convierte la matriz en una imagen: vivas verdes, muertas oscuras."""
    imagen = np.zeros((FILAS, COLUMNAS, 3), dtype=np.uint8)
    imagen[:, :] = (25, 25, 35)         # color de fondo (muertas)
    imagen[tablero == 1] = (80, 250, 120)  # color de las vivas
    # agranda cada celda a TAM_CELDA x TAM_CELDA píxeles
    imagen = np.repeat(np.repeat(imagen, TAM_CELDA, axis=0), TAM_CELDA, axis=1)
    return imagen


st.title("Juego de la Vida")

# Streamlit reinicia el script en cada clic, así que guardamos
# el tablero en session_state para que no se pierda.
if "tablero" not in st.session_state:
    st.session_state.tablero = crear_tablero_aleatorio()
    st.session_state.generacion = 0
    st.session_state.corriendo = False

col1, col2, col3, col4 = st.columns(4)

if col1.button("Iniciar / Pausar"):
    st.session_state.corriendo = not st.session_state.corriendo

if col2.button("Un paso"):
    st.session_state.tablero = siguiente_generacion(st.session_state.tablero)
    st.session_state.generacion += 1

if col3.button("Aleatorio"):
    st.session_state.tablero = crear_tablero_aleatorio()
    st.session_state.generacion = 0

if col4.button("Limpiar"):
    st.session_state.tablero = crear_tablero_vacio()
    st.session_state.generacion = 0

st.write(f"Generación: {st.session_state.generacion}")
st.image(tablero_a_imagen(st.session_state.tablero))

# Si está corriendo: avanza una generación y vuelve a dibujar
if st.session_state.corriendo:
    time.sleep(0.1)
    st.session_state.tablero = siguiente_generacion(st.session_state.tablero)
    st.session_state.generacion += 1
    st.rerun()
    