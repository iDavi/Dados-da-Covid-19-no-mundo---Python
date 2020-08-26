#Importando as coisas que o código precisa para funcionar
import pandas as pd
import requests
from bs4 import BeautifulSoup


#def que retorna a informação
def RetornarResposta(req):
    print("0 = Visão geral")
    print ("1 = Casos ativos no mundo")
    print("3 = Casos leves ativos no mundo")
    print("5 = Casos severos ativos no mundo")
    modos = ["Mostrando visão geral","Mostrando casos ativos no mundo","",
    "Mostrando casos leves ativos no mundo","","Mostrando Casos severos ativos no mundo"]

    modo = int(input("Digite um número"))
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find(name='table')
    table_str = str(table)
    df = pd.read_html(table_str)[0]

    print(modos[modo])
    if not modo == 0: 
        print(df[0][modo])
    else:
        print(df[0])

        
#def que inicia o programa
def Iniciar():
    print("Conectando com o banco de dados...")
    req = requests.get("https://www.worldometers.info/coronavirus/coronavirus-cases/")
    if req.status_code == 200:
        print("Conectado!")
        print("Dados da Covid 19 no mundo - Python | by @iDavi")
        RetornarResposta(req)
    else:
        print("Erro ao tentar se conectar ao banco de dados")
    

Iniciar() #Apenas chame iniciar para iniciar o programa

