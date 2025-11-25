
import streamlit as st
import streamlit.components.v1 as components

# IMPORTA TUS TABLAS Y VARIABLES (AJUSTA A TU PROYECTO)
# from MOTOCICLISMO.app.data import tabla3, tabla4, tabla5, tabla6, tabla7, tabla8, url_victorias

def run():

    st.write("")

    # TÍTULO PRINCIPAL
    st.markdown(
        """
        <head>
            <link href="https://fonts.googleapis.com/css?family=Sofia" rel="stylesheet">
        </head>
        <div style="
                background: linear-gradient(to bottom, white, #666666); 
                padding: 10px; 
                border-radius: 15px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                gap: 10px; 
                font-family: 'Sofia', sans-serif; 
                color: #335577;">
            <h1 style="font-family: 'Tangerine', sans-serif; color: #002200; margin-right: -17px;">
                Análisis exploratorio de datos
            </h1> 
        </div>
        """,
        unsafe_allow_html=True
    )

    # INTRODUCCIÓN
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Velocidad media en carrera</h2>
            <p style="text-indent: 1em;">
            La velocidad media de un gran premio de motociclismo depende, sobre todo, del trazado, 
            las condiciones climáticas y de la cilindrada. La varianza de la velocidad media entre los pilotos 
            que terminaron la carrera es pequeña. Pongamos, por ejemplo, la carrera de MotoGP en el circuito de Misano 
            en 2021: como vemos, el ganador Marc Marquez tuvo una velocidad promedio de 163.4 km/h, mientras que 
            el último piloto en terminar, Takaki Nakagami, tuvo un promedio de 158.2 km/h.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # TABLAS 3 y 4
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(tabla3)
        st.markdown(
            """
            <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
                <p>Tabla 3: Top 3 velocidad media en Misano 2021</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.write(tabla4)
        st.markdown(
            """
            <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
                <p>Tabla 4: Bottom 3 velocidad media en Misano 2021</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # TEXTO SOBRE KDE
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            Creación de gráficos de densidad con suavizado de Kernel para la velocidad media por carrera desde el año 2000. 
            En la segunda gráfica se desglosa en tres categorías (reina, segunda y tercera).
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # GRÁFICOS DE VELOCIDAD
    st.image('../img/velocidad.jpg', use_column_width=True)
    st.write("")
    st.image('../img/velocidad_3_jorobas.jpg', use_column_width=True)
    st.write("")
    st.image('../img/cilindradas_antiguas.jpg', use_column_width=True)

    st.write("")

    # MÁXIMOS GANADORES
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Máximos ganadores</h2>
            <p style="text-indent: 1em;">
                En esta gráfica podemos observar quienes han sido los pilotos que más carreras han ganado desde 2000. 
                La aplicación de PowerBI permite interactuar con la gráfica.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    components.iframe(url_victorias, height=450, width=700)
    st.write("")

    # TEXTO SOBRE LOS CUATRO FANTÁSTICOS
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;">
                Si escogemos los datos totales, <b>Valentino Rossi</b> aparece en primer lugar con 87 victorias (115 si contamos desde su debut),
                seguido por Marc Márquez, con 85 (hoy 88). En categoría reina, Rossi domina con diferencia.
            </p>
            <p style="text-indent: 1em;">
                Tanto en cómputo global como en categoría reina, destacan los llamados 
                <i>Los Cuatro Fantásticos</i>: Jorge Lorenzo, Dani Pedrosa, Casey Stoner y Valentino Rossi. 
                Desde 2013, Marc Márquez sustituyó a Stoner como parte del Big Four.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.image('../img/los_4_fantasticos.jpg', use_column_width=True)
    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 0px; border-radius: 5px;">
            <p style="text-indent: 1em; font-size: 3.6mm;">     
            <i>Los Cuatro Fantásticos</i> tomando una curva en Sachsenring. Fuente: Wikimedia Commons.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # VICTORIAS POR PAÍS
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Victorias por nacionalidad</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding:-2px; border-radius: 5px; text-align: center;">
            <h5 style="text-indent: 1em;">TABLAS 5, 6, 7 y 8. RECUENTO DE VICTORIAS</h5>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # TABLAS 5 y 6
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(tabla5)
        st.markdown(
            """
            <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
                <p>Tabla 5: Victorias por país (total)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.write(tabla6)
        st.markdown(
            """
            <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
                <p>Tabla 6: Victorias por país (categoría reina)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # TABLAS 7 y 8
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(tabla7)
        st.markdown(
            """
            <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
                <p>Tabla 7: Victorias por país antes del 2000</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.write(tabla8)
        st.markdown(
            """
            <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
                <p>Tabla 8: Victorias por país antes del 2000 (categoría reina)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")