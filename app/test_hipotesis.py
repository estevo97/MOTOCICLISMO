import streamlit as st
import base64

def run():

    st.title("Test de Hipótesis")

    # Sección principal
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h2 style="text-indent: 1em;">Realización de varios test de hipótesis</h2>
            <p style="text-indent: 1em;"> En este apartado se analizan test de contraste de hipótesis para determinar si:
            <ul style="text-indent: 1em;">
                <li> La velocidad media ha ido aumentando a lo largo de los años
                <li> Los pilotos españoles rinden mejor en sus circuitos que en el resto 
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Primer test con tabla
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
            <p style="text-indent: 1em;">
            Aquí tenemos el primer contraste de hipótesis...
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Tabla HTML
    # st.markdown(open("tabla_velocidad.html", "r", encoding="utf8").read(), unsafe_allow_html=True)

    # Fórmula 1
    formula_img = base64.b64encode(open('img/formula.png', "rb").read()).decode()
    st.markdown(
        f"""
        <div style="text-align: center; padding: 10px;">
            <img src="data:image/png;base64,{formula_img}" width="250">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fórmula 2
    formula_vm = base64.b64encode(open('img/formula_vm.png', "rb").read()).decode()
    st.markdown(
        f"""
        <div style="text-align: center; padding: 10px;">
            <img src="data:image/png;base64,{formula_vm}" width="250">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Gráficas
    st.image('img/reglin.jpg', use_container_width=True)
    st.image('img/circ_esp.jpg', use_container_width=True)
    st.image('img/circ_esp_vio.jpg', use_container_width=True)

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> p = 0.263 </p>
            <p><b>No podemos rechazar</b> la hipótesis nula...</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Casos particulares
    st.image('img/circ_pedr_vio.jpg', use_container_width=True)
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> p = 0.003 </p>
            <p><b>Se descarta</b> la hipótesis nula. Dani Pedrosa...</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image('img/circ_bau_vio.jpg', use_container_width=True)
    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <p style="text-indent: 1em;"> p = 0.929 </p>
            <p><b>No podemos rechazar</b> la hipótesis nula. Álvaro Bautista...</p>
        </div>
        """,
        unsafe_allow_html=True
    )