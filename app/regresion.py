import streamlit as st
import numpy as np
import joblib

def run():

    st.title("Modelo de Regresión")

    # Encabezado estilizado
    st.markdown(
        """
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Tangerine&display=swap" rel="stylesheet">
        </head>
        <div style="
                background: linear-gradient(to bottom, white, #007722); 
                padding: 10px; 
                border-radius: 15px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                gap: 10px; 
                font-family: 'Tangerine', sans-serif; 
                color: #335577;">
            <h1 style="font-family: 'Tangerine', sans-serif; color: #112266; margin-right: -17px;">
                Modelo de aprendizaje: Random Forest Regression
            </h1> 
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Estimamos el tiempo por vuelta de tu circuito</h3>
            <p style="text-indent: 1em;"> 
                Se ha creado un modelo de regresión Random Forest que permite estimar el tiempo por vuelta en 
                base a los siguientes parámetros:
            </p>
            <ul style="text-indent: 1em;">
                <li>Longitud del circuito</li>
                <li>Número de curvas</li>
                <li>Número de curvas a izquierda</li>
                <li>Longitud de la recta más larga</li>
                <li>Máxima velocidad en carrera</li>
                <li>Desnivel del circuito</li>
            </ul>
            <p style="text-indent: 1em;">
                Introduce los <b>datos de tu circuito</b> y te diremos cuánto tardarías en dar una vuelta. 
                <b>Fíjate bien en las unidades!</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # Cargar modelo una sola vez
    @st.cache_resource
    def cargar_modelo():
        return joblib.load('model_RF.pkl')

    model = cargar_modelo()

    # CSS para inputs
    st.markdown(
        """
        <style>
            div[data-testid="stNumberInput"] > label {
                background-color: white;
                padding: 5px 10px;
                border-radius: 5px;
                box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Inputs
    longitud = st.number_input('Longitud del circuito (km)', min_value=0.0, max_value=100.0, value=4.0)
    curvas = st.number_input('Número de curvas', min_value=0, max_value=100, value=10)
    curvas_izq = st.number_input('Número de curvas a izquierda', min_value=0, max_value=100, value=5)
    recta = st.number_input('Longitud de la recta más larga (km)', min_value=0.0, max_value=100.0, value=1.0)
    velocidad = st.number_input('Máxima velocidad en carrera (km/h)', min_value=0, max_value=400, value=300)
    desnivel = st.number_input('Desnivel del circuito (m)', min_value=-1000, max_value=1000, value=0)

    input_data = np.array([longitud, curvas, curvas_izq, recta, velocidad, desnivel]).reshape(1, -1)

    # Botón de predicción
    if st.button('Predecir'):
        prediction = model.predict(input_data)[0] / 1000  # pasa ms → s
        segundos = prediction
        minutos = int(segundos // 60)
        segundos_restantes = segundos % 60
        tiempo_formateado = f"{minutos}:{segundos_restantes:06.3f}"

        st.markdown(
            f"""
            <div style="background-color: white; padding: 10px; border-radius: 5px; text-align: center;">
                <h4><i>Tiempo estimado por vuelta (min:seg.milésimas):</i></h4>
                <p style="font-size: 24px; font-weight: bold;">{tiempo_formateado}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.image('img/flag.png', use_container_width=True)