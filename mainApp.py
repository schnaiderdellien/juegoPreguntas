import streamlit as st
import random
import pandas as pd
import altair as alt

# Configuración de la página
st.set_page_config(page_title="Juego de Preguntas", page_icon="📱", layout="wide")

# Diccionarios de preguntas y retos
PREGUNTAS = {
  "nivel1": [
    "¿Qué es lo que más miedo te da de la vida adulta?",
    "¿Quién crees que es capaz de comer 1kg de pasta en una hora?",
    "¿Qué es lo peor que te podría pasar?",
    "¿Qué prefieres: tener el don de entender a los animales o escuchar lo que piensan las personas a tu alrededor siempre?",
    "¿Qué prefieres, volver al pasado o viajar al futuro?",
    "¿Roncas mientras duermes?",
    "¿Cuál es el sitio más raro en el que has hecho tus necesidades?",
    "¿Qué prefieres, que nadie venga a tu boda o que nadie venga a tu funeral?",
    "¿Qué prefieres, ser el primero de tus amigos en morir o ser el último?",
    "¿Qué envidias de cada una de las personas presentes?",
    "¿Con qué título de película definirías tu vida?",
    "¿Qué es lo que más valoras?",
    "¿Qué olor asqueroso te gusta en secreto?",
    "¿Qué es lo más raro que sueles hacer cuando estás solo?",
    "¿Qué te diferencia del resto?",
    "Del 0 al 10, ¿qué nota te pondrías?",
    "¿Cuál es tu mayor inseguridad?",
    "¿Qué es lo que más te hace enfadar?"
  ],
  "nivel2": [
    "¿Quién es para ti la persona más sexy de la habitación?",
    "¿Quién crees que liga más y por qué?",
    "¿Qué es lo peor que has hecho por amor?",
    "Tres defectos y tres virtudes tuyos.",
    "¿Con quién del grupo te harías un tatuaje?",
    "¿Con qué amistad te quedas de los aquí presentes?",
    "¿A quién salvarías primero de este grupo?",
    "¿A quién llamarías para enterrar un cadáver?",
    "¿Qué harías ahora mismo si supieras que no habría consecuencias de ningún tipo?",
    "¿Quién crees que es la persona que peor viste del grupo?",
    "¿Quién es más probable que acabe borracho hoy?",
    "¿Cómo romperías con una pareja de la forma más dolorosa y desagradable posible para la otra persona?",
    "Si tuvieras que matar a alguien del grupo, ¿a quién matarías y a quién pedirías que te ayude?",
    "¿Con qué tres personas no te tatuarías nada?",
    "¿Qué prefieres: oler mucho los pies de alguien siempre que os encontréis o no poder verlo?",
    "¿Qué nunca perdonarías?",
    "¿Te queda solo un minuto de vida, qué quieres decir?",
    "Si pudieras estar en la mente de alguien de este grupo, ¿de quién sería y por qué?",
    "¿Qué prefieres, ser infiel o que te pongan los cuernos?"
  ],
  "nivel3": [
    "¿Si nadie se enterara nunca, con quién pasarías una noche de pasión esta noche?",
    "¿Quién te parece el/la más guapo/a del grupo?",
    "¿A quién escogerías para hacer un trío?",
    "¿Con qué parejas de amigos querrías ir a un club de intercambio de parejas?",
    "¿Cuál es tu zona erógena más sensible?",
    "¿Cuál es tu fantasía sexual?",
    "¿Postura sexual favorita?",
    "¿Qué nota te darías en la cama?",
    "¿Qué es lo que te suele gustar hacer después del sexo?",
    "¿De qué te disfrazarías como fantasía sexual?",
    "¿Tendrías una relación abierta?",
    "¿Si alguien te diera un millón de euros por romper con tu pareja, lo harías?",
    "¿Si alguien te diera un millón de euros por ser infiel a tu pareja, lo serías?",
    "¿Con cuántas personas te has acostado?",
    "¿A quién llamarías para enterrar un cadáver?",
    "¿Escoge a dos personas que quieras que se besen?",
    "¿Qué prefieres: ser infiel o que te pongan los cuernos?",
    "¿A quién salvarías primero de este grupo?"
  ]
}
RETOS = {
"nivel1": [
        "Canta una canción frente a ",
        "Bebe por cada positivo que le dicen a ",
        "Imita a alguien del grupo, por cada fallo bebes adivina ",
        "Cuenta un chiste si se ríe bebe, a  ",
        "Da 10 vueltas sobre ti mismo y luego ponte a correr en línea recta cogido de la mano de ",
        "Haz una lucha de brazos con ",
        "Cuenta algo que nadie sepa. a ",
        "Cuenta tu experiencia más vergonzosa. a",
        "Haz una declaración de amor a ",
        "Dibuja un «tatuaje» en la cara con un marcador al jugador a",
        "Bebe por cada vez que beba ",
        "Pasale 3 chupitos a "
    ],
    "nivel2": [
        "Bebe 2 chupitos o di algo negativo de ",
        "Hazle un masaje a ",
        "Baila la canción que te ponga ",
        "Si te queda menos de la mitad de bateria bebe un chupito y le das tres a",
        "Dale un abrazo a ",
        "Gira una botella y besa a quien toque. gira la botella ",
        "Describe la relación con el título de una canción a ",
        "Cuenta lo que sientes por ",
        "Hasta que te vuelva a tocar no puedes hablar si hablas te dirá lo que tiene que beber",
        "Imita un orgamos de ",
        "Cierra los ojos, ponte en medio de los jugadores y adivina quiénes son tocándoles la nariz. elige el jugador "
    ],
    "nivel3": [
        "Besa donde quieras a",
        "Cierra los ojos y deja que te bese donde quiera.",
        "Quedarse en ropa interior delante de todos durante una ronda.",
        "Haz un baile sexy a ",
        "Haz una imitación de",
        "Bebe un chupito de tequila de la parte del cuerpo de ",
        "Pasa la lengua por el cuello de ",
        "Lame la mejilla de",
        "Di la primera letra del nombre de tu ex por cada fallo bebes, adivina"
    ]
}
# Inicialización del juego
def inicializacion_juego():
    """Inicializar las variables de sesión"""
    if 'jugadores' not in st.session_state:
        st.session_state.jugadores = []
    if 'jugadores_actuales' not in st.session_state:
        st.session_state.jugadores_actuales = 0
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
    if 'puntuaciones' not in st.session_state:
        st.session_state.puntuaciones = {}
    if 'ocultar_mensaje' not in st.session_state:
        st.session_state.ocultar_mensaje = False

