# 🚀 FIAP - Desenvolvimento de API com Flask

Este projeto fornece uma introdução ao desenvolvimento de APIs REST utilizando Flask, um microframework Python leve e poderoso. Ele demonstra como estruturar e implementar endpoints de uma API com autenticação (Basic e JWT), extração de dados via Web Scraping e manipulação de informações.

---

## 🔹 Tecnologias Utilizadas

- **Flask (3.1.0)**: Framework para construção de APIs web.
- **Flask-HTTPAuth (4.8.0)**: Autenticação básica para proteger os endpoints.
- **Flask-JWT-Extended (4.7.1)**: Autenticação baseada em tokens JWT.
- **Flasgger (0.9.7.1)**: Geração automática de documentação Swagger para a API.
- **Requests (2.32.3)**: Biblioteca para realizar requisições HTTP.
- **BeautifulSoup (4.13.4)**: Extração e análise de dados HTML/XML.
- **Pandas (2.2.3)**: Manipulação e estruturação de dados.
- **SQLAlchemy (4.7.1)**: ORM para modelagem e persistência de dados.
- **Flask SQLAlchemy (3.1.1)**: ORM para modelagem e persistência de dados (Lib Flask).

---

## 📘 Documentação da API com Flasgger

A documentação da API é gerada automaticamente com o **Flasgger**, uma extensão do Flask que integra o Swagger UI. Isso permite que você visualize, teste e interaja com os endpoints diretamente pelo navegador, sem a necessidade de ferramentas externas como Postman.

### 📍 Acesso

Após iniciar a aplicação, acesse a documentação interativa em:

```
http://localhost:5000/apidocs/
```

### ⚙️ Configuração

A configuração do Swagger está definida no arquivo `config_app_local.py`, incluindo título, versão e esquema de autenticação JWT:

```python
SWAGGER = {
  'title': 'Catálogo de Receitas Gourmet',
  'uiversion': 3,
  'version': '0.0.1',
  'openapi': '3.0.2',
  'components': {
    'securitySchemes': {
      'BearerAuth': {
        'type': 'http',
        'scheme': 'bearer',
        'bearerFormat': 'JWT',
        'description': 'Insira o token JWT no formato **Bearer <seu_token>**'
      }
    }
  },
  'security': [{'BearerAuth': []}]
}
```

### ✅ Benefícios

- Interface amigável para explorar e testar endpoints.
- Suporte a autenticação JWT diretamente pela interface.
- Geração automática a partir de docstrings nos métodos da API.
- Facilita a colaboração e entendimento da API por outros desenvolvedores.

---



## 🔐 Tipos de Autenticação

O projeto implementa dois tipos de autenticação:

### ✅ Basic Auth (via Flask-HTTPAuth)
- Utilizado em versões anteriores ou exemplos simples.
- Baseado em usuário e senha enviados no cabeçalho da requisição.

### 🔐 JWT (JSON Web Token)
- Implementado com Flask-JWT-Extended.
- Após login, o usuário recebe um token JWT.
- Esse token deve ser enviado no cabeçalho:

```
Authorization: Bearer <token>
```

---

## 🔑 Endpoints de Autenticação

- `POST /register`: Registra um novo usuário.
- `POST /login`: Realiza login e retorna um token JWT.
- `GET /protected`: Rota protegida que exige autenticação JWT.

---

## ⚙️ Configuração do Esquema de Segurança JWT

A configuração do JWT e sua integração com o Swagger estão definidas no arquivo `config_app_local.py`:

```python
SWAGGER = {
  'title': 'Catálogo de Receitas Gourmet',
  'uiversion': 3,
  'version': '0.0.1',
  'openapi': '3.0.2',
  'components': {
    'securitySchemes': {
      'BearerAuth': {
        'type': 'http',
        'scheme': 'bearer',
        'bearerFormat': 'JWT',
        'description': 'Insira o token JWT no formato **Bearer <seu_token>**'
      }
    }
  },
  'security': [{'BearerAuth': []}]
}
```

---

## 🧠 Modelos e Banco de Dados

