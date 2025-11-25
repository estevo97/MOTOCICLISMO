from MOTOCICLISMO.app.pages import test_hipotesis
import streamlit as st
from streamlit_drawable_canvas import st_canvas
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
from dotenv import load_dotenv
import os

# ---------------------CARGAS PREVIAS----------------------#

tabla1 = pd.read_csv('../tablas/tabla1.csv')
tabla1 = tabla1.rename(columns={tabla1.columns[0]: "Parámetro"})

tabla2 = pd.read_csv('../tablas/cuantiles.csv')
tabla2 = tabla2.drop(tabla2.columns[0], axis=1)

tabla3 = pd.read_csv('../tablas/top3.csv')
tabla3 = tabla3.drop(tabla3.columns[0], axis=1)

tabla4 = pd.read_csv('../tablas/last3.csv')
tabla4 = tabla4.drop(tabla4.columns[0], axis=1)



tabla5 = pd.read_csv('../tablas/paises_all.csv')
tabla5 = tabla5.drop(tabla5.columns[0], axis=1)

tabla6 = pd.read_csv('../tablas/paises_500GP.csv')
tabla6 = tabla6.drop(tabla6.columns[0], axis=1)

tabla7 = pd.read_csv('../tablas/paises_antes.csv')
tabla7 = tabla7.drop(tabla7.columns[0], axis=1)

tabla8 = pd.read_csv('../tablas/paises_antes_500.csv')
tabla8 = tabla8.drop(tabla8.columns[0], axis=1)

warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))


load_dotenv()
url_victorias = os.getenv("POWERBI_URL_victorias")

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
            <li>Pag 4: Modelo NO SUPERVISADO</li>
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
        <img src="data:image/png;base64,{}" width="200" style="border-radius: 15px;">
    </div>
    """.format(base64.b64encode(open('../img/RBF_logo.png', "rb").read()).decode()),
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")

# # ---------------------MENU----------------------# 

#header image


page = option_menu(None, ["Home", "Limpieza", "EDA", "Temporadas", "Test de Hipótesis", "Modelo de Regresión", "Aplicación"], 
    icons=["house", "cone-striped", "bar-chart", "calendar3", "question", "stopwatch", "apple"], 
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
    df = pd.read_csv('../data/FILTERED_ROWS.csv')
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

add_bg_from_local('../img/icon_moto2.png')

# ---------------------BODY----------------------#




# Haz algo para que el titulo quede en un formato mas bonito

st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Black+Ops+One&display=swap" rel="stylesheet">
    </head>
    <div style="background: linear-gradient(to bottom, white, gray); 
                padding: 10px; 
                border-radius: 5px; 
                display: flex; 
                flex-direction: column; 
                align-items: flex-start; 
                gap: 10px; 
                font-family: 'Black Ops One', sans-serif; 
                color: #333;">
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{}" width="100">
            <div style="display: flex; flex-direction: column; margin-left: 30px;">
                <h1 style="font-family: 'Black Ops One', sans-serif; color: #333; margin-left: 0; display: inline">
                    <span style="
                        background-color: #4CAF60; 
                        color: white; 
                        padding: 0px 0px 0px 9px; /* Arriba, derecha, abajo, izquierda */ 
                        border-radius: 3px;
                        box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);">
                        An
                    </span>álisis 
                </h1>
                <h1 style="font-family: 'Black Ops One', sans-serif; color: #333; margin-left: 90px; display: inline;">
                    moto<span style="
                        background-color: #4CAF60; 
                        color: white; 
                        padding: 0px 0px 0px 0px; 
                        border-radius: 3px;
                        box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);">
                        GP
                    </span>ero
                </h1>
            </div>
            <img src="data:image/png;base64,{}" width="100">
        </div>
    </div>
    """.format(
        base64.b64encode(open('../img/icon_moto.png', "rb").read()).decode(),
        base64.b64encode(open('../img/icon_moto.png', "rb").read()).decode()
    ),
    unsafe_allow_html=True
)



# ---------------------HOME----------------------#

from pages import home
if page == "Home":
    home.run()



# ---------------------LIMPIEZA----------------------#



from pages import limpieza
if page == "Limpieza":
    limpieza.run()




# ---------------------EDA----------------------#

from pages import eda
if page == "EDA":
    eda.run()
    


# ---------------------TEMPORADAS----------------------#

from pages import temporadas
if page == "Temporadas":
    temporadas.run()


# ---------------------TEST DE HIPÓTESIS----------------------#

from pages import temporadas
if page == "Test de Hipótesis":
    test_hipotesis.run()

# ---------------------MODELO DE REGRESIÓN----------------------#

from pages import regresion
if page == "Modelo de Regresión":
    regresion.run()

# ---------------------APLICACIÓN----------------------#
        
from pages import aplicacion
if page == "Aplicación":
    aplicacion.run()



    

