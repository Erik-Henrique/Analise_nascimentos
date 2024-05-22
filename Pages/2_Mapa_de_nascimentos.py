import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def app():
  st.set_page_config(layout='wide',
                     page_title='SINASC RONDÔNIA',
                     page_icon='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Bras%C3%A3o_de_Rond%C3%B4nia.svg/1200px-Bras%C3%A3o_de_Rond%C3%B4nia.svg.png')
  
  page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://scontent-gru1-1.xx.fbcdn.net/v/t39.30808-6/291779830_105699482202577_6654195867880689942_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFmWDx72lVg_Xqax3nN15UAM7OA3lH5H_czs4DeUfkf93MF8MNtwes4i-94OtkabFUcBhgc2icdjFNl0_a83aOR&_nc_ohc=7LpSckNKdsoQ7kNvgF7eG5B&_nc_ht=scontent-gru1-1.xx&oh=00_AYB3PEuRb6OtaU79IjMzaFMdP4Ko3GJ7j2MvUiRfTsAElA&oe=66516BCB");
    background-size: cover;
    }
    [data-testid="stSidebarContent"] {
    background-image: url("https://scontent-gru1-1.xx.fbcdn.net/v/t39.30808-6/291779830_105699482202577_6654195867880689942_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFmWDx72lVg_Xqax3nN15UAM7OA3lH5H_czs4DeUfkf93MF8MNtwes4i-94OtkabFUcBhgc2icdjFNl0_a83aOR&_nc_ohc=7LpSckNKdsoQ7kNvgF7eG5B&_nc_ht=scontent-gru1-1.xx&oh=00_AYB3PEuRb6OtaU79IjMzaFMdP4Ko3GJ7j2MvUiRfTsAElA&oe=66516BCB");
    background-size: cover;
    }
    [data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
    }
    </style>
    """
  st.markdown(page_bg_img, unsafe_allow_html=True)
  
  
  # Carregando o data frame
  DATE_COLUMN = 'dtnasc'
  DATA_URL = (r"C:\Users\erikd\OneDrive\Área de Trabalho\Streamlit\Atividade\input_M15_SINASC_RO_2019.csv")
  # Adicionando o data frame a uma variável
  data = pd.read_csv(DATA_URL)
  data.drop(1863, axis=0, inplace=True)
  data.reset_index(drop=True)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  
  # Gerador de mapa com local de nascimentos 
  st.title('Cidade de nascimento')
  st.write('''#### Selecione abaixo a data para ver os locais onde houveram nascimentos:''')  
  d = st.date_input("#", value = datetime.date(2019, 1, 1), min_value= datetime.date(2019,1,1), max_value= datetime.date(2019,12,31), format= "DD/MM/YYYY")
  filtered_data = data[data[DATE_COLUMN].dt.day == d.day]
  st.subheader(f'Locais onde houveram nascimentos na data {d.day}-{d.month}-{d.year}')
  st.map(filtered_data)
