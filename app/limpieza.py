import streamlit as st

def run(tabla1, tabla2):

    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h1>Limpieza de Datos</h1>

            <h2 style="text-indent: 1em;">Partición del dataset</h2>
            <p style="text-indent: 1em;">
                El dataset original se ha dividido en <b>dos mitades</b>: la primera consta de los datos anteriores al año 2000 y 
                la segunda de los datos de este año en adelante. Nos interesa el dataset con los datos del 2000 en adelante, pero 
                en determinadas partes del trabajo se hará uso de la primera parte o incluso del dataset original.
            </p>

            <p style="text-indent: 1em;">
                La razón del corte es sencilla: los datos anteriores al 2000 presentan más valores faltantes y múltiples categorías 
                distintas a las actuales (125/Moto3, 250/Moto2, 500/MotoGP). Esto dificulta comparar pilotos de épocas antiguas. 
                Un ejemplo claro es <b>Ángel Nieto</b>, que ganó sus 13 títulos entre 50cc y 125cc.
            </p>

            <h2 style="text-indent: 1em;">Tratamiento de Valores Nulos</h2>
            <p style="text-indent: 1em;">En el dataset (2000+), con casi 30000 datos, se encontraron:</p>

            <ul>
                <li><b>Number</b>: más de 5000 nulos → imputados con distribución uniforme (1–99).</li>
                <li><b>Speed</b>: casi 1000 nulos → imputados con la <b>media de esa carrera</b> para su categoría.</li>
                <li><b>Time</b>: 1 nulo → eliminado por irrelevante.</li>
            </ul>

            <h2 style="text-indent: 1em;">Tratamiento de Valores Atípicos</h2>
            <p style="text-indent: 1em;">
                Analizamos la variable <b>speed</b> para identificar outliers:
            </p>
            <ul>
                <li><b>Tabla 1</b>: muy poca desviación estándar y un máximo anormalmente alto.</li>
                <li><b>Tabla 2</b>: grandes saltos entre percentiles extremos → existen outliers claros.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(tabla1)
        st.markdown(
            """
            <div style="background-color: #F2F2F2; padding: 5px; border-radius: 5px; text-align: center">
                <h5>Tabla 1: Descriptiva de la variable speed</h5>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.write(tabla2)
        st.markdown(
            """
            <div style="background-color: #F2F2F2; padding: 5px; border-radius: 5px; text-align: center">
                <h5>Tabla 2: Percentiles de la variable speed</h5>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.image('../img/boxplot_speed.jpg', use_column_width=True)

    st.write("")

    st.markdown(
        """
        <div style="background-color: white; padding: 10px; border-radius: 5px;">
            <h3 style="text-indent: 1em;">Recomendación para modelo de aprendizaje</h3>

            <p style="text-indent: 1em;">
                En la gráfica de caja se observan valores atípicos tanto altos como bajos.
                Los outliers superiores se consideran <b>legítimos</b> porque provienen de circuitos muy rápidos como Phillip Island o Spielberg.
            </p>

            <p style="text-indent: 1em;">
                Los valores atípicos por abajo suelen corresponder a pilotos que han tenido problemas en las primeras vueltas, por lo que
                no representan ritmos competitivos.
            </p>

            <p style="text-indent: 1em;">
                Para un modelo predictivo:
            </p>

            <ul>
                <li>Eliminar los outliers inferiores de <b>speed</b>.</li>
                <li>Realizar <b>encoding</b> y <b>escalado</b> de variables categóricas y numéricas.</li>
                <li>Crear subdatasets por cilindrada si speed es variable dependiente.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")