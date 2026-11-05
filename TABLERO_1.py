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
