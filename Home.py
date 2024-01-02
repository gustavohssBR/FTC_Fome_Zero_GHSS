import streamlit as st
from PIL import Image

st.set_page_config(
        page_title='Home',
        page_icon='🏠')


image = Image.open('Fome_Zero_logo.png')

st.sidebar.image(image, width=120)
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown("""___""")

st.write('# Alimentando Sonhos, Saciando Vidas: Juntos Rumo ao Fome Zero!')
st.markdown(
    """
    Essa Dashboard foi construido para acopanhar as métricas de crescimento dos Restaurantes por Cidades, Paises e Tipos de Culinárias.
    ### Como utilizar esse Dashboard?
    - Visão Geral:
        - Uma visao Geral DataFrame.
        - E um Mapa com os Restaurantes com as informações do tipo de culinaria, a avaliação e o preço médio para duas pessoas.
    - visão Paises:
        - Os indicadores dos Paises.
    - Visão Cidades:
        - OS indicadores das Cidades.
    - Visão Culinária :
        - Os indicadores das culinárias
        
    ### Ask for Help
    - Meu perfil no LinkedIn
        - www.linkedin.com/in/gustavohenriquedossantoss
    
""")