import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import warnings
import base64
from pandas.errors import SettingWithCopyWarning
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
from plotly.subplots import make_subplots
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static
import xgboost as xgb
import json
from joblib import load
from pycaret.regression import load_model
from PIL import Image



tabla1 = pd.read_csv('../tablas/tabla1.csv')
tabla1 = tabla1.rename(columns={tabla1.columns[0]: "Parámetro"})

tabla2 = pd.read_csv('../tablas/cuantiles.csv')
tabla2 = tabla2.drop(tabla2.columns[0], axis=1)

warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))
 

# ---------------------SITE CONFIG----------------------#
st.set_page_config(
    page_title="Motociclismo",
    page_icon="🏍️",
    layout="centered", 
    initial_sidebar_state="collapsed", 
)

# Recuadro en el sidebar
st.sidebar.markdown(
    """
    <div style="
        background-color: #aa4433; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1); 
        font-size: 14px; 
        color: #ffffff;">
        <h3 style="color: #ffffff;">Índice</h3>
        <ul style="list-style-type: square; padding-left: 20px;">
            <li>App</li>
            <li>Pag 1: Descriptiva vbles.</li>
            <li>Pag 2: EDA detallado</li>
            <li>Pag 3: Análisis temporadas 2006-2012</li>
            <li>Pag 4: Conclusión</li>
        </ul>
        <p style="font-size: 12px; color: #ffffff;">Para ver estas secciones, haga click en el nombre de éstas en la parte superior del sidebar.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------LOGO----------------------#

st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <img src="data:image/png;base64,{}" width="200">
    </div>
    """.format(base64.b64encode(open(r'../img/RBF_logo.png', "rb").read()).decode()),
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")

# # ---------------------MENU----------------------# 

#header image


page = option_menu(None, ["Home", "Limpieza", "EDA", "Temporadas", "Test de Hipótesis", "Un poco de historia", "Aplicación"], 
    icons=["house", "cone-striped", "bar-chart", "calendar-check", "question", "book", "apple"], 
    default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px", "padding": "0px", "--hover-color": "#eee"},
        "icon": {"margin": "auto", "display": "block"}  # Centered icons
    }
)


# ---------------------LOAD DATA----------------------#

# read data
@st.cache_data()
def load_data():
    df = pd.read_csv(r'../data/FILTERED_ROWS.csv')
    return df

# load data
df = load_data()

# ---------------------BACKGROUND IMAGE----------------------#

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: 2000px 1200px;
            background-repeat: no-repeat;
            background-position: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

add_bg_from_local(r'../img/icon_moto2.png')

# ---------------------BODY----------------------#




# Haz algo para que el titulo quede en un formato mas bonito
st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Black+Ops+One&display=swap" rel="stylesheet">
    </head>
    <div style="
            background: linear-gradient(to bottom, white, gray); 
            padding: 10px; 
            border-radius: 5px; 
            display: flex; 
            align-items: center; 
            justify-content: flex-start; 
            gap: 10px; 
            font-family: 'Black Ops One', sans-serif; 
            color: #333;">
        <img src="data:image/png;base64,{}" width="100">
        <h1 style="font-family: 'Black Ops One', sans-serif; color: #333; margin-right: -17px;">Análisis de pilotaje</h1>
        <img src="data:image/png;base64,{}" width="100">
    </div>
    """.format(
        base64.b64encode(open(r'../img/icon_moto.png', "rb").read()).decode(),
        base64.b64encode(open(r'../img/icon_moto.png', "rb").read()).decode()
    ),
    unsafe_allow_html=True
)



# ---------------------HOME----------------------#

if page == "Home":
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h1>En este proyecto...</h1>
            Aquí se muestran detalles sobre la limpieza de datos.
        </div>
        """,
        unsafe_allow_html=True
    )



# ---------------------LIMPIEZA----------------------#



