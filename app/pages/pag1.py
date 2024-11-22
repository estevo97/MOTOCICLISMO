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


st.set_page_config(page_title="Limpieza de Datos", page_icon="🧹")
st.title("Descriptiva de variables")
st.write("Una breve descriptiva de las variables de nuestro dataset.")


st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <table>
    <tr>
        <th>Variable</th>
        <th>Descripción</th>
    </tr>
    <tr>
        <td><strong>year</strong></td>
        <td>Año de la temporada (desde 1949 hasta 2021)</td>
    </tr>
    <tr>
        <td><strong>category</strong></td>
        <td>Cilindrada: 50cc, 80cc, 125cc, 250cc, 350cc, 500cc, MotoGP, Moto2, Moto3 y MotoE. <br>
        Dependiendo de la década van apareciendo algunas y desapareciendo otras; por ejemplo, en el año 2002 la categoría reina de 500cc pasa a llamarse MotoGP, y pocos años después 125cc y 250cc pasan a llamarse Moto3 y Moto2, respectivamente. Además, existen algunas categorías que duraron muy poco tiempo en las primeras décadas, como la de 350cc.</td>
    </tr>
    <tr>
        <td><strong>sequence</strong></td>
        <td>Orden del gran premio pertinente dentro del calendario de una temporada (la primera carrera tiene el valor de 1, la siguiente el 2, etc.)</td>
    </tr>
    <tr>
        <td><strong>shortname</strong></td>
        <td>Abreviatura del gran premio. <br>
        Por ejemplo: RSA es la abreviatura del Gran Premio de Sudáfrica, SPA la del Gran Premio de España en Jerez y VAL la del Gran Premio de la Comunidad Valenciana en el circuito de Ricardo Tormo.</td>
    </tr>
    <tr>
        <td><strong>circuit_name</strong></td>
        <td>Nombre del circuito</td>
    </tr>
    <tr>
        <td><strong>team_name</strong></td>
        <td>Nombre del equipo (Repsol Honda Team, Yamaha Factory Racing entre otros)</td>
    </tr>
    <tr>
        <td><strong>bike_name</strong></td>
        <td>Marca de la moto (Ducati, Honda, Aprilia, etc.)</td>
    </tr>
    <tr>
        <td><strong>position</strong></td>
        <td>Posición en la que quedó un piloto en el gran premio pertinente</td>
    </tr>
    <tr>
        <td><strong>points</strong></td>
        <td>Puntos que obtuvo el piloto en ese gran premio (puntúan los quince primeros mediante el sistema 25, 20, 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)</td>
    </tr>
    <tr>
        <td><strong>number</strong></td>
        <td>Número del piloto <br>
        Algunos pilotos como Valentino Rossi llevan siempre el mismo número a lo largo de su carrera mientras que otros lo cambian en algún momento o deciden correr con el número correspondiente a la clasificación en el mundial del año anterior. Esto suele ser más típico cuando un piloto gana el campeonato, que al año siguiente compita con el número 1.</td>
    </tr>
    <tr>
        <td><strong>country</strong></td>
        <td>Abreviatura del país del piloto</td>
    </tr>
    <tr>
        <td><strong>speed</strong></td>
        <td>Velocidad media del piloto durante el gran premio</td>
    </tr>
    <tr>
        <td><strong>time</strong></td>
        <td>Tiempo que tarda el piloto ganador en completar un gran premio en caso de ganar o distancia respecto al ganador del piloto pertinente</td>
    </tr>
</table>
        </div>
        """,
        unsafe_allow_html=True
    )