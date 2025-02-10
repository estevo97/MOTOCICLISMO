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
            <h3 style="text-indent: 1em;">Análisis de reaultados de pilotos por temporada</h3>
        </div>
        """,
        unsafe_allow_html=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h4 style="text-indent: 1em;">Temporada 2006</h4>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2006.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h4 style="text-indent: 1em;">Temporada 2007</h4>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2007.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h4 style="text-indent: 1em;">Temporada 2008</h4>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2008.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h4 style="text-indent: 1em;">Temporada 2009</h4>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2009.jpg', use_container_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h4 style="text-indent: 1em;">Temporada 2010</h4>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2010.jpg', use_container_width=True)
