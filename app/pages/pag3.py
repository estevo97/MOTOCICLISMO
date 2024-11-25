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
            <p style="text-indent: 1em;"> Se ha creado un gráfico interactivo con Plotly Express que muestra la evolución de la velocidad media en carrera en las tres categorías desde 2006 hasta 2012. 
            </p>
            <h3 style="text-indent: 1em;">Contextualización</h3>
            <p style="text-indent: 1em;"> En el período 2005 - 2009 se produjo un cambio de paradigma en la categoría reina de motociclismo. 
            </p>
        </div>
        """,
        unsafe_allow_html=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2006</h3>
            <p style="text-indent: 1em;"> El campeonato 2006, como podemos ver, se caracterizó por un duelo entre Nicky Hayden y Valentino Rossi, que finalmente se terminó
            llevando el estadounidense tras un final de campeonato muy emocionante. Dani Pedrosa debutaba ese año y se adijudicó un par de victorias a los mandos de su Repsol
            Honda. 
            </p>
            <p style="text-indent: 1em;"> Esta temporada se caracterizó por la enorme igualdad y por gran cantidad de ganadores diferentes. Si le echamos un vistazo a la gráfica de puntuación por carrera,
            vemos que hay mucha variabilidad carrera tras carrera. Es por este motivo que Nicky Hayden pudo hacerse con el título ganando únicamente en dos grandes premios (Holanda
            y EEUU), mientras que las cinco victorias no le sirvieron a Rossi para ser campeón.</p>
            <p style="text-indent: 1em;"> A modo de curiosidad: puede que les llame la atención las puntuaciones del gran premio de Catalunya, con una gran cantidad de ceros. Esto fue debido a una
            caída grupal que tuvo lugar en la salida tras un toque entre el español Sete Gibernau y Loris Capirossi, que terminó haciendo un efecto dominó involucrando a otros pilotos
            como Marco Melandri y Dani Pedrosa. El vídeo de la salida de ese caótico gran premio se puede visualizar en este link: <a href="https://www.youtube.com/watch?v=AOwNOT-BlG8" target="_blank"> Ver vídeo en YouTube </a>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2006.jpg', use_column_width=True)

st.write("")

st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Temporada 2007</h3>
            <p style="text-indent: 1em;"> El año 2007 fue el primero de la llamada era de las 800cc, que sustituyó a las 990cc. Se caracterizó por
        el dominio de <b>Casey Stoner</b> ya desde la primera carrera. Valentino Rossi y Dani Pedrosa alternaron algunas victorias y se disputaron el segundo puesto
        del campeonato. Mientras tanto, en la categoría de 250cc Jorge Lorenzo se convertía en bicampeón tras una temporada excelsa y se preparaba para dar el salto
        a MotoGP.
            </p>
        </div>
        """,
        unsafe_allow_html=True)

st.image('img/2007.jpg', use_column_width=True)

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

st.image('img/2008.jpg', use_column_width=True)

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

st.image('img/2009.jpg', use_column_width=True)

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

st.image('img/2010.jpg', use_column_width=True)
