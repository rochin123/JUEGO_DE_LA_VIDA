# =====================================================
# PARTE 3: INTERFAZ (Streamlit)
# =====================================================
# Dentro de INTERFAZ_3.py
import TABLERO_1
import REGLAS_2

# O bien, si importan funciones específicas:
# from TABLERO_1 import crear_tablero
# from REGLAS_2 import aplicar_reglas

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
