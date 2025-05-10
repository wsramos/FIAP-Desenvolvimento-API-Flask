import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://olhardigital.com.br/2024/09/12/pro/ia-teria-encontrado-forma-de-nao-ser-controlada-por-humanos-entenda/'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text # Pega o conteúdo HTML
    print("Página obtida com sucesso!")

    # podemos usar métodos e acessar os elementos do html usando o objeto obtido com bs4
    soup = BeautifulSoup(html_content, 'html.parser')

    print(soup.title.string) # retorna o título da página
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")

