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
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2008.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2009</h3>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2009.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2010</h3>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2010.jpg', use_container_width=True)
