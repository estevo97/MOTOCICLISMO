import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Cargar modelo solo una vez
@st.cache_resource
def cargar_modelo():
    return tf.keras.models.load_model("../modelo_adivinar_circuitos2.keras")

modelo = cargar_modelo()

def clasificar_imagenes(img):

    if isinstance(img, dict):
        if "composite" in img:
            img = img["composite"]
        else:
            raise ValueError("El diccionario no contiene la clave 'composite'")

    img_rgb = img

    # Resize
    img_resized = tf.image.resize(img_rgb, (224, 224))

    # Normalización
    img_resized = img_resized.numpy().astype("float32") / 255.0

    # Expand batch
    img_resized = np.expand_dims(img_resized, axis=0)

    predicciones = modelo.predict(img_resized)
    digito_predicho = np.argmax(predicciones)

    class_names = ['montmelo', 'monza', 'silverstone', 'spa']
    return class_names[digito_predicho]

def run():

    st.title("Clasificación de Circuitos")
    st.write("Dibuja un circuito para identificarlo con IA.")

    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 1)",
        stroke_width=3,
        stroke_color="#000000",
        background_color="#FFFFFF",
        height=300,
        width=400,
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:

        img_array = canvas_result.image_data.astype("uint8")
        st.image(img_array, caption="Tu dibujo", use_column_width=True)

        if st.button("Identificar circuito"):

            img_pil = Image.fromarray(img_array).convert("RGB")
            img_np = np.array(img_pil)

            prediccion = clasificar_imagenes(img_np)

            st.success(f"El circuito identificado es: **{prediccion}**")