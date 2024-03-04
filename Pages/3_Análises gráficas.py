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

st.write('''## Análises gráficas''')

seleção = st.selectbox(
    'Selecione a análise desejada:',
    ('Contagem da IDADEMAE x Tempo', 'Quantidade de bebês por dia ao longo do tempo', 'Quantidade de bebês meninos e meninas nascidos ao longo do tempo',
     'Média de peso dos bebês meninos e meninas', 'Média peso x Escolaridade mãe', 'APGAR1 pelo tempo de gestação', 'APGAR5 pelo tempo de gestação'), 
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
if seleção == 'Contagem da IDADEMAE x Tempo':
       data_min = data['dtnasc'].min()
       data_max = data['dtnasc'].max()

       datas = data.dtnasc.unique()

       data_inicial = st.date_input('Data inicial',
                              value= data_min,
                              min_value=data_min,
                              max_value=data_max)
       data_final = st.date_input('Data inicial',
                             value= data_max,
                             min_value=data_min,
                             max_value=data_max)


       sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]

       gerador_grafico(sinasc, 'idademae', 'dtnasc', 'mean', 'média idade mãe', 'data de nascimento')

elif seleção == 'Quantidade de bebês por dia ao longo do tempo':
       data_min = data['dtnasc'].min()
       data_max = data['dtnasc'].max()

       datas = data.dtnasc.unique()

       data_inicial = st.date_input('Data inicial',
                                    value= data_min,
                                    min_value=data_min,
                                    max_value=data_max)
       data_final = st.date_input('Data inicial',
                                    value= data_max,
                                    min_value=data_min,
                                    max_value=data_max)


       sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]

       gerador_grafico(sinasc, 'idademae', 'dtnasc', 'count', 'quantidade de nascimentos', 'data de nascimento')

elif seleção == 'Quantidade de bebês meninos e meninas nascidos ao longo do tempo':
       data_min = data['dtnasc'].min()
       data_max = data['dtnasc'].max()

       datas = data.dtnasc.unique()

       data_inicial = st.date_input('Data inicial',
                                    value= data_min,
                                    min_value=data_min,
                                    max_value=data_max)
       data_final = st.date_input('Data inicial',
                                    value= data_max,
                                    min_value=data_min,
                                    max_value=data_max)


       sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]

       gerador_grafico(sinasc, 'idademae', ['dtnasc', 'sexo'], 'count', 'quantidade de nascimentos', 'data de nascimento', opcao= 'unstack')

elif seleção == 'Média de peso dos bebês meninos e meninas':
       data_min = data['dtnasc'].min()
       data_max = data['dtnasc'].max()

       datas = data.dtnasc.unique()

       data_inicial = st.date_input('Data inicial',
                                    value= data_min,
                                    min_value=data_min,
                                    max_value=data_max)
       data_final = st.date_input('Data inicial',
                                    value= data_max,
                                    min_value=data_min,
                                    max_value=data_max)


       sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]

       gerador_grafico(sinasc, 'peso', ['dtnasc', 'sexo'], 'mean', 'média de peso dos bebes', 'data de nascimento', opcao= 'unstack')

elif seleção == 'Média peso x Escolaridade mãe':
       data_min = data['dtnasc'].min()
       data_max = data['dtnasc'].max()

       datas = data.dtnasc.unique()

       data_inicial = st.date_input('Data inicial',
                                    value= data_min,
                                    min_value=data_min,
                                    max_value=data_max)
       data_final = st.date_input('Data inicial',
                                    value= data_max,
                                    min_value=data_min,
                                    max_value=data_max)


       sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]

       gerador_grafico(sinasc, 'peso', ['escmae'], 'mean', 'média de peso dos bebes', 'data de nascimento', opcao= 'sort')
        
elif seleção == 'APGAR1 pelo tempo de gestação':
       data_min = data['dtnasc'].min()
       data_max = data['dtnasc'].max()

       datas = data.dtnasc.unique()

       data_inicial = st.date_input('Data inicial',
                                    value= data_min,
                                    min_value=data_min,
                                    max_value=data_max)
       data_final = st.date_input('Data inicial',
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
       data_final = st.date_input('Data inicial',
                                    value= data_max,
                                    min_value=data_min,
                                    max_value=data_max)


       sinasc = data[(data['dtnasc'] <= pd.to_datetime(data_final)) & (data['dtnasc'] >= pd.to_datetime(data_inicial))]

       gerador_grafico(sinasc, 'apgar5', ['gestacao'], 'mean', 'APGAR5 médio', 'tempo de gestação', opcao= 'sort')