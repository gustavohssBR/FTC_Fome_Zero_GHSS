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
import altair as alt

st.set_page_config( page_title='Visão Culinária', page_icon='🍟', layout='wide' )


#FUNÇÕES


def piores_culinarias(dff):
    """ 
    Essa função tem a responsabilidade de plotar um grafico de barras com as piores culinarias.
    1. agrupando a avaliação media por culinaria e pegar o primeiro ponto de preço . 
    2. e ordenando para pegar as 10 culinária com a menor avaliação.
    3. e criar um grafico de barras com as 10 cidade com a mmenor avaliaçao e diferenciar as culinaria pela preço.
    
    Input: Dataframe
    Output: grafico de barras
    """
    df_aux = (df.loc[:,['aggregate_rating','country_code', 'cuisines',]]
                    .groupby([ 'cuisines'])
                    .agg({'aggregate_rating':'mean','country_code':'first'})
                    .reset_index())
    df_aux = df_aux.sort_values(by='aggregate_rating', ascending=True).reset_index(drop=True)
    df_aux = df_aux.head(quant_restaura)
    fig = px.bar(df_aux, x='cuisines', y ='aggregate_rating',color='country_code')
    return fig

def melhores_culinarias(dff):
    """ 
    Essa função tem a responsabilidade de plotar um grafico de barras com as melhores culinarias.
    1. agrupando a avaliação media por culinaria e pegar o primeiro ponto de preço . 
    2. e ordenando para pegar as 10 culinária com a maior avaliação.
    3. e criar um grafico de barras com as 10 cidade com a maior avaliaçao e diferenciar as culinaria pela preço.
    
    Input: Dataframe
    Output: grafico de barras
    """
    df_aux = (df.loc[:,['aggregate_rating', 'cuisines','country_code']]
                    .groupby([ 'cuisines' ])
                    .agg({'aggregate_rating':'mean', 'country_code':'first'})
                    .reset_index())
    df_aux = df_aux.sort_values(by='aggregate_rating', ascending=False).reset_index(drop=True)
    df_aux = df_aux.head(quant_restaura)
    fig = px.bar(df_aux, x='cuisines', y ='aggregate_rating',color='country_code')
    
    return fig

def top_restaurante(df):
    """ 
    Essa função tem a responsabilidade de retornar os 10 melhores restaurantes.
    1. agrupando os restaurantes unicas pelas cidades, pais, culinaria, valor para duas pessoas, quantidade de avaliações por restaurante e a media da avaliação por restaurante. 
    2. e ordenando para pegar as 10 cidade com as maiores medias das avaliações.
    
    Input: Dataframe
    Output: Dataframe
    """
    dff = df[['restaurant_id', 'restaurant_name', 'country_code', 'city', 'cuisines', 'valor_duas_pessoas',  'aggregate_rating', 'votes']]
    df_aux = dff.groupby('restaurant_id').agg({ 'restaurant_name':'first',
                                                'country_code':'first',
                                                'city':'first',
                                                'cuisines':'first' ,
                                                'valor_duas_pessoas':'first' ,
                                                'aggregate_rating':'mean',
                                                'votes':'first'}).reset_index()
    df_aux = df_aux.sort_values(by='aggregate_rating', ascending=False).reset_index(drop=True)
    df_aux = df_aux.head(quant_restaura)
    return df_aux

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
st.header('Marketplace - Visão Culinária')

image_path = "Fome_Zero_logo.png"
image = Image.open(image_path)
st.sidebar.image(image, width=120)


st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('#### Alimentando Sonhos, Saciando Vidas: Juntos Rumo ao Fome Zero!')
st.sidebar.markdown("""___""")
st.sidebar.markdown('## Filtros')


paises_options=st.sidebar.multiselect(
    'Filtro de Países',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'] ,
    default=['Brazil', 'India', 'United States of America',
       'Canada', 'England'] )

quant_restaura = st.sidebar.slider("Selecione a quantidade de Restaurantes que deseja visualizar",  1, 20, 10)

culinarias_options = st.sidebar.multiselect(
    'Filtro de Culinárias',
    ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'California', 'Others',
       'Eastern European', 'Creole', 'Ramen', 'Ukrainian', 'Hawaiian',
       'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan',
       'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian',
       'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Afghan', 'Lucknowi', 'Charcoal Chicken', 'Mangalorean',
       'Egyptian', 'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian',
       'Western', 'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'] ,
    default=['Italian', 'American',  'Pizza', 'Japanese',
             'Brazilian', 'Arabian', 'Home-made'] )

st.sidebar.markdown("""___""")
st.sidebar.markdown('Powered by Comunidade DS')

linhas_selecionadas = df['country_code'].isin( paises_options )
dfpa = df.loc[linhas_selecionadas, :]

linhas_selecionadas = dfpa['cuisines'].isin( culinarias_options )
dfcu = dfpa.loc[linhas_selecionadas, :]

#=========================================
#Layout no Streamlit
#=========================================

with st.container():
    st.header( 'Melhores Restaurantes dos Principais tipos Culinários' )
    dff = dfcu[['restaurant_id','aggregate_rating', 'restaurant_name', 'cuisines', 'valor_duas_pessoas', 'city', 'country_code']]
    df_aux = dff.groupby('restaurant_id').agg({ 'restaurant_name':'first',
                                                'country_code':'first',
                                                'city':'first',
                                                'cuisines':'first' ,
                                                'valor_duas_pessoas':'first' ,
                                                'aggregate_rating':'mean'  }).reset_index()

    df_aux = df_aux.sort_values(by='aggregate_rating', ascending=False).reset_index(drop=True)
    df_aux = df_aux.head(5)

    # Exibindo os valores inteiros usando st.columns e adicionando tooltips
    columns = st.columns(len(df_aux))
    for index, column in enumerate(columns):
        help_text = f'Pais: {df_aux["country_code"][index]}\n\n'
        help_text += f'cidade: {df_aux["city"][index]}\n\n'
        help_text += f'Preço: {df_aux["valor_duas_pessoas"][index]}\n'
        column.metric(label =f"{df_aux['cuisines'][index]} : {df_aux['restaurant_name'][index]}" ,
                      value=f'{df_aux["aggregate_rating"][index]} / 5.0'  ,
                      help = help_text)


with st.container():    
    st.header(f'Top {quant_restaura} Restaurantes' )
    df_aux = top_restaurante(dfcu)
    st.dataframe(df_aux)
    

    

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header(f'Top {quant_restaura} Melhores tipos de Culinárias')
        fig = melhores_culinarias(dfpa)
        st.plotly_chart(fig, use_container_width = True)
    
    with col2:
        st.header(f'Top {quant_restaura} Piores tipos de Culinárias')
        fig = piores_culinarias(dfpa)
        st.plotly_chart(fig, use_container_width = True)




# a forma de rodar o python no terminal
##__ python Culinaria.py __##
# a forma de rodar o streanlit no terminal
##__ streamlit run Culinaria.py __##
# ver todos os itens que tem na pasta
##__ ls __##
