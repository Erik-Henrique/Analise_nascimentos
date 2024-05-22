import streamlit as st
import pandas as pd

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
  
  st.write('''## Aqui você vai poder explorar o Data Frame da sua forma:''')
  st.write(' ')
  
  
  
  st.write(' ')
  st.write('##### Para visualizar o Data Frame, basta indicar o indice inicial, final e as colunas:') 
  st.write(' ')
  
  number1 = st.number_input('Indice inicial', value = 0)
  number2 = st.number_input('Indice final', value = 27027)
  colunas = st.multiselect('Seletor de colunas',default= 'Todas as variáveis',                   
                                                options=['Todas as variáveis','origem','codestab','codmunnasc','locnasc','idademae','estcivmae','escmae','codocupmae','qtdfilvivo','qtdfilmort','codmunres','gestacao','gravidez','parto','consultas','dtnasc','horanasc','sexo','apgar1',
                                                          'apgar5','racacor','peso','idanomal','dtcadastro','codanomal','numerolote','versaosist','dtrecebim','difdata','dtrecoriga','naturalmae', 'codmunnatu','codufnatu','escmae2010','seriescmae','dtnascmae',
                                                          'racacormae','qtdgestant','qtdpartnor','qtdpartces','idadepai','dtultmenst','semagestac','tpmetestim','consprenat','mesprenat','tpapresent','sttrabpart','stcesparto','tpnascassi','tpfuncresp','tpdocresp',
                                                          'dtdeclarac','escmaeagr1','stdnepidem','stdnnova','codpaisres','tprobson','paridade','kotelchuck','contador','munresstatus','munrestipo','munresnome','munresuf','latitude','longitude','munresalt','munresarea'])
  
  
  
  if 'Todas as variáveis' not in colunas:
         if st.button('Visualizar o Data Frame'):
                st.write(data[colunas][int(number1):int(number2)+1])
  
  if 'Todas as variáveis' in colunas:
         if st.button('Visualizar o Data Frame'):
                st.write(data[int(number1):int(number2)+1])
                







