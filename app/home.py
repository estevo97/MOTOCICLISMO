import streamlit as st

def run():

    # Espacio superior
    st.write("")

    # Bloque con autor
    st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 5px 10px; border-radius: 5px;">
            <p style="margin: 0;">Creación y diseño: <b>ESTEVO ARIAS GARCÍA</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Bloque principal
    st.markdown(
        """
        <div style="
            background-color: white; 
            padding: 20px; 
            border-radius: 10px;
            box-shadow: 0px 0px 8px rgba(0,0,0,0.1);
        ">
            <h1 style="text-align: center;">Proyecto de Análisis del Mundial de Motociclismo</h1>

            <p style="text-indent: 1em; font-size: 1.05rem;">
                Este proyecto recoge un análisis exhaustivo del Campeonato del Mundo de Motociclismo,
                abarcando desde el año 1949 hasta la actualidad.
                Incluye procesos de <b>limpieza de datos</b>, <b>exploración estadística</b>,
                <b>visualización</b> y la creación de una pequeña <b>IA capaz de identificar circuitos</b>
                a partir de un dibujo realizado por el usuario.
            </p>

            <p style="text-indent: 1em; font-size: 1.05rem;">
                A través del menú lateral podrás navegar por las diferentes secciones del proyecto:
            </p>

            <ul style="font-size: 1.05rem; line-height: 1.6;">
                <li><b>Limpieza</b>: tratamiento de nulos, outliers y estructura del dataset.</li>
                <li><b>Análisis Exploratorio (EDA)</b>: estadísticas, tablas, densidades y visualizaciones.</li>
                <li><b>Resultados</b>: análisis de victorias, pilotos destacados y comparativas por categorías.</li>
                <li><b>Aplicación IA</b>: dibuja un circuito en la pizarra y un modelo IA lo clasifica.</li>
            </ul>

            <p style="text-indent: 1em; font-size: 1.05rem;">
                Navega, explora y disfruta de los datos del deporte de motor más espectacular del mundo.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )