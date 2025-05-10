# 🚀 FIAP - Desenvolvimento de API com Flask

Este projeto fornece uma introdução ao desenvolvimento de APIs REST utilizando Flask, um microframework Python leve e poderoso. Ele demonstra como estruturar e implementar endpoints de uma API com autenticação básica, extração de dados via Web Scraping e manipulação de informações.

🔹 Tecnologias Utilizadas:
* Flask (3.1.0): Framework para construção de APIs web.
* Flask-HTTPAuth (4.8.0): Autenticação básica para proteger os endpoints.
* Flasgger (0.9.7.1): Geração automática de documentação Swagger para a API.
* Requests (2.32.3): Biblioteca para realizar requisições HTTP.
* BeautifulSoup (4.13.4): Extração e análise de dados HTML/XML.
* Pandas (2.2.3): Manipulação e estruturação de dados.

O código inclui exemplos práticos de operações CRUD, autenticação, web scraping e documentação interativa, facilitando a construção de APIs escaláveis e bem organizadas.

## 📌 Preparando o Ambiente

1. Criar um ambiente virtual:
~~~~
python -m venv env
~~~~

2. Ativar o ambiente virtual:
~~~~
source env/Scripts/activate
~~~~

3. Instalar as dependências:
~~~~
pip install - requirements.txt
~~~~

## 🌐 Flask - Introdução
Flask é um microframework web em Python, minimalista e flexível, ideal para criar APIs e Aplicações web **de forma rápida e simples**, com suporte a extensões para funcionalidades adicionais.

## 🕵️ Web Scraping

### 🔍 O que é Web Scraping?
Web scraping é uma técnica para extrair dados de sites de maneira automatizada. Ele é útil quando:

* Não há API disponível para acessar os dados.
* É necessário coletar grandes volumes de informações públicas na web.
* Há necessidade de monitoramento de preços, notícias ou tendências.

### ⚠️ Considerações sobre Uso
Antes de realizar web scraping, verifique os termos de uso do site. Algumas práticas podem violar políticas ou legislações, como a LGPD no Brasil.

### 🛠 Como usar Web Scraping em Python?
O processo básico envolve:

Fazer requisições HTTP para acessar páginas da web.
Analisar o HTML da página para localizar os dados desejados.
Extrair e estruturar os dados.

### 🏆 BeautifulSoup:

* Uso: Análise e extração de dados de HTML e XML.
* Vantagens: Simples e fácil de usar.
* Instalação: pip install beautifulsoup4

## 🔗 API Reference

### 📌 Obter Itens

Retorna uma lista de Items armazenados em variável.
* Retorno: Json com cada item da Lista.
* StatusCode: 200

~~~
# Via linha de comando

curl -X GET http://localhost:5000/items -H "Content-Type: application/json"
~~~

### 🆕 Criar Item

Cria um item de acordo com o body recebido na requisição. Inclui o item na lista de items.
* Retorno: Json do item criado.
* StatusCode: 201

~~~
# Via linha de comando

curl -X POST http://localhost:5000/items -d '{"nome":"Coca-Cola","valor":"R$15,00"}' -H "Content-Type: application/json"
~~~

### ✏️ Atualizar Item

Atualiza um item de acordo com a índice na lista de items.
* Retorno: Json do item atualizado.
* StatusCode: 200
* ErrorCode: 404

~~~
# Via linha de comando

curl -X PUT http://localhost:5000/items/0 -d '{"nome":"Coca-Cola","valor":"R$15,00"}' -H "Content-Type: application/json"
~~~

### 🗑️ Excluir Item

Exclui um item de acordo com o índice na lista de items.
* Retorno: N/A.
* StatusCode: 200
* ErrorCode: 404

~~~
# Via linha de comando

curl -X DELETE http://localhost:5000/items/0 -H "Content-Type: application/json"
~~~