#Bibliotecas 
import pandas as pd
import numpy as np
import inflection
import streamlit as st
from streamlit_folium import folium_static
from PIL import Image
import folium
from folium.plugins import MarkerCluster
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config( page_title='Visão Paises', page_icon='🌎', layout='wide' )

#FUNÇÕES 
def valor_pessoa_paises(df):
    """ 
    Essa função tem a responsabilidade de plotar um grafico de barras .
    1. utilizando as colunas de latitude e longitude para encoratrar a localizaçao dos restaurantes. 
    2. a coluna de rating_color para diferenciar a cor dos icon do restaurante por avaliações.
    3. e utilizar a função de icon com a variavel glyphicon-home para que a localização tenha o simbolo de uma casa.
    4. e usar a funçao popup_content para colocar informações extras quando passar encima da localização.
   
    Input: Dataframe
    Output: Grafico de Barras
    """
    df_aux = df.groupby('country_code').agg({'average_cost_for_two':'mean',
                                 'moeda':'first'  }).reset_index()
    df_aux = df_aux.sort_values(by='average_cost_for_two',ascending=False ).reset_index(drop=True)
    fig = px.bar(df_aux, x='country_code',y='average_cost_for_two',color='moeda')
    return fig

#LIMPEZA DE DADOS
# Função para encontrar duas string desejadas em cada lista de um Dataframe
def encontrar_duas_palavras(lista, string1, string2):
    for i in lista:
        for j in lista:
            if string1 in i: 
                return string1 
            elif string2 in j:
                return string2
    return 'NaN'

# Função para encontrar a string desejada em cada lista de um Dataframe
def encontrar_palavras(dflista, string):
    for i in dflista:
        if string in i:
            return i
    return 'NaN'


def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df


def Limpeza_dados(df_):
    df = df_.copy()
    #Dropando a coluna possui somente uma variável 
    # uma coluna com um unico valor 
    df = df.drop(columns='Switch to order menu' )
    
    df = rename_columns(df)
  
    #LIMPEZA DE VALRES FALTANTES:
    df = df.dropna(how='any',axis=0) 

    # LINPEZA DE VALORES DUPLICADOS
    #marcado como false e true valores duplicados marcando como true todos os valores duplicados menos o primeiro valor que possui uma copia
    data_duplicate = df.duplicated(keep = 'first')
    #retirando os dados duplicados que sao os Trues e deixado somente os dados False 
    #o (~) e para inplementar os dados False sem ele vem os dados True
    df = df[~data_duplicate]
    # resetando o index
    df = df.reset_index(drop = True)
    
    #PREENCHIMENTO DO NOME DOS PAISE
    COUNTRIES = { 1: "India",
                  14: "Australia",
                  30: "Brazil",
                  37: "Canada",
                  94: "Indonesia",
                  148: "New Zeland",
                  162: "Philippines",
                  166: "Qatar",
                  184: "Singapure",
                  189: "South Africa",
                  191: "Sri Lanka",
                  208: "Turkey",
                  214: "United Arab Emirates",
                  215: "England",
                  216: "United States of America",}
    df['country_code'] = df['country_code'].map(COUNTRIES)
    
    #CRIAÇÃO DO TIPO DE CATEGORIA DE COMIDA
    category = { 1:'cheap', 2:'normal', 3:'expensive', 4:'gourmet'}
    df['price_type'] = df['price_range'].map(category)
    
    #CRIAÇÃO DO NOME DAS CORES
    COLORS = {"3F7E00": "darkgreen",
              "5BA829": "green",
              "9ACD32": "lightgreen",
              "CDD614": "orange",
              "FFBA00": "red",
              "CBCBC8": "darkred",
              "FF7800": "darkred",}

    df['rating_color'] = df['rating_color'].map(COLORS)
    
    COUNTRIES = { 'India':'(INR)',
                  'Australia':'(AUD)',
                  'Brazil':'reis(R$)',
                  'Canada':'(CAD)',
                  'Indonesia':'Rupia(Rp)',
                  'New Zeland':'(NZD)',
                  'Philippines':'(₱)',
                  'Qatar':'Rial(QAR)',
                  'Singapure':'(SGD)',
                  'South Africa':'rands(ZAR)',
                  'Sri Lanka':'(LKR)',
                  'Turkey':'Lira(₺)',
                  'United Arab Emirates':'(AED)',
                  'England':'Libra(£)',
                  'United States of America':'Dollar($)'}
    df['moeda'] = df['country_code'].map(COUNTRIES)
    df['average_cost_for_two_str'] = df['average_cost_for_two'].astype(str)

    # Fundir as colunas em uma nova coluna
    df['valor_duas_pessoas'] = df['average_cost_for_two_str'] + df['moeda']
    
    # CRIANDO UMA COLUNA COM AS LISTA DOS TIPOS DE CULINARIAS
    #Divida as strings em torno do separador que e o , delimitador fornecido.
    #df['cuisines_distict'] = df['cuisines'].str.split(r', |,')
    #df['unique_cuisines'] = df['cuisines'].apply(lambda x: extrair_primeira_palavra(x))
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])



    
    return df

#COLETA DE DADOS
df_ = pd.read_csv(r'./dataset/zomato.csv')
#df_ = pd.read_csv(r'../dataset/zomato.csv')

df = Limpeza_dados(df_)

#forma de printar o as informações no terminal 
#python Paises.py

#=========================================
#Barra lateral
#=========================================
st.header('Marketplace - Visão Pais')

image_path = "Fome_Zero_logo.png"
image = Image.open(image_path)
st.sidebar.image(image, width=120)


st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('#### Alimentando Sonhos, Saciando Vidas: Juntos Rumo ao Fome Zero!')
st.sidebar.markdown("""___""")
st.sidebar.markdown('## Filtros')


traffic_options=st.sidebar.multiselect(
    'Quais as condições do trânsito',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'] ,
    default=['Brazil', 'United States of America', 'India',
       'Canada', 'England'] )

st.sidebar.markdown("""___""")
st.sidebar.markdown('Powered by Comunidade DS')

linhas_selecionadas = df['country_code'].isin( traffic_options )
df = df.loc[linhas_selecionadas, :]

#=========================================
#Layout no Streamlit
#=========================================
with st.container():
    st.markdown('## valor medio para duas pessoas por Paises ')
    fig = valor_pessoa_paises(df)
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('## quantidade de culinárias por paises ')
        df_aux = df.loc[:,['country_code', 'cuisines']].groupby([ 'country_code' ]).nunique().reset_index()
        fig = px.bar(df_aux, x='country_code',y='cuisines')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown('## quantidade de cidade por paises ')
        df_axc = df.loc[:, [ 'country_code','city' ] ].groupby([ 'country_code']).nunique().reset_index()
        fig = px.bar(df_axc, x='country_code', y ='city')
        st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Media de quantidade de avaliações por paises')
        df_aux = df.loc[:,['country_code','votes']].groupby(['country_code']).mean().reset_index()
        fig = px.bar(df_aux, x='country_code', y='votes')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.header('restaurantes com o nível de preço igual a 4 ')
        df_aux = df.loc[:, [ 'country_code', 'price_range', 'restaurant_id' ] ].groupby([ 'country_code','price_range']).nunique().reset_index()
        df_aux = df_aux.loc[df_aux['price_range'] == 4]
        fig = px.bar(df_aux, x='country_code',y='restaurant_id')
        st.plotly_chart(fig, use_container_width=True)

        
    
    
