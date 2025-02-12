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

tabla1 = pd.read_csv('tablas/tabla1.csv')
tabla1 = tabla1.rename(columns={tabla1.columns[0]: "Parámetro"})

tabla2 = pd.read_csv('tablas/cuantiles.csv')
tabla2 = tabla2.drop(tabla2.columns[0], axis=1)

tabla3 = pd.read_csv('tablas/top3.csv')
tabla3 = tabla3.drop(tabla3.columns[0], axis=1)

tabla4 = pd.read_csv('tablas/last3.csv')
tabla4 = tabla4.drop(tabla4.columns[0], axis=1)



tabla5 = pd.read_csv('tablas/paises_all.csv')
tabla5 = tabla5.drop(tabla5.columns[0], axis=1)

tabla6 = pd.read_csv('tablas/paises_500GP.csv')
tabla6 = tabla6.drop(tabla6.columns[0], axis=1)

tabla7 = pd.read_csv('tablas/paises_antes.csv')
tabla7 = tabla7.drop(tabla7.columns[0], axis=1)

tabla8 = pd.read_csv('tablas/paises_antes_500.csv')
tabla8 = tabla8.drop(tabla8.columns[0], axis=1)

url_victorias = st.secrets.get("POWERBI_URL_victorias")
url_velocidad_victorias = st.secrets.get("POWERBI_URL_velocidad_victorias")


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
        <h2 style="Tangerine"; color: #002200; margin-right: -17px;">EDA DETALLADO</h2> 
    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
    """
    <div style="background-color: white; padding: 10px; border-radius: 5px;">
        <div style="display: flex; align-items: center;">
            <span style="color: black; margin-right: 5px;">&#9658;</span>
            <h3 style="margin: 0;">Velocidad media en carrera</h3>
        </div>
        <p style="text-indent: 1em;">Velocidad media en carrera desde la temporada 2000 por circuito y categoría.</p>
    
    </div>
    """,
    unsafe_allow_html=True
)
    

st.write("")

components.iframe(url_velocidad_victorias, height=450, width=700)

st.write("")
st.components.v1.iframe('<iframe src="https://uphubgrade-my.sharepoint.com/personal/estevo_arias_bootcamp-upgrade_com/_layouts/15/Doc.aspx?sourcedoc={586b05ec-40f3-4662-b12f-338224b15db2}&amp;action=embedview&amp;wdAr=1.7777777777777777" width="476px" height="288px" frameborder="0">Esto es un archivo de presentación de <a target="_blank" href="https://office.com">Microsoft Office</a> incrustado con tecnología de <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>', width=800, height=600)
st.write("")

st.markdown(
    """
    <div style="background-color: white; padding: 10px; border-radius: 5px;">
        <div style="display: flex; align-items: center;">
        </div>
        <p style="text-indent: 1em;">Velocidad media en carrera durante el GP de San Marino 2021 (circuito de Misano).</p>
    </div>
    """,
    unsafe_allow_html=True
)
    
st.write("")
    
col1, col2 = st.columns([1, 2]) 

with col1:
        st.write(tabla3)
        st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
            <p>Tabla 3: Top 3 velocidad media en Missano 2021</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
with col2:
        st.write(tabla4)
        st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
            <p>Tabla 4: Bottom 3 velocidad media en Missano 2021</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 

st.write("")
st.write("")
        
st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            Densidad con suavizado de Kernel para la velocidad media en carrera desde el año 2000. 
            En la segunda gráfica se desglosa en tres categorías: reina, intermedia y ligera.
            </p>
        </div>
        """,
        unsafe_allow_html=True)    
    
st.write("")

st.image('img/velocidad.jpg', use_container_width=True)
    
st.write("")

st.image('img/velocidad_3_jorobas.jpg', use_container_width=True)
    
st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Máximos ganadores</h2>
            <p style="text-indent: 1em;"> En esta gráfica podemos observar quienes han sido los pilotos que más carreras han ganado desde el 
            año 2000. La aplicación de PowerBI nos permite interactuar con la gráfica y ver los datos totales o desglosados por categoría.
            </p>
            </div>
        """,
        unsafe_allow_html=True)
    
st.write("")

components.iframe(url_victorias, height=450, width=700)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> Si escogemos los datos totales, <b>Valentino Rossi</b> aparece en primer lugar con 87 victorias (si contásemos desde que debutó serían 115),
            seguido de cerca por Marc Márquez, que contaba con 85 (a día de hoy este dato es de 88). Por otro lado, escogiendo sólo los datos de la categoría
            máxima, se observa que Rossi, con sus mismas 87 victorias, <b>gana con amplia diferencia</b> al resto.</p>
            <p style="text-indent: 1em;"> Tanto en cómputo global como escogiendo sólo la catagoría reina, podemos apreciar claramente a los pilotos que han sido reconocidos
            tanto por la prensa como por los aficionados como <i>Los Cuatro Fantásticos</i>: en una primera etapa (2008 a 2012), este grupo estuvo
            conformado por los españoles <b>Jorge Lorenzo</b> y <b>Dani Pedrosa</b>, el australiano <b>Casey Stoner</b> y el mismo Rossi. Tras la retirada de Stoner
            a finales de 2012 y la irrupción de <b>Marc Márquez</b> en MotoGP para la temporada 2013, los <i>Cuatro Fantásticos</i> (también llamado el Big Four) pasaron
            a ser Rossi, Márquez, Lorenzo y Pedrosa.</p>
        </div>
        """,
        unsafe_allow_html=True)
    
st.write("")
    
st.image('img/los_4_fantasticos.jpg', use_container_width=True)

st.markdown(
        """
        <div style="background-color: white; padding: 0px; border-radius: 5px;">
            <p style="text-indent: 1em; font-size: 3.6mm;">     
            <i>Los Cuatro Fantásticos</i> tomando una curva en el circuito de Sachsenring. 
            Fuente: Wikimedia Commons. </p>
        </div>
        """,
        unsafe_allow_html=True)
    
st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Victorias por nacionalidad</h2>
            </div>
        """,
    unsafe_allow_html=True)
    
st.write("")

st.markdown(
        """
        <div style="background-color: white; padding:-2px; border-radius: 5px; text-align: center;">
            <h5 style="text-indent: 1em;">TABLAS 5, 6, 7 y 8. RECUENTO DE VICTORIAS</h5>
            </div>
        """,
    unsafe_allow_html=True)

st.write("")   
    
col1, col2 = st.columns([1, 2]) 
with col1:
        st.write(tabla5)
        st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
            <p>Tabla 5: Victorias por países en total</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 
with col2:
        st.write(tabla6)
        st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
            <p>Tabla 6: Victorias por países en la categoría reina</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 
    
st.write("")

st.write("")
    
col1, col2 = st.columns([1, 2]) 

with col1:
        st.write(tabla7)
        st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
            <p>Tabla 7: Victorias por países antes del año 2000</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 
with col2:
        st.write(tabla8)
        st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px; border-radius: 5px; text-align: center">
            <p>Tabla 8: Victorias por países antes del año 2000 en la categoría reina</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 
    
st.write("")

st.write("")
    
st.image('img/vel_anyo_cil.jpg', use_container_width=True)

st.write("")
    
st.image('img/vel_anyo_reina.jpg', use_container_width=True)
