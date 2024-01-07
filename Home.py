#Bibliotecas 
import pandas as pd
import numpy as np
import inflection
import streamlit as st
from streamlit_folium import folium_static
from PIL import Image
import folium
from folium.plugins import MarkerCluster

st.set_page_config(
        page_title='Home',
        page_icon='🏠')

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
    df['average_cost_for_two'] = df['average_cost_for_two'].astype(str)

    # Fundir as colunas em uma nova coluna
    df['valor_duas_pessoas'] = df['average_cost_for_two'] + df['moeda']
    
    # CRIANDO UMA COLUNA COM AS LISTA DOS TIPOS DE CULINARIAS
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    return df

#df = Limpeza_dados(df_)

# FUNÇAO PARA CONVERTER AS MOEDAS PARA DOLLAR
#def converter_para_dolar(moeda, valor):
    #currency_rates = CurrencyRates()
    #return currency_rates.convert(moeda, 'USD', valor)

# Aplicar a função de conversão a cada linha do DataFrame usando apply e lambda
#df['Valor_em_USD'] = df.apply(lambda row: converter_para_dolar(row['moeda'], row['average_cost_for_two']), axis=1)

## CONVERTER A COLUNA DE VAOLOR MEDIO PARA DUAS PESSOAS PARA DOLAR
#nome_do_arquivo = 'dados.csv'
#df.to_csv(nome_do_arquivo, index=False)
#from IPython.display import FileLink
# Criando um link de download para o arquivo CSV
#display(FileLink(nome_do_arquivo))

def limpeza_extra(df):
    df['Valor_em_USD'] = df['Valor_em_USD'].round(2)
    df['average_cost_for_two_str'] = df['Valor_em_USD'].astype(str)
    # Fundir as colunas em uma nova coluna
    df['valor_duas_pessoas'] = df['average_cost_for_two_str'] + df['moeda']
    return df

#COLETA DE DADOS
df_ = pd.read_csv(r'./dataset/dados.csv')
#df_ = pd.read_csv(r'../dataset/dados.csv')

df = limpeza_extra(df_)

image = Image.open('Fome_Zero_logo.png')

st.sidebar.image(image, width=120)
st.sidebar.markdown('# Fome Zero')


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


#st.sidebar.markdown('### Download dos dados tratados')
#st.sidebar.download_button(
#    label="Download",
#    data=csv,
#    file_name='large_df.csv',
#    mime='text/csv',)
    




st.sidebar.markdown("""___""")

st.write('# Fome Zero!')
st.write('## Alimentando Sonhos, Saciando Vidas: Juntos Rumo ao Fome Zero!')
st.markdown(
    """
    Essa Dashboard foi construido para acopanhar as métricas de crescimento dos Restaurantes por Cidades, Paises e Tipos de Culinárias.
    ### Como utilizar esse Dashboard?
    - Visão Geral:
        - Uma visao Geral DataFrame.
        - E um Mapa com os Restaurantes com as informações do tipo de culinaria, a avaliação e o preço médio para duas pessoas.
    - visão Paises:
        - Os indicadores dos Restaurantes.
    - Visão Cidades:
        - OS indicadores das Cidades.
    - Visão Culinária :
        - Os indicadores das culinárias
        
    ### Ask for Help
    - Meu perfil no LinkedIn
        - www.linkedin.com/in/gustavohenriquedossantoss
    
""")
csv = convert_df(df)
st.markdown('### Download dos dados tratados')
st.download_button(
    label="Download",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)
