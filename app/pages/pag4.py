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


st.set_page_config(page_title="Modelo NO Supervisado", page_icon="🏍️")
st.title("Modelo NO supervisado")
st.markdown("""En esta sección se presenta un modelo de aprendizaje no supervisado basado en el clustering de KMeans para agrupar a los 
circuitos de la temporada 2008 de acuerdo a sus características.""")


st.markdown(
    """
    <div style="background-color: white; padding: 10px; border-radius: 0px;">
        <h2 style="text-indent: 1em;">Clasificando los circuitos en clusters.</h2>
        <p style="text-indent: 1em;"> Nos interesa saber qué características comparten los circuitos: cantidad de curvas, recta más larga, desnivel, 
    tiempo por vuelta, etc. De este modo, podemos agrupar a los circuitos en unos pocos grupos y ver qué características comparten. Esto
    puede resultar útil para ver si hay pilotos que rinden mejor en un determinado tipo de circuito o si por el contrario este tipo de
    características no son tan importantes como otras que no se están teniendo en cuenta (correr en casa, climatología, racha de resultados, etc.).
        </p>
        <p style="text-indent: 1em;"> El modelo de clustering KMeans es un algoritmo de aprendizaje no supervisado 
    que agrupa los objetos en k grupos de acuerdo a sus atributos. En nuestro caso, k-means clasificará
    a los circuitos de la temporada 2008 según su longitud, número de curvas totales, 
    número de curvas de izquierda, longitud de la recta más larga, tiempo por vuelta del ganador del gran premio, 
    velocidad máxima en carrera y desnivel (diferencia en metros desde el punto más alto del circuito hasta el
    punto más bajo).
        </p>
        <p style="text-indent: 1em;"> El algoritmo k-means utiliza la distancia euclídea entre los objetos (circuitos) y los centroides de 
    los clusters, tratando de minimizar la suma de las distancias de los objetos a su centroide más próximo.
        </p>
        <p style="text-indent: 1em;"> Mayor número de clusters implica menor suma de distancias, pero computacionalmente es más costoso.
    Para escoger el número de clusters óptimo se representa gráficamente la suma de las distancias en función del número de clusters y se
    trata de encontrar el codo o los codos que deja la línea que une los puntos.
        </p>

    </div>
    """,
unsafe_allow_html=True)

st.image('img/codo_pca.jpg', use_container_width=True)

st.write("")

st.image('img/clusters_pca.jpg', use_container_width=True)
