import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importlib
import config 

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Início", "Visualizar os dados", "Mapa de nascimentos", "Análises gráficas"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "Pages.Início",
  "Visualizar os dados": "Pages.1_Visualizar_os_dados",
  "Mapa de nascimentos": "Pages.2_Mapa_de_nascimentos",
  "Análises gráficas": "Pages.3_Análises_gráficas"
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()