elif page == "Limpieza":
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h1>Limpieza de Datos</h1>
            <h2 style="text-indent: 1em;">Partición del dataset</h2>
            <p style="text-indent: 1em;"> El dataset original se ha dividido en <b>dos mitades</b>: la primera consta de los datos anteriores al año 2000 y la segunda de los datos de este año en adelante. Nos interesa el dataset 
            con los datos del 2000 en adelante, pero en determinadas partes del trabajo se hará uso de la primera parte de los datos o incluso del
            dateset original.
            </p>
            <p style="text-indent: 1em;"> La razón por la que se hace el corte es sencilla: los datos anteriores al 2000 son más complicados por varios motivos: el primero, que existen 
            muchos más datos faltantes, y el segundo y más importante es la existencia de <b>múltiples categorías</b> además de las tres más conocidas (125cc ó Moto3,
            250cc ó Moto2 y 500cc ó MotoGP) en las primeras décadas del campeonato, lo que complica hacer una comparación entre pilotos que destacaron en diferentes categorías. Si bien en la actualidad existe el consenso
            de que un piloto empieza en la tercera categoría y va escalando hasta hacerse con un sitio en MotoGP, durante las primeras décadas del campeonato
            del mundo de motociclismo no necesariamente sucedía esta transición. El caso más notorio en el motociclismo español es el de Ángel Nieto, que, considerado
            como el gran valedor del motociclismo español, triunfó únicamente en las categorías de 50cc y de 125cc obteniendo en total 13 campeonatos.</p>
            <h2 style="text-indent: 1em;">Tratamiento de Valores Nulos</h2>
            <p style="text-indent: 1em;">Se identificaron y trataron los valores nulos en el nuevo dataset de datos del año 2000 en adelante, que contiene casi 30000 datos. A continuación se muestra un resumen de los valores nulos encontrados:</p>
            <ul>
                <li>Number: hay algo más de 5000 valores nulos. Se imputó a partir de una <b>distribución uniforme</b> de números enteros del 1 al 99. </li>
                <li>Speed: hay casi mil valores nulos. Se imputó con el valor <b>promedio</b> de la speed de esa carrera en concreto. 
                Por ejemplo, si el piloto A abandona en la carrera de Assen del año 2004 en la categoría de 125cc, se obtiene su speed con la 
                media del resto de pilotos de 125cc de esa carrera.</li>
                <li>Time: 1 único nulo. Se opta por <b>eliminar dicho valor</b> porque no corresponde a ningún piloto importante.</li>
            </ul>
            <h2 style="text-indent: 1em;">Tratamiento de Valores Atípicos</h2>
            <p style="text-indent: 1em;"> Nos interesa la variable speed para encontrar posibles valores atípicos y ver si son legítimos o no:</p>
                <li><b>Tabla 1</b>: Observamos que hay muy poca desviación estándar y que el máximo toma un valor extremadamente alto.</li>
                <li><b>Tabla 2</b>: En línea con lo anterior, vemos cómo hay dos saltos fuera de lo común entre el percentil 0 con el percentil 0.025 y
                entre el percentil 0.975 y el percentil 1. Es evidente que hay outliers. </li>
        </div>
        """,
        unsafe_allow_html=True)
    st.write("")
    col1, col2 = st.columns([1, 2])  # Ajusta las proporciones según sea necesario
    with col1:
        st.write(tabla1)
        st.markdown(
        """
        <div style="background-color: white; padding: 5px; border-radius: 5px; text-align: center">
            <h5>Tabla 1: Descriptiva de la variable speed</h4>
        </div>
        """,
        unsafe_allow_html=True
    ) 
    with col2:
        st.write(tabla2)
        st.markdown(
        """
        <div style="background-color: white; padding: 5px; border-radius: 5px; text-align: center">
            <h5>Tabla 2: Percentiles de la variable speed</h4>
        </div>
        """,
        unsafe_allow_html=True
    )  
    st.write("")

    st.image(r'../img/boxplot_speed.jpg', use_column_width=True)
    
    st.write("")
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px">
            <h3 style="text-indent: 1em;">Recomendación para modelo de aprendizaje</h3>
            <p style="text-indent: 1em;">Como se puede comprobar en la <b>gráfica de caja</b> de la variable speed, tenemos valores
            atípicos tanto por arriba como por abajo. Los valores atípicos por arriba los consideraremos <b>legítimos</b>, ya que 
            corresponden a circuitos de alta velocidad como Phillip Island o Spielberg (este último circuito sólo ha sido gran premio desde 2016) 
            y han sido marcados por pilotos dMotoGP en esas carreras. </p>
            <p style="text-indent: 1em;">No se puede decir lo mismo de los valores atípicos por abajo, que lo más probable es que sean valores recogidos para
            pilotos que han tenido problemas en las primeras vueltas y que han rodado a un ritmo que no se puede considerar
            competitivo. </p>
            <p style="text-indent: 1em;">En caso de querer implementar un modelo predictivo, conviene eliminar los outliers por abajo de la variable speed, así
            como hacer un encodeado y escalado de las demás variables. En caso de querer hacer predicts de la velocidad media
            o de utilizar ésta como variable independiente, también es recomendable realizar nuevas particiones
            del dataset en donde se recojan sólo los valores de la cilindrada de interés. </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    





# ---------------------EDA----------------------#

elif page == "EDA":
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Velocidad media en carrera</h2>
            <p style="text-indent: 1em;"> La velocidad media de un gran premio de motociclismo depende, sobre todo, del trazado, las condiciones climáticas y 
            de la cilindrada. La varianza de esta variable entre los pilotos que terminaron la carrera es muy pequeña. Pongamos, por ejemplo, la 
            carrera de MotoGP en el circuito de Misano en 2021: como vemos, el ganador Marc Marquez tuvo una velocidad promedio de
            163.4 kilómetros por hora, mientras que el último piloto en terminar la carrera
            </p>
            <p style="text-indent: 1em;"> Creación de gráficos en de densidad con el suavizado de Kernel para la velocidad media por carrera desde el año 2000. 
            En la segunda gráfica se desglosa en tres categorías (categoría reina, segunda categoría y tercera categoría).
            </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    st.image(r'../img/velocidad.jpg', use_column_width=True)
    
    st.write("")

    st.image(r'../img/velocidad_3_jorobas.jpg', use_column_width=True)
    
    st.write("")

    st.image(r'../img/cilindradas_antiguas.jpg', use_column_width=True)
    
    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Máximos ganadores</h2>v
            <p style="text-indent: 1em;"> Creación de gráficos en de densidad con el suavizado de Kernel para la velocidad media por carrera desde el año 2000. 
            En la segunda gráfica se desglosa en tres categorías (categoría reina, segunda categoría y tercera categoría).
            </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNDA4YTM3YjktOGUyYy00ZTBhLTk3ODEtY2NiMmEyOThkNmYyIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9", height=450, width=700)