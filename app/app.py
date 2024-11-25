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
from dotenv import load_dotenv
import os

# ---------------------CARGAS PREVIAS----------------------#

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

warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))


load_dotenv()
url_victorias = st.secrets.get("POWERBI_URL_victorias")

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
    """.format(base64.b64encode(open('img/RBF_logo.png', "rb").read()).decode()),
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
    df = pd.read_csv('data/FILTERED_ROWS.csv')
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

add_bg_from_local('img/icon_moto2.png')

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
        base64.b64encode(open('img/icon_moto.png', "rb").read()).decode(),
        base64.b64encode(open('img/icon_moto.png', "rb").read()).decode()
    ),
    unsafe_allow_html=True
)



# ---------------------HOME----------------------#

if page == "Home":

    st.write("")
    st.markdown(
        """
        <div style="background-color: #EECCAA; padding: 0px 0px 0px 10px; border-radius: 5px;">
            <p>Creación y diseño: <b>ESTEVO ARIAS GARCÍA</b></p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown(
    """
    <div style="background-color: white; padding: 20px; border-radius: 10px; font-family: Arial, sans-serif;">
        <h1 style="text-align: center; color: #2E86C1;">¡Bienvenido a nuestra aplicación!</h1>
        <h2 style="margin-top: 20px; color: #117A65;">Podrá usted consultar:</h2>
        <ul style="list-style-type: square; line-height: 1.8; margin-left: 20px;">
            <li><b><span style="color: #8E44AD;">LIMPIEZA:</span></b> <i>El pre-procesamiento de los datasets que utilizamos.</i></li>
            <li><b><span style="color: #D35400;">EDA:</span></b> <i>Gráficas comentadas de nuestros análisis exploratorios.</i></li>
            <li><b><span style="color: #2874A6;">TEMPORADAS:</span></b> <i>Analizamos algunas temporadas y sacamos conclusiones inéditas.</i></li>
            <li><b><span style="color: #16A085;">CONTRASTE DE HIPÓTESIS:</span></b> <i>Resolvemos algunas dudas que muchos aficionados al motociclismo tienen/tenemos.</i></li>
            <li><b><span style="color: #C0392B;">MODELO DE REGRESIÓN:</span></b> <i>Con nuestro nuevo modelo, podrá usted introducir los datos de su circuito (real o ficticio) y éste le dirá el tiempo por vuelta estimado.</i></li>
            <li><b><span style="color: #7D3C98;">Sidebar:</span></b> <i>Información más pormenorizada de todos estos procesos.</i></li>
            <li><b><span style="color: #1F618D;">Y mucho más:</span></b> <i>¡Esto se actualiza cada día!</i></li>
        </ul>
        <h2 style="margin-top: 30px; color: #117A65;">Próximas novedades:</h2>
        <p style="text-indent: 20px; line-height: 1.8;">En pocas semanas, estará disponible la nueva aplicación con la red neuronal <b>InceptionV3</b>, con la que podrá 
        <i>dibujar con el cursor un TRAZADO de un circuito real</i>, y ésta le dirá el nombre del circuito con sus datos y estadísticas.</p>
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

    st.image('img/boxplot_speed.jpg', use_column_width=True)
    
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
        <h1 style="font-family: 'Tangerine', sans-serif; color: #002200; margin-right: -17px;">Análisis exploratorio de datos</h1> 
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Velocidad media en carrera</h2>
            <p style="text-indent: 1em;"> La velocidad media de un gran premio de motociclismo depende, sobre todo, del trazado, las condiciones climáticas y 
            de la cilindrada. La varianza de la velocidad media entre los pilotos que terminaron la carrera pequeña. Pongamos, por ejemplo, la 
            carrera de MotoGP en el circuito de Misano en 2021: como vemos, el ganador Marc Marquez tuvo una velocidad promedio de
            163.4 kilómetros por hora, mientras que el último piloto en terminar la carrera, Taaki Nakagami, tuvo un promedio de 158.2 km/h.
            </p>
        </div>
        """,
        unsafe_allow_html=True)
    
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
            Creación de gráficos en de densidad con el suavizado de Kernel para la velocidad media por carrera desde el año 2000. 
            En la segunda gráfica se desglosa en tres categorías (categoría reina, segunda categoría y tercera categoría).
            </p>
        </div>
        """,
        unsafe_allow_html=True)    
    
    st.write("")

    st.image('img/velocidad.jpg', use_column_width=True)
    
    st.write("")

    st.image('img/velocidad_3_jorobas.jpg', use_column_width=True)
    
    st.write("")

    st.image('img/cilindradas_antiguas.jpg', use_column_width=True)
    
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
    
    st.image('img/los_4_fantasticos.jpg', use_column_width=True)

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
    


elif page == "Temporadas":
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Análisis de temporadas 2006-2010</h2>
            <p style="text-indent: 1em;"> En este apartado se analizan las <b>temporadas 2006-2010</b>, que han sido solicitadas por nuestros seguidores en la encuesta de la semana pasada. 
            </p>
            <p style="text-indent: 1em;"> Se ha creado un linechart para cada uno de los años con Plotly Express que muestra la de las puntuaciones de los 10 mejores pilotos de una temporada. Este tipo de
            gráficas nos permite detectar patrones de manera sencilla e interpretar correctamente los aspectos más importantes que sucedieron en ese año (además de tirar de la memoria que muchos
            de los aficionados poseemos).
            </p>
            <h3 style="text-indent: 1em;">Contextualización</h3>
            <p style="text-indent: 1em;"> En el período 2005 - 2009 se produjo un cambio de paradigma en la categoría reina de motociclismo. Se venía de 5 títulos consecutivos de 
            Valentino Rossi y de un dominio apabullante del piloto transalpino. Sin embargo, una floja temporada 2006 del italiano aunada a la irrupción de tres jóvenes pilotos que tenían
            un estilo de pilotaje innovador, nos trajeron de nuevo unos campeonatos emocionantes en los que se alternaban las victorias el mismo grupo de corredores:
            <ul style="text-indent: 1em;">
                <li> Valentino Rossi #46
                <li> Casey Stoner #27
                <li> Dani Pedrosa #26
                <li> Jorge Lorenzo #48 y #99
            </ul>
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
            </p>
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

    st.image('img/2009.jpg', use_column_width=True)

    st.write("")

    st.image('img/2010.jpg', use_column_width=True)



elif page == "Test de Hipótesis":
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Realización de varios test de hipótesis</h2>
            <p style="text-indent: 1em;"> En este apartado se analizan test de contraste de hipótesis para determinar si:
            <ul style="text-indent: 1em;">
                <li> La velocidad media ha ido aumentando a lo largo de los años
                <li> Los pilotos españoles rinden mejor en sus circuitos que en el resto 
            </ul>
            <h3 style="text-indent: 1em;">Prueba de regresión lineal ordinaria</h3>
            <p style="text-indent: 1em;"> Para el primer test se realizará una regresión lineal simple y se comprobarán los p-valores de los coeficientes beta de la regresión. Para el segundo caso se
            hará la prueba de Mann-Whitney:<p/>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    st.markdown(
    """
    <div style="background-color: white; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
        </p>
        <p style="text-indent: 1em;"> Aquí tenemos el primer contraste de hipótesis.
        </p>
        <table style="border-collapse: collapse; margin: 25px 0; font-size: 0.9em; font-family: Arial, sans-serif; min-width: 400px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); width: 100%;">
            <thead>
                <tr style="background-color: #009879; color: #ffffff; text-align: left;">
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;"></td>
                    <th style="border: 1px solid #dddddd; text-align: center; padding: 8px;">coef</th>
                    <th style="border: 1px solid #dddddd; text-align: center; padding: 8px;">std err</th>
                    <th style="border: 1px solid #dddddd; text-align: center; padding: 8px;">t</th>
                    <th style="border: 1px solid #dddddd; text-align: center; padding: 8px;">P&gt;|t|</th>
                    <th style="border: 1px solid #dddddd; text-align: center; padding: 8px;">[0.025</th>
                    <th style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.975]</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #dddddd;">
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">const</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">-902.5730</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">102.599</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">-8.797</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.000</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">-1116.590</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">-688.556</td>
                </tr>
                <tr style="background-color: #f3f3f3; border-bottom: 1px solid #dddddd;">
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">year</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.5275</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.051</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">10.337</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.000</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.421</td>
                    <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">0.634</td>
                </tr>
            </tbody>
        </table>
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown(
    r"""
    <div style="
        background-color: #f9f9f9; 
        border: 2px solid #dcdcdc; 
        border-radius: 8px; 
        padding: 10px; 
        margin: 10px 0;
        text-align: center;">
        <p style="font-size: 18px; color: #333; margin-bottom: 15px;">
        La fórmula del modelo de regresión lineal es:
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

    st.markdown(
        """
        <div style="text-align: center; border-radius: 15px; box-shadow: 0 15 15px rgba(0, 0, 0, 0.2); padding: 10px;">
            <img src="data:image/png;base64,{}" width="250">
        </div>
        """.format(base64.b64encode(open('img/formula.png', "rb").read()).decode()),
        unsafe_allow_html=True
    )

    st.markdown(
    r"""
    <div style="
        background-color: #f9f9f9; 
        border: 2px solid #dcdcdc; 
        border-radius: 8px; 
        padding: 10px; 
        margin: 10px 0;
        text-align: center;">
        <p style="font-size: 18px; color: #333; margin-bottom: 15px;">
        Con nuestros coeficientes, tenemos que:
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center; border-radius: 15px; box-shadow: 0 15 15px rgba(0, 0, 0, 0.2); padding: 10px;">
            <img src="data:image/png;base64,{}" width="250">
        </div>
        """.format(base64.b64encode(open('img/formula_vm.png', "rb").read()).decode()),
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> El modelo predice que cada año la velocidad media en carrera aumenta en 0.5275 km/h.   
            </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    st.image('img/reglin.jpg', use_column_width=True)

    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Pruebas de Mann-Whitney</h3>
            <p style="text-indent: 1em;"> Una pregunta que nos puede surgir a los aficionados es si es cierto aquello de que "corriendo en casa rindes mejor". Podemos comprobar si tal cosa ocurre con nuestros datos haciendo
            un test de contraste de hipótesis. Para ello, seleccionamos una muestra A con todos los resultados de los pilotos españoles y otra muestra B con sólo los resultados de los españoles en los circuitos espeñoles. Se elige hacer
            un test de Mann Whitney porque:
            <ul style="text-indent: 1em;">
                <li> Los datos no se ajustan a una distribución normal.
                <li> Las observaciones se pueden ordenar y son independientes (aunque podrían haber mini-dependencias en los resultados de un piloto concreto). En todo caso, el test más apropiado sigue siendo el de Mann Whitney. 
            </ul>
            <h3 style="text-indent: 1em;">Prueba 1: TODOS LOS PILOTOS ESPAÑOLES</h3>
        </div>
        """,
        unsafe_allow_html=True)

    st.image('img/circ_esp.jpg', use_column_width=True)

    st.write("")

    st.image('img/circ_esp_vio.jpg', use_column_width=True)

    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> p=0.263 </p>
        <p> <b>No podemos rechazar</b> la hipótesis nula. Los pilotos españoles parecen rendir igual en sus circuitos que en el resto. </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> Y qué ocurre si escogemos los resultados de un piloto en concreto? Pues vamos a ver dos ejemplos::
            <ul style="text-indent: 1em;">
                <li> Ejemplo A: Dani Pedrosa
                <li> Ejemplo B: Alvaro Bautista 
            </ul>
            </p>
        </div>
        """,
        unsafe_allow_html=True)  

    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Prueba 2a: DANI PEDROSA</h3>
        </div>
        """,
        unsafe_allow_html=True)  
    
    st.write("")

    st.image('img/circ_pedr_vio.jpg', use_column_width=True)

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> p=0.003 </p>
        <p> <b>Se descarta</b> la hipótesis nula. Dani Pedrosa rinde mejor en los circuitos españoles que en los de fuera. </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Prueba 2b: ALVARO BAUTISTA</h3>
        </div>
        """,
        unsafe_allow_html=True)

    st.write("")

    st.image('img/circ_bau_vio.jpg', use_column_width=True) 

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> p=0.929 </p>
        <p> <b>No podemos rechazar</b> la hipótesis nula. Álvaro Bautista parece rendir igual en los circuitos españoles que en los de fuera. </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")


elif page == "Modelo de Regresión":
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
        <h1 style="font-family: 'Tangerine', sans-serif; color: #112266; margin-right: -17px;">Modelo de aprendizaje: Random Forest Regression</h1> 
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Estimamos el tiempo por vuelta de tu circuito</h2>
            <p style="text-indent: 1em;"> Se ha creado un modelo de regresión Random Forest que permite estimar el tiempo por vuelta en 
            base a los siguientes parámetros. 
            </p>
            <ul style="text-indent: 1em;">
                <li>Longitud del circuito</li>
                <li>Número de curvas</li>
                <li>Número de curvas a izquierda</li>
                <li>Longitud de la recta más larga</li>
                <li>Máxima velocidad en carrera</li>
                <li>Desnivel del circuito</li>
            </ul>
            <p style="text-indent: 1em;"> Introduce los <b>datos de tu circuito</b> y te diremos cuánto tiempo tardarías en dar una vuelta. OJO! Fíjate
            bien en las unidades!
            </p>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    st.write("")
    import joblib
    import datetime
    model = joblib.load('model_RF.pkl')

    st.markdown(
    """
    <style>
        /* Estilizar el contenedor del label del input */
        div[data-testid="stNumberInput"] > label {
            background-color: white;
            padding: 5px 10px; /* Espaciado interno del fondo blanco */
            border-radius: 5px; /* Bordes redondeados */
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1); /* Sombra para destacar */
            display: inline-block; /* Asegura que el fondo blanco sea solo del texto */
        }
    </style>
    """,
    unsafe_allow_html=True
)

    longitud = st.number_input('Longitud del circuito (km)', min_value=0.0, max_value=100.0, value=4.0)
    curvas = st.number_input('Número de curvas', min_value=0, max_value=100, value=10)
    curvas_izq = st.number_input('Número de curvas a izquierda', min_value=0, max_value=100, value=5)
    recta = st.number_input('Longitud de la recta más larga (km)', min_value=0.0, max_value=100.0, value=1.0)
    velocidad = st.number_input('Máxima velocidad en carrera (km/h)', min_value=0, max_value=400, value=300)
    desnivel = st.number_input('Desnivel del circuito (m)', min_value=-1000, max_value=1000, value=0)

    input_data = np.array([longitud, curvas, curvas_izq, recta, velocidad, desnivel]).reshape(1, -1)
    

    if st.button('Predecir'):
        prediction = model.predict(input_data)[0] / 1000
        segundos = prediction
        minutos = int(segundos // 60)  
        segundos_restantes = segundos % 60  
        tiempo_formateado = f"{minutos}:{segundos_restantes:06.3f}"
        st.markdown(
            f"""
            <div style="background-color: white; padding: 10px; border-radius: 5px; text-align: center;">
            <h4><i>Tiempo estimado por vuelta (en min:seg.milésimas):</i></h4>
            <p style="font-size: 24px; font-weight: bold;">{tiempo_formateado}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image('img/flag.png', use_column_width=True)
        

    

