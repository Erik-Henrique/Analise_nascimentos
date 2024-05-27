import streamlit as st
import importlib

import config 

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Início", "Visualizar os dados", "Mapa de nascimentos", "Análises gráficas"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "Pages.1_Início",
  "Visualizar os dados": "Pages.2_Visualizar_os_dados",
  "Mapa de nascimentos": "Pages.3_Mapa_de_nascimentos",
  "Análises gráficas": "Pages.4_Análises_gráficas"
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()

