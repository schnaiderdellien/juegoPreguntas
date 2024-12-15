import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Juego de Preguntas", page_icon="📱", layout="wide")

# Diccionarios de preguntas y retos
PREGUNTAS = {
"nivel1": [
        "¿Cuál es tu color favorito?",
        "¿Cuál es tu comida favorita?",
        "¿Tienes una mascota?",
        "¿Qué superpoder te gustaría tener?",
        "¿Cuál es tu animal favorito?",
        "¿Prefieres el verano o el invierno?",
        "¿Qué película has visto más veces?",
        "¿Cuál es tu deporte favorito?",
        "¿Qué harías con un millón de dólares?",
        "¿Qué lugar del mundo te gustaría visitar?",
        "¿Cuál es tu serie de televisión favorita?",
        "¿Qué instrumento musical te gustaría tocar?",
        "¿Te gusta más la playa o la montaña?",
        "¿Cuál es tu helado favorito?",
        "¿Cuál es tu juego de mesa preferido?",
        "¿Qué harías si fueras invisible por un día?",
        "¿Cuál es tu canción favorita?",
        "¿Te gusta más leer o ver películas?",
        "¿Prefieres perros o gatos?",
        "¿Qué libro recomendarías a un amigo?"
    ],
    "nivel2": [
        "¿Qué tres cosas te llevarías a una isla desierta?",
        "¿Qué harías si pudieras viajar en el tiempo?",
        "¿Cómo describirías un día perfecto?",
        "¿Cuál es el mayor logro de tu vida?",
        "¿Qué tipo de vacaciones te gustan más?",
        "Si fueras presidente, ¿qué sería lo primero que harías?",
        "¿Qué es algo que siempre has querido aprender?",
        "¿Qué harías si te encontraras con tu ídolo?",
        "¿Cuál es tu recuerdo favorito de la infancia?",
        "¿Qué cambiarías de tu rutina diaria?",
        "¿Cuál es el mejor consejo que te han dado?",
        "¿Qué harías si ganaras la lotería?",
        "¿Qué es algo que te hace feliz instantáneamente?",
        "¿Cómo sería tu casa soñada?",
        "¿Qué película te ha hecho llorar más?",
        "¿Qué talento secreto tienes?",
        "¿Qué harías si fueras famoso por un día?",
        "¿Qué tres palabras te describen mejor?",
        "¿Cuál es el mejor regalo que has recibido?",
        "¿Qué habilidad te gustaría mejorar?"
    ],
    "nivel3": [
        "¿Cuál ha sido la decisión más difícil que has tomado?",
        "¿Cómo te gustaría ser recordado?",
        "¿Qué harías si solo te quedara un día de vida?",
        "¿Cuál ha sido el mayor desafío que has enfrentado?",
        "¿Qué es algo que lamentas no haber hecho?",
        "Si pudieras cambiar algo de tu pasado, ¿qué sería?",
        "¿Qué es lo más valioso que posees?",
        "¿Qué persona ha tenido el mayor impacto en tu vida?",
        "¿Cuál es tu mayor miedo y por qué?",
        "¿Qué te motiva a seguir adelante en momentos difíciles?",
        "¿Qué significa el éxito para ti?",
        "¿Qué opinas sobre la importancia del dinero en la vida?",
        "¿Cómo definirías la felicidad?",
        "¿Qué valores consideras más importantes en una persona?",
        "¿Cuál ha sido tu mayor lección de vida hasta ahora?",
        "¿Qué es lo más arriesgado que has hecho?",
        "¿Qué te hace sentir más orgulloso de ti mismo?",
        "¿Qué importancia le das a la familia en tu vida?",
        "¿Qué es algo que harías diferente si tuvieras otra oportunidad?",
        "¿Qué sueños o metas tienes aún por cumplir?"
    ]
}
RETOS = {
"nivel1": [
        "Canta una canción frente a todos.",
        "Haz 10 saltos de tijera.",
        "Imita a un animal durante 30 segundos.",
        "Baila como si no te estuviera viendo nadie.",
        "Cuenta un chiste gracioso.",
        "Haz 5 flexiones.",
        "Imita a una celebridad famosa.",
        "Haz una mueca durante 30 segundos.",
        "Haz una declaración de amor a un objeto inanimado.",
        "Imita a un personaje de dibujos animados.",
        "Recita el abecedario al revés.",
        "Haz una llamada telefónica fingiendo que eres alguien más.",
        "Baila durante 1 minuto sin parar.",
        "Imita un objeto en el que todo el mundo lo pueda reconocer.",
        "Canta la canción de una película Disney.",
        "Haz una historia inventada usando solo 3 palabras.",
        "Haz 10 abdominales.",
        "Actúa como si fueras un superhéroe durante 1 minuto.",
        "Di un trabalenguas muy rápido.",
        "Haz un tutorial inventado sobre algo."
    ],
    "nivel2": [
        "Haz una entrevista a alguien sobre su día como si fueras un reportero.",
        "Haz un reto de 30 segundos de hacer mímica con un tema elegido al azar.",
        "Escribe un poema en 1 minuto.",
        "Realiza una actividad deportiva durante 2 minutos.",
        "Imita a tu cantante favorito durante 1 minuto.",
        "Haz 5 piruetas sin caerte.",
        "Recita 5 trabalenguas difíciles de manera fluida.",
        "Toma un selfie en una pose creativa.",
        "Haz una escena dramática de una película famosa.",
        "Imita a tus padres durante 1 minuto.",
        "Haz una llamada telefónica fingiendo ser alguien famoso.",
        "Haz una competencia de risas con alguien.",
        "Escribe una carta a tu futuro yo.",
        "Recita un discurso sobre la importancia de la amistad.",
        "Haz 20 saltos en el lugar.",
        "Haz 10 sentadillas.",
        "Actúa como si fueras un personaje histórico durante 2 minutos.",
        "Haz una rutina de baile inventada con música.",
        "Imita el sonido de una tormenta.",
        "Haz 20 abdominales mientras cantas una canción."
    ],
    "nivel3": [
        "Imagina que eres un líder mundial y da un discurso importante.",
        "Escribe un discurso sobre la paz mundial.",
        "Haz una crítica de una película como si fueras un experto.",
        "Actúa como un personaje famoso en una escena de acción.",
        "Haz una imitación de un político famoso.",
        "Escribe y recita una carta a tu yo más joven.",
        "Haz un resumen de tu vida en 1 minuto.",
        "Imagina que eres un maestro y explica un tema complejo.",
        "Imita a tu actor favorito en una escena dramática.",
        "Haz una canción improvisada sobre un tema aleatorio.",
        "Haz una escena de una película de terror.",
        "Imagina que estás en una entrevista de trabajo y responde preguntas difíciles.",
        "Haz un reto de improvisación con un tema que te den.",
        "Haz una presentación sobre el futuro de la tecnología.",
        "Imita a un animal extinto como si lo hubieras visto en persona.",
        "Explica de manera divertida y creativa cómo hacer algo complicado.",
        "Crea una historia improvisada sobre un héroe que salva al mundo.",
        "Haz una presentación como si fueras un experto en ciencia.",
        "Actúa como si fueras un astronauta en el espacio.",
        "Escribe y recita un monólogo profundo sobre la vida."
    ]
}

