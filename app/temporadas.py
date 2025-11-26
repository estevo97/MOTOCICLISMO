import streamlit as st

def run():
    st.title("Temporadas")
    st.write("Contenido de la página de inicio")




    
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
                <p style="text-indent: 1em;"> El campeonato 2006, como podemos ver, se caracterizó por 
                </p>
            </div>
            """,
            unsafe_allow_html=True)

    st.image('img/2006.jpg', use_container_width=True)

    st.write("")

    st.markdown(
            """
            <div style="background-color: white; padding: 10px; border-radius: 5px;">
                <h3 style="text-indent: 1em;">Temporada 2007</h3>
                <p style="text-indent: 1em;"> El año 2007 fue el primero de la llamada era de las 800cc, que sustituyó a las 990cc. Se caracterizó por
            el dominio de <b>Casey Stoner</b> ya desde la primera carrera.  
                </p>
            </div>
            """,
            unsafe_allow_html=True)

    st.image('img/2007.jpg', use_container_width=True)

    st.write("")

    st.markdown(
            """
            <div style="background-color: white; padding: 10px; border-radius: 5px;">
                <h3 style="text-indent: 1em;">Temporada 2007</h3>
                <p style="text-indent: 1em;"> En el año 2008 debutó el mallorquín <b>Jorge Lorenzo</b> como compañero de equipo de Valentino Rossi.
            Este año consistió en una lucha cuerpo a cuerpo entre Stoner y Rossi, que tuvo su climax durante el Gran Premio de Laguna Seca, donde se recuerda
            el famoso adelantamiento de Rossi a Stoner en la curva de la sacacorchos. No obstante, durante la primera mitad del campeonato el dominio
            fue de Pedrosa, que pese a contar con tan sólo dos victorias era el más regular. En el Gran Premio de Alemania, con la pista mojada y con Pedrosa de
            cabalgando hacia la victoria, una mala caída en la curva 1 le destrozó el hombro y su lucha por el título mundial se esfumó.   
                </p>
            </div>
            """,
            unsafe_allow_html=True)

    st.image('img/2008.jpg', use_container_width=True)

    st.write("")

    st.image('img/2009.jpg', use_container_width=True)

    st.write("")

    st.image('img/2010.jpg', use_container_width=True)