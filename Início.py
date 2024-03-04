import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',
                   page_title='SINASC RONDÔNIA',
                   page_icon='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Bras%C3%A3o_de_Rond%C3%B4nia.svg/1200px-Bras%C3%A3o_de_Rond%C3%B4nia.svg.png')

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
