import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',
                   page_title='SINASC RONDÔNIA',
                   page_icon='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Bras%C3%A3o_de_Rond%C3%B4nia.svg/1200px-Bras%C3%A3o_de_Rond%C3%B4nia.svg.png')

# Carregando o data frame
DATE_COLUMN = 'dtnasc'
DATA_URL = (r"C:\Users\erikd\OneDrive\Área de Trabalho\Scripts Python\EBAC\Cientista de dados\Modulo 16 - Streamlit\input_M15_SINASC_RO_2019.csv")
# Adicionando o data frame a uma variável
data = pd.read_csv(DATA_URL)
lowercase = lambda x: str(x).lower()
data.rename(lowercase, axis='columns', inplace=True)
data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

# Gerador de mapa com local de nascimentos 
st.title('Cidade de nascimento')
st.write('''#### Selecione abaixo o dia que deseja ver os locais de nascimento''')   
hour_to_filter = st.slider('Selecione o dia', 1, 31, 1)  
filtered_data = data[data[DATE_COLUMN].dt.day == hour_to_filter]
st.subheader(f'Locais onde houveram nascimentos no dia {hour_to_filter}')
st.map(filtered_data)