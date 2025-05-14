from flask import Flask, jsonify, request  # Importação dos componentes principais do Flask
from infrastructure.security.auth.basicAuth import BasicAuthentication
from flasgger import Swagger
from bs4 import BeautifulSoup
import requests

# Criando uma instância da classe Flask, que representa a aplicação web
wsapi = Flask(__name__)

wsapi.config['Swagger'] = {
    'title': 'My Flask API',
    'universion': 3
}

swagger = Swagger(wsapi)

def get_title(url):
    """
    Obtém o título de uma página web a partir da URL fornecida.

    Args:
        url (str): A URL da página a ser analisada.

    Returns:
        dict: Um dicionário contendo o título da página.
        tuple: Em caso de erro, retorna um dicionário com a mensagem de erro e um código HTTP 500.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return {"title": title}  # Corrigido para retornar um dicionário JSON válido
    except Exception as e:
        return {"error": str(e)}, 500

@wsapi.route('/scrape/title', methods=['GET'])
@BasicAuthentication.auth.login_required
def scrape_title():
    """
    Extrai o título de uma página web a partir da URL fornecida.
    ---
    security:
        - BasicAuth: []
    tags:
      - Web Scraping
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: A URL da página da qual o título será extraído.
    responses:
      200:
        description: Retorna o título da página web.
        schema:
          type: object
          properties:
            title:
              type: string
              description: O título da página extraída.
      400:
        description: Erro quando a URL não é fornecida.
        schema:
          type: object
          properties:
            error:
              type: string
              description: Mensagem informando que a URL é obrigatória.
    """
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    return jsonify(get_title(url))  # Retorno corrigido

if __name__ == '__main__':
    wsapi.run(debug=True)
