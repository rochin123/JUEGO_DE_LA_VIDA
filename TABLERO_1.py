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



# PARTE 1: TABLERO
def crear_tablero_vacio():
    return np.zeros((FILAS, COLUMNAS), dtype=int)


def crear_tablero_aleatorio():
    return (np.random.random((FILAS, COLUMNAS)) < 0.25).astype(int)