# Inicializar el juego
inicializacion_juego()

# Configuración del juego inicial
if not st.session_state.juego_activo:
    st.markdown("<h1 style='text-align: center;'>Juego de Preguntas y Retos</h1>", unsafe_allow_html=True)

    st.header("Configuración de los jugadores")
    col1, col2 = st.columns(2)

    with col1:
        numero_jugadores = st.number_input("¿Cuántos jugadores?", min_value=2, step=1, value=2)
        categoria = st.selectbox("Elige tu nivel:", list(PREGUNTAS.keys()))
        jugar = st.button("Iniciar Juego")

    with col2:
        jugadores = []
        for i in range(numero_jugadores):
            nombre_jugador = st.text_input(f"Nombre del jugador {i + 1}:", key=f"jugador_{i}")
            if nombre_jugador:
                jugadores.append(nombre_jugador)

    if len(jugadores) == numero_jugadores and jugar:
        st.session_state.jugadores = jugadores
        st.session_state.categoria = categoria
        st.session_state.juego_activo = True
        st.session_state.jugador_actual = random.choice(jugadores)
        st.session_state.puntuaciones = {jugador: 0 for jugador in jugadores}
        st.rerun()

# Ronda de Juego
else:
    st.markdown("<h1 style='text-align: center;'>Ronda de Juego</h1>", unsafe_allow_html=True)
    
    # Selector de categoría en cualquier momento
    nueva_categoria = st.selectbox(
        "Selecciona una categoría:", list(PREGUNTAS.keys()), 
        index=list(PREGUNTAS.keys()).index(st.session_state.categoria)
    )
    if nueva_categoria != st.session_state.categoria:
        st.session_state.categoria = nueva_categoria
        st.session_state.pregunta_seleccionada = None
        st.session_state.reto_seleccionado = None
        st.session_state.ocultar_mensaje = False
        st.success(f"Categoría cambiada a: {nueva_categoria}")
        st.rerun()

    jugador_actual = st.session_state.jugador_actual

    # Mostrar Pregunta/Reto si no está oculto
    if not st.session_state.ocultar_mensaje:
        if not st.session_state.pregunta_seleccionada and not st.session_state.reto_seleccionado:
            if random.choice([True, False]):
                st.session_state.pregunta_seleccionada = random.choice(PREGUNTAS[st.session_state.categoria])
            else:
                st.session_state.reto_seleccionado = random.choice(RETOS[st.session_state.categoria])

        if st.session_state.pregunta_seleccionada:
            st.markdown(f"<h2 style='text-align: center;'>{jugador_actual}, {st.session_state.pregunta_seleccionada}</h2>", unsafe_allow_html=True)
        elif st.session_state.reto_seleccionado:
            otro_jugador = random.choice([j for j in st.session_state.jugadores if j != jugador_actual])
            st.markdown(f"<h2 style='text-align: center;'>{jugador_actual}, {st.session_state.reto_seleccionado} {otro_jugador}</h2>", unsafe_allow_html=True)

    # Botón para la siguiente ronda
    if st.button("Siguiente ronda"):
        st.session_state.jugadores_actuales = (st.session_state.jugadores_actuales + 1) % len(st.session_state.jugadores)
        st.session_state.jugador_actual = st.session_state.jugadores[st.session_state.jugadores_actuales]
        st.session_state.pregunta_seleccionada = None
        st.session_state.reto_seleccionado = None
        st.session_state.ocultar_mensaje = False
        st.rerun()

    # Mostrar puntuaciones actuales en dos columnas
    st.header("Puntuaciones")
    col1, col2 = st.columns(2)

    with col1:
        # Campos number_input para modificar puntos
        for jugador in st.session_state.jugadores:
            puntos = st.number_input(
                f"{jugador}:",
                min_value=-50,
                max_value=50,
                step=1,
                value=st.session_state.puntuaciones[jugador],
                key=f"puntos_{jugador}"
            )
            if puntos != st.session_state.puntuaciones[jugador]:
                st.session_state.puntuaciones[jugador] = puntos
                st.session_state.ocultar_mensaje = True
                st.rerun()

    with col2:
        # Gráfica de puntuaciones
        if st.session_state.puntuaciones:
            df_puntos = pd.DataFrame({
                "Jugador": list(st.session_state.puntuaciones.keys()),
                "Puntuación": list(st.session_state.puntuaciones.values())
            })
            
            # Crear gráfico de barras con Altair
            chart = alt.Chart(df_puntos).mark_bar().encode(
                y=alt.X("Jugador:N", title="Jugador", sort=None),
                x=alt.Y("Puntuación:Q", title="Puntuación"),
                color=alt.Color("Jugador:N", legend=None)
            ).properties(
                width=300,
                height=400
            )
            st.altair_chart(chart, use_container_width=True)

    # Botón para salir del juego
    if st.button("Salir del Juego"):
        st.session_state.juego_activo = False
        st.session_state.jugadores = []
        st.session_state.categoria = None
        st.session_state.puntuaciones = {}
        st.write("Gracias por jugar. ¡Hasta la próxima!")
