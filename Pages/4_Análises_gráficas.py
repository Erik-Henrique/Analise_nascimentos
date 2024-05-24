import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

def app():
# 
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
  DATA_URL = (r"https://raw.githubusercontent.com/Erik-Henrique/Analise_nascimentos/main/input_M15_SINASC_RO_2019.csv")
  # Adicionando o data frame a uma variável
  data = pd.read_csv(DATA_URL)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  
  st.write('''## Análises gráficas pré-definidas''')
  
  seleção = st.selectbox(
      'Selecione a análise desejada:',
      ('Média da idade da mãe e do pai ao longo do tempo', 'Média da idade da mãe ao longo do tempo', 'Média da idade da mãe pela escolaridade', 'Média da idade da pai pela escolaridade', 'Média da idade do pai ao longo do tempo', 'Média da idade da mãe e o tipo de parto',
       'Quantidade de nascimentos por dia ao longo do tempo', 'Quantidade de nascimentos por sexo ao longo do tempo',
       'Média de peso dos bebês por sexo ao longo do tempo', 'Média peso pela escolaridade da mãe', 'APGAR1 pelo tempo de gestação', 'APGAR5 pelo tempo de gestação'), 
       index = None, placeholder= 'Clique aqui para selecionar a análise desejada')
  
  # Gerador de Gráficos 
  def gerador_grafico(data,value,index,func,ylabel,xlabel,opcao='nada'):
        if opcao == 'nada':
          pd.pivot_table(data= data, values= value, index= index,
                         aggfunc= func).plot(figsize=[18,6])
        elif opcao == 'unstack':
          pd.pivot_table(data= data, values= value, index= index,
                         aggfunc= func).unstack().plot(figsize=[18,6])
        elif opcao == 'sort':
          pd.pivot_table(data= data, values= value, index= index,
                         aggfunc= func).sort_values(value).plot(figsize=[18,6])
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        st.pyplot(fig=plt)
  
  # Seleção dos gráficos
  if seleção == 'Média da idade da mãe e do pai ao longo do tempo':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                value= data_min,
                                min_value=data_min,
                                max_value=data_max)
         data_final = st.date_input('Data final',
                               value= data_max,
                               min_value=data_min,
                               max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, ['idademae','idadepai'], 'dtnasc', 'mean', 'média idade mãe e pai', 'data de nascimento')
  
  if seleção == 'Média da idade da mãe ao longo do tempo':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                value= data_min,
                                min_value=data_min,
                                max_value=data_max)
         data_final = st.date_input('Data final',
                               value= data_max,
                               min_value=data_min,
                               max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idademae', 'dtnasc', 'mean', 'média idade mãe', 'data de nascimento')
  
  if seleção == 'Média da idade da mãe e o tipo de parto':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                value= data_min,
                                min_value=data_min,
                                max_value=data_max)
         data_final = st.date_input('Data final',
                               value= data_max,
                               min_value=data_min,
                               max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idademae', 'parto', 'mean', 'média idade mãe', 'data de nascimento')
  
  if seleção == 'Média da idade da mãe pela escolaridade':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                value= data_min,
                                min_value=data_min,
                                max_value=data_max)
         data_final = st.date_input('Data final',
                               value= data_max,
                               min_value=data_min,
                               max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idademae', 'escmae', 'mean', 'média idade mãe', 'escolaridade')
  
  if seleção == 'Média da idade da pai pela escolaridade':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                value= data_min,
                                min_value=data_min,
                                max_value=data_max)
         data_final = st.date_input('Data final',
                               value= data_max,
                               min_value=data_min,
                               max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idadepai', 'escmae', 'mean', 'média idade pai', 'escolaridade')
  
  if seleção == 'Média da idade do pai ao longo do tempo':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                value= data_min,
                                min_value=data_min,
                                max_value=data_max)
         data_final = st.date_input('Data final',
                               value= data_max,
                               min_value=data_min,
                               max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idadepai', 'dtnasc', 'mean', 'média idade pai', 'data de nascimento')
  
  elif seleção == 'Quantidade de nascimentos por dia ao longo do tempo':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                      value= data_min,
                                      min_value=data_min,
                                      max_value=data_max)
         data_final = st.date_input('Data final',
                                      value= data_max,
                                      min_value=data_min,
                                      max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idademae', 'dtnasc', 'count', 'quantidade de nascimentos', 'data de nascimento')
  
  elif seleção == 'Quantidade de nascimentos por sexo ao longo do tempo':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                      value= data_min,
                                      min_value=data_min,
                                      max_value=data_max)
         data_final = st.date_input('Data final',
                                      value= data_max,
                                      min_value=data_min,
                                      max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'idademae', ['dtnasc', 'sexo'], 'count', 'quantidade de nascimentos', 'data de nascimento', opcao= 'unstack')
  
  elif seleção == 'Média de peso dos bebês por sexo ao longo do tempo':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                      value= data_min,
                                      min_value=data_min,
                                      max_value=data_max)
         data_final = st.date_input('Data final',
                                      value= data_max,
                                      min_value=data_min,
                                      max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'peso', ['dtnasc', 'sexo'], 'mean', 'média de peso dos bebes', 'data de nascimento', opcao= 'unstack')
  
  elif seleção == 'Média peso pela escolaridade da mãe':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                      value= data_min,
                                      min_value=data_min,
                                      max_value=data_max)
         data_final = st.date_input('Data final',
                                      value= data_max,
                                      min_value=data_min,
                                      max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'peso', 'escmae', 'mean', 'média de peso dos bebes', 'escolaridade da mãe', opcao= 'sort')
          
  elif seleção == 'APGAR1 pelo tempo de gestação':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                      value= data_min,
                                      min_value=data_min,
                                      max_value=data_max)
         data_final = st.date_input('Data final',
                                      value= data_max,
                                      min_value=data_min,
                                      max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'apgar1', ['gestacao'], 'mean', 'APGAR1 médio', 'tempo de gestação', opcao= 'sort')
      
  elif seleção == 'APGAR5 pelo tempo de gestação':
         data_min = data['dtnasc'].min()
         data_max = data['dtnasc'].max()
  
         datas = data.dtnasc.unique()
  
         data_inicial = st.date_input('Data inicial',
                                      value= data_min,
                                      min_value=data_min,
                                      max_value=data_max)
         data_final = st.date_input('Data final',
                                      value= data_max,
                                      min_value=data_min,
                                      max_value=data_max)
  
  
         sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]
  
         gerador_grafico(sinasc, 'apgar5', ['gestacao'], 'mean', 'APGAR5 médio', 'tempo de gestação', opcao= 'sort')
  
  
  st.write('''## Crie suas análises gráficas''')
  
  seleção_4 = st.selectbox(
                'Selecione a função a ser aplicada na análise:',
                ('Contagem da quantidade de bebês','Média','Mediana', ), 
                index = None, placeholder= 'Clique aqui para selecionar a variável desejada')
  
  if seleção_4 == 'Contagem da quantidade de bebês':
         seleção_2 = 'idademae'
  else:
         seleção_2 = st.selectbox(
                       'Selecione a 1° variável:',
                       ('peso', 'idademae', 'idadepai'), 
                       index = None, placeholder= 'Clique aqui para selecionar a variável desejada')
         if seleção_2 == 'escolaridade mãe':
                seleção_2 = 'escmae'
  
  if seleção_4 == 'Contagem da quantidade de bebês':
         seleção_3 = st.selectbox(
                'Selecione a 1° variável:',
                ('escolaridade mãe','gestacao','gravidez','data de nascimento', 'sexo', 'apgar1', "apgar5", 'idadepai'), 
                index = None, placeholder= 'Clique aqui para selecionar a variável desejada')
         if seleção_3 == 'escolaridade mãe':
                seleção_3 = 'escmae'
         if seleção_3 == 'data de nascimento':
                seleção_3 = 'dtnasc'
  else:
        seleção_3 = st.selectbox(
                'Selecione a 2° variável:',
                ('escolaridade mãe','idademae','gestacao','gravidez','data de nascimento', 'sexo', 'apgar1', "apgar5", 'idadepai'), 
                index = None, placeholder= 'Clique aqui para selecionar a variável desejada')
  
  if seleção_3 == 'escolaridade mãe':
                seleção_3 = 'escmae'
  if seleção_3 == 'data de nascimento':
                seleção_3 = 'dtnasc'
  
  
  
  
  
  if seleção_4 == 'Contagem da quantidade de bebês':
        seleção_4 = 'count'
  if seleção_4 == 'Média':
        seleção_4 = 'mean'
  if seleção_4 == 'Mediana':
        seleção_4 = 'median'
  
  
  
  if st.button('Visualizar o gráfico'):
         if seleção_4 == None:
               st.write('Por favor, preencha todos os campos acima!')
               sleep(59)
         if seleção_4 == 'count':
                gerador_grafico(data, seleção_2, seleção_3, seleção_4, 'Quantidade de bebês', seleção_3)
         if (seleção_4 == 'mean') & (seleção_2 in ['idademae', 'idadepai']):
                gerador_grafico(data, seleção_2, seleção_3, seleção_4, 'Média da ' + seleção_2, seleção_3)
         if (seleção_4 == 'mean') & (seleção_2 == 'peso'):
                gerador_grafico(data, seleção_2, seleção_3, seleção_4, 'Média do ' + seleção_2, seleção_3)
         if (seleção_4 == 'median') & (seleção_2 in ['idademae', 'idadepai']):
                gerador_grafico(data, seleção_2, seleção_3, seleção_4, 'Mediana da ' + seleção_2, seleção_3)
         if (seleção_4 == 'median') & (seleção_2 == 'peso'):
                gerador_grafico(data, seleção_2, seleção_3, seleção_4, 'Mediana do ' + seleção_2, seleção_3)