O projeto utiliza **Flask-SQLAlchemy** com banco de dados SQLite. A configuração está em `config_app_local.py`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### Modelos definidos

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time_minutes = db.Column(db.Integer, nullable=False)
```

---

## 🔗 API Reference

Esta seção reúne todos os endpoints disponíveis no projeto, organizados por contexto de uso. A API inclui funcionalidades de autenticação, gerenciamento de receitas (com proteção via JWT) e manipulação de itens em memória (para fins de demonstração).

### 🍲 Endpoints de Receitas (JWT Protegidos)

Todos os endpoints abaixo requerem autenticação JWT via cabeçalho:

```
Authorization: Bearer <seu_token>
```

| Método | Rota                  | Descrição                         |
|--------|-----------------------|-----------------------------------|
| POST   | `/recipes`            | Cria uma nova receita             |
| GET    | `/recipes`            | Lista receitas com filtros        |
| PUT    | `/recipes/<id>`       | Atualiza uma receita existente    |
| DELETE | `/recipes/<id>`       | Remove uma receita                |

#### Filtros disponíveis em `/recipes`:

- `ingredient`: filtra por ingrediente
- `max_time`: tempo máximo de preparo (minutos)

---

### 📦 Endpoints de Itens (Em Memória)

Estes endpoints manipulam uma lista de itens armazenados em memória. Não utilizam banco de dados nem autenticação.

| Método | Rota             | Descrição                         |
|--------|------------------|-----------------------------------|
| GET    | `/items`         | Retorna todos os itens            |
| POST   | `/items`         | Cria um novo item                 |
| PUT    | `/items/<index>` | Atualiza um item pelo índice      |
| DELETE | `/items/<index>` | Remove um item pelo índice        |

#### Exemplos de uso via `curl`:

```bash
# Obter todos os itens
curl -X GET http://localhost:5000/items -H "Content-Type: application/json"

# Criar um item
curl -X POST http://localhost:5000/items \
  -d '{"nome":"Coca-Cola","valor":"R$15,00"}' \
  -H "Content-Type: application/json"

# Atualizar um item
curl -X PUT http://localhost:5000/items/0 \
  -d '{"nome":"Coca-Cola","valor":"R$18,00"}' \
  -H "Content-Type: application/json"

# Excluir um item
curl -X DELETE http://localhost:5000/items/0 \
  -H "Content-Type: application/json"
```

---

## 📌 Preparando o Ambiente

1. Criar um ambiente virtual:
   ```
   python -m venv env
   ```

2. Ativar o ambiente virtual:
   ```
   source env/Scripts/activate
   ```

3. Instalar as dependências:
   ```
   pip install -r requirements.txt
   ```

---

## ▶️ Executando scripts
A estrutura do projeto visa separar em as responsabilidades em scripts isolados, portanto para que não haja erro na execução de nenhum script por falta de dependência ou falha na importação, é necessário executar os scripts especificando o contexto geral do projeto. Abaixo, temos um exemplo de como fazer isso:

```bash
python -m api.receitas_gourmet_api
```

---

## 🌐 Flask - Introdução

Flask é um microframework web em Python, minimalista e flexível, ideal para criar APIs e aplicações web **de forma rápida e simples**, com suporte a extensões para funcionalidades adicionais.

### Configurações

- Builtin Configuration Values:
  https://flask.palletsprojects.com/en/stable/config/#builtin-configuration-values

---

## 🕵️ Web Scraping

### 🔍 O que é Web Scraping?

Web scraping é uma técnica para extrair dados de sites de maneira automatizada. Ele é útil quando:

- Não há API disponível para acessar os dados.
- É necessário coletar grandes volumes de informações públicas na web.
- Há necessidade de monitoramento de preços, notícias ou tendências.

### ⚠️ Considerações sobre Uso

Antes de realizar web scraping, verifique os termos de uso do site. Algumas práticas podem violar políticas ou legislações, como a LGPD no Brasil.

### 🛠 Como usar Web Scraping em Python?

O processo básico envolve:

1. Fazer requisições HTTP para acessar páginas da web.
2. Analisar o HTML da página para localizar os dados desejados.
3. Extrair e estruturar os dados.

### 🏆 BeautifulSoup

- Uso: Análise e extração de dados de HTML e XML.
- Vantagens: Simples e fácil de usar.
- Instalação: `pip install beautifulsoup4`