# Inicialización del juego
def inicializacion_juego():
    """Inicializar las variables de sesión"""
    if 'jugadores' not in st.session_state:
        st.session_state.jugadores = []
    if 'jugadores_actuales' not in st.session_state:
        st.session_state.jugadores_actuales = 0  # Para el control de turnos
    if 'juego_activo' not in st.session_state:
        st.session_state.juego_activo = False
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

# Inicializar el juego
inicializacion_juego()

# Si el juego no está activo, mostrar la configuración de los jugadores
if not st.session_state.juego_activo:
    # Título del juego
    st.markdown("<h1 style='text-align: center;'>Juego de Preguntas y Retos</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Bienvenido al juego creado por Schnaider</h5>", unsafe_allow_html=True)

    # Configuración de los jugadores
    st.header("Configuración de los jugadores")
    col1, col2 = st.columns(2)

    with col1:
        numero_jugadores = st.number_input("¿Cuántos jugadores?", min_value=2, step=1, value=2)
        categorias = list(PREGUNTAS.keys())
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
        st.session_state.preguntas = PREGUNTAS[categoria.lower()]
        st.session_state.retos = RETOS[categoria.lower()]
        st.session_state.juego_activo = True
        st.session_state.jugador_actual = random.choice(st.session_state.jugadores)  # Elegir aleatoriamente un jugador inicial
        st.session_state.pregunta_seleccionada = None
        st.session_state.reto_seleccionado = None
        st.session_state.ronda_iniciada = False
        st.rerun()  # Recarga la página para mostrar la ronda de juego

else:
    # Cuando el juego esté activo, mostrar la "Ronda de Juego"
    st.header("Ronda de Juego")

    # Opción para cambiar de categoría en cualquier momento
    nueva_categoria = st.selectbox("Selecciona una categoría:", list(PREGUNTAS.keys()), 
                                   index=list(PREGUNTAS.keys()).index(st.session_state.categoria))
    if nueva_categoria != st.session_state.categoria:
        st.session_state.categoria = nueva_categoria
        st.session_state.preguntas = PREGUNTAS[nueva_categoria.lower()]
        st.session_state.retos = RETOS[nueva_categoria.lower()]
        st.success(f"Categoría cambiada a: {nueva_categoria}")

    jugador_actual = st.session_state.jugador_actual

    # Si la ronda no ha iniciado, elegir una pregunta o reto aleatoriamente
    if not st.session_state.ronda_iniciada:
        if random.choice([True, False]):  # True para pregunta, False para reto
            if st.session_state.preguntas:
                pregunta_seleccionada = random.choice(st.session_state.preguntas)
                st.session_state.pregunta_seleccionada = pregunta_seleccionada
                st.session_state.reto_seleccionado = None
                st.write(f"**{jugador_actual}**, tu pregunta es: {pregunta_seleccionada}")
            else:
                st.write("¡No hay más preguntas disponibles!")
        else:
            if st.session_state.retos:
                reto_seleccionado = random.choice(st.session_state.retos)
                st.session_state.reto_seleccionado = reto_seleccionado
                st.session_state.pregunta_seleccionada = None
                otro_jugador = random.choice([j for j in st.session_state.jugadores if j != jugador_actual])
                st.write(f"**{jugador_actual}**, tu reto es: {reto_seleccionado} (Interacción con **{otro_jugador}**)")
            else:
                st.write("¡No hay más retos disponibles!")

    # Verificar si el jugador quiere continuar con la siguiente ronda
    col1, col2 = st.columns([3, 1])

    with col1:
        if st.button("Siguiente ronda"):
            st.session_state.jugadores_actuales = (st.session_state.jugadores_actuales + 1) % len(st.session_state.jugadores)
            st.session_state.jugador_actual = st.session_state.jugadores[st.session_state.jugadores_actuales]
            st.session_state.pregunta_seleccionada = None
            st.session_state.reto_seleccionado = None
            st.session_state.ronda_iniciada = False
            st.rerun()

    with col2:
        if st.button("Salir del Juego"):
            st.session_state.juego_activo = False
            st.session_state.jugadores = []
            st.session_state.categoria = None
            st.write("Gracias por jugar. ¡Hasta la próxima!")
