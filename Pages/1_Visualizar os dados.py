import streamlit as st
import pandas as pd

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

st.write('''## Este é o Data Frame usado para realizar as análises, fique a vontade para explora-ló.''')
st.write(' ')

if st.button('Clique aqui para ver apenas o Data Frame original novamente'):
       st.write(data[0:])
else:
       st.write(data[0:])

st.write(' ')
st.write('##### Você pode filtrar o Data Frame, basta indicar o indice inicial e o indice final:') 
st.write(' ')

number1 = st.number_input('Indice inicial')
number2 = st.number_input('Indice final')

if st.button('Visualizar o Data Frame'):
       st.write(data[int(number1):int(number2)+1])




