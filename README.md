🏍️🏁 Análisis MotoGP – Proyecto Completo en Streamlit










🚀 Aplicación desplegada

👉 Accede a la app completa en Hugging Face:

🔗 https://huggingface.co/spaces/estevoag/MOTOCICLISMO

La aplicación se ejecuta 100% en la nube e incluye análisis, visualizaciones interactivas y modelos de IA.

🧠 ¿Qué incluye este proyecto?
🔍 1. Limpieza de datos (EDA Preprocessing)

Tratamiento de valores nulos

Corrección de outliers

Normalización de variables

Transformación y filtrado de columnas

📊 2. Análisis Exploratorio (EDA)

Mapas de calor

Gráficas interactivas con Plotly

Distribuciones, correlaciones y estadísticas clave

Comparativas entre pilotos, escuderías y temporadas

🏆 3. Análisis de Temporadas

Evolución de pilotos

Clasificaciones

Ritmos por circuito

Análisis de competitividad entre equipos

🧪 4. Contraste de Hipótesis

¿La pole predice la victoria?

¿Hay circuitos que favorecen estilos de conducción concretos?

Pruebas estadísticas formales con Python

🤖 5. Modelo de Regresión

Modelo predictivo capaz de estimar tiempos de vuelta

Introduce parámetros del circuito y obtiene predicciones

✏️ 6. IA para Reconocimiento de Circuitos

El usuario puede dibujar un circuito y el modelo (TensorFlow + InceptionV3) intenta identificarlo entre varios trazados reales.
Incluye preprocesamiento, normalización y predicción.

📚 7. Sidebar detallado

Explicación de cada parte del proyecto (código, metodología y decisiones).

🧩 Tecnologías principales
Tecnología	Uso
Python 3.10+	Lenguaje principal
Streamlit	Interfaz web
TensorFlow 2.x	Red neuronal para circuitos
NumPy / Pandas	Procesamiento
Seaborn / Matplotlib / Plotly	Visualizaciones
streamlit-drawable-canvas	Dibujo en la app
Hugging Face Spaces	Despliegue
Power BI Embeds	Dashboards conectados
📁 Estructura del proyecto
📂 proyecto/
│── app.py                   # Archivo principal
│── aplicacion.py            # Clasificador IA (canvas)
│── pages/                   # Resto de secciones Streamlit
│── modelos/                 # Modelos TensorFlow (en HF)
│── img/                     # Imágenes y recursos
│── requirements.txt         # Dependencias
│── README.md                # Este archivo

🎯 Objetivo

Este proyecto pretende ofrecer una plataforma completa para analizar MotoGP, combinando:

Ciencia de Datos

IA

Visualización interactiva

Interpretabilidad

Todo accesible desde la web.

👨‍💻 Autor

Estevo Arias García
Proyecto realizado con dedicación, pasión por MotoGP y enfoque académico/divulgativo.



una versión tipo documentación técnica,

o una versión ultra minimalista.

¿Quieres alguno de esos estilos?
