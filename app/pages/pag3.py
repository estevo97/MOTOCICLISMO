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

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Análisis de temporadas 2006-2010</h2>
            <p style="text-indent: 1em;"> En este apartado se analizan las temporadas 2006-2010, que son las que se han considerado más relevantes para el análisis de la velocidad media en carrera. 
            </p>
        </div>
        """,
        unsafe_allow_html=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2006</h3>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2006.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2007</h3>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2007.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2008</h3>
            <p style="text-indent: 1em;"> En el año 2008 debutó el mallorquín <b>Jorge Lorenzo</b> como compañero de equipo de Valentino Rossi.
        Este año consistió en una lucha cuerpo a cuerpo entre Stoner y Rossi, que tuvo su climax durante el Gran Premio de Laguna Seca, donde se recuerda
        el famoso adelantamiento de Rossi a Stoner en la curva de la sacacorchos. No obstante, durante la primera mitad del campeonato el dominio
        fue de Pedrosa, que pese a contar con tan sólo dos victorias era el más regular. En el Gran Premio de Alemania, con la pista mojada y con Pedrosa de
        cabalgando hacia la victoria, una mala caída en la curva 1 le destrozó el hombro y su lucha por el título mundial se esfumó.   
            </p>
            <p> En cuanto a Jorge Lorenzo, tuvo un gran inicio de temporada obteniendo tres pole positions consecutivas y una victoria en estoril, pero una
        serie de caídas a partir de la carrera de Shangai lastraron su buen arranque y acabó teniendo un final de campeonato algo discreto.
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2008.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2009</h3>
            <p style="text-indent: 1em;"> En el año 2009 
            </p>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2009.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2010</h3>
            <p style="text-indent: 1em;"> En el año 2010    
            </p>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2010.jpg', use_container_width=True)
