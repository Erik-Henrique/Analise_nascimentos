import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importlib

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Visualizar os dados", "Mapa de nascimentos", "Análises gráficas"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Visualizar os dados": "Pages.1_Visualizar_os_dados",
  "Mapa de nascimentos": "Pages.2_Mapa_de_nascimentos",
  "Análises gráficas": "Pages.3_Análises_gráficas"
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()

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

st.write("# Bem vindo ao SINASC RONDÔNIA (Sistema de Informação sobre Nascidos Vivos) de 2019 👋")

st.write('''#### Este é um Web App contendo uma análise detalhada de vários dados sobre os nascimentos que aconteceram no estado de Rondônia no ano de 2019.''')

st.markdown(
    """
    **👈 Na barra lateral você pode selecionar a análise que deseja ver**
    ### Quer saber mais sobre o estado de Rondônia?
    - Confira o [Site oficial do estado](https://www.ro.gov.br/)
    - Confira os [Dados do Wikipedia](https://pt.wikipedia.org/wiki/Rond%C3%B4nia)
    - Confira os [Dados do IBGE](https://cidades.ibge.gov.br/brasil/ro/historico)
    - Confira algumas [Curiosidades de Rondônia](https://www.youtube.com/watch?v=dg-MXs6M8gk)
"""
)
