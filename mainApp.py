import streamlit as st
import pandas as pd
import random

# Configuración de la página
st.set_page_config(page_title="Juego de Preguntas", page_icon="🔥", layout="wide")

# Inicialización del juego
def inicializacion_juego():
    """Inicializar las variables de sesión"""
    if 'jugadores' not in st.session_state:
        st.session_state.jugadores = []
    if 'jugadores_actuales' not in st.session_state:
        st.session_state.jugadores_actuales = 0  # Para el control de turnos
    if 'juego_activo' not in st.session_state:
        st.session_state.juego_activo = False
    if 'preguntas_y_retos' not in st.session_state:
        st.session_state.preguntas_y_retos = []
    if 'categoria' not in st.session_state:
        st.session_state.categoria = None
    if 'jugador_actual' not in st.session_state:
        st.session_state.jugador_actual = None
    if 'pregunta_seleccionada' not in st.session_state:
        st.session_state.pregunta_seleccionada = None
    if 'reto_seleccionado' not in st.session_state:
        st.session_state.reto_seleccionado = None
    if 'ronda_iniciada' not in st.session_state:
        st.session_state.ronda_iniciada = False  # Estado de la ronda actual

# Función para cargar preguntas y retos desde un archivo CSV
def cargar_categoria(categoria):
    """Cargar las preguntas y retos de un archivo CSV según la categoría"""
    carpeta_preguntas = "preguntas"  # Asegúrate de tener esta carpeta con los archivos CSV
    archivo_csv = f"{carpeta_preguntas}/{categoria.lower()}.csv"
    
    try:
        df = pd.read_csv(archivo_csv)
        return df['pregunta'].tolist(), df['reto'].tolist()
    except FileNotFoundError:
        st.error(f"No se encontró el archivo CSV para la categoría {categoria}.")
        return [], []

# Cargar categorías disponibles
categorias = ["Nivel1", "Nivel2", "Nivel3"]

# Inicializar el juego
inicializacion_juego()

# Si el juego no está activo, mostrar la configuración de los jugadores
if not st.session_state.juego_activo:
    # Título del juego
    st.markdown("<h1 style='text-align: center;'> Juego de preguntas y retos</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Bienvenido al juego creado por Schnaider</h5>", unsafe_allow_html=True)

    # Configuración de los jugadores
    st.header("Configuración de los jugadores")
    col1, col2 = st.columns(2)

    with col1:
        numero_jugadores = st.number_input("¿Cuántos jugadores?", min_value=2, step=1, value=2)
        categoria = st.selectbox("Elige tu nivel:", categorias)
        jugar = st.button("Iniciar Juego", use_container_width=True)

    with col2:
        jugadores = []
        for i in range(numero_jugadores):
            nombre_jugador = st.text_input(f"Nombre del jugador {i + 1}:", key=f"jugador_{i}")
            if nombre_jugador:
                jugadores.append(nombre_jugador)

    # Verificar que todos los jugadores hayan sido ingresados
    if len(jugadores) == numero_jugadores and categoria and jugar:
        st.session_state.jugadores = jugadores
        st.session_state.categoria = categoria
        st.session_state.preguntas, st.session_state.retos = cargar_categoria(categoria)
        st.session_state.juego_activo = True
        st.session_state.jugador_actual = random.choice(st.session_state.jugadores)  # Elegir aleatoriamente un jugador inicial
        st.session_state.pregunta_seleccionada = None  # Asegurarse que no haya pregunta seleccionada inicialmente
        st.session_state.reto_seleccionado = None  # Asegurarse de que no haya reto seleccionado inicialmente
        st.session_state.ronda_iniciada = False  # Estado inicial de ronda no iniciada
        st.rerun()  # Recarga la página para mostrar la ronda de juego

else:
    # Cuando el juego esté activo, mostrar la "Ronda de Juego"
    st.header("Ronda de Juego")

    # Opción para cambiar de categoría en cualquier momento
    nueva_categoria = st.selectbox("Selecciona una categoría:", categorias, index=categorias.index(st.session_state.categoria))
    if nueva_categoria != st.session_state.categoria:
        st.session_state.categoria = nueva_categoria
        st.session_state.preguntas, st.session_state.retos = cargar_categoria(nueva_categoria)
        st.success(f"Categoría cambiada a: {nueva_categoria}")

    jugador_actual = st.session_state.jugador_actual

    # Si la ronda no ha iniciado, elegir una pregunta o reto aleatoriamente
    if not st.session_state.ronda_iniciada:
        if random.choice([True, False]):  # True para pregunta, False para reto
            if st.session_state.preguntas:
                pregunta_seleccionada = random.choice(st.session_state.preguntas)
                st.session_state.pregunta_seleccionada = pregunta_seleccionada
                st.session_state.reto_seleccionado = None  # Asegurarse de que no haya reto seleccionado
                st.write(f"**{jugador_actual}**, tu pregunta es: {pregunta_seleccionada}")
            else:
                st.write("¡No hay más preguntas disponibles!")
        else:
            if st.session_state.retos:
                reto_seleccionado = random.choice(st.session_state.retos)
                st.session_state.reto_seleccionado = reto_seleccionado
                st.session_state.pregunta_seleccionada = None  # Asegurarse de que no haya pregunta seleccionada
                otro_jugador = random.choice([j for j in st.session_state.jugadores if j != jugador_actual])
                st.write(f"**{jugador_actual}**, tu reto es: {reto_seleccionado} (Interacción con **{otro_jugador}**)")

            else:
                st.write("¡No hay más retos disponibles!")

    # Verificar si el jugador quiere continuar con la siguiente ronda
    col1, col2 = st.columns([3, 1])

    with col1:
        if st.button("Siguiente ronda"):
            # Cambiar al siguiente jugador
            st.session_state.jugadores_actuales = (st.session_state.jugadores_actuales + 1) % len(st.session_state.jugadores)
            st.session_state.jugador_actual = st.session_state.jugadores[st.session_state.jugadores_actuales]

            # Seleccionar nueva pregunta o reto para la siguiente ronda
            st.session_state.pregunta_seleccionada = None
            st.session_state.reto_seleccionado = None

            st.session_state.ronda_iniciada = False  # Reiniciar el estado de ronda

            st.rerun()  # Recargar la página para la siguiente ronda

    with col2:
        if st.button("Salir del Juego"):
            # Salir del juego
            st.session_state.juego_activo = False
            st.session_state.jugadores = []
            st.session_state.puntajes = {}
            st.session_state.categoria = None
            st.write("Gracias por jugar. ¡Hasta la próxima!")
