from flask import Flask, jsonify, request  # Importação dos componentes principais do Flask
from infrastructure.basicAuth import BasicAuthentication
from flasgger import Swagger

# Criando uma instância da classe Flask, que representa a aplicação web
items_api = Flask(__name__)

# Lista que servirá como armazenamento temporário de itens
items = []

items_api.config['Swagger'] = {
    'title': 'My Flask API',
    'universion': 3
}

swagger = Swagger(items_api)

@items_api.route('/items', methods=['GET'])  # Define um endpoint que responde a requisições GET na rota /items
@BasicAuthentication.auth.login_required
def get_items():
    """
    Obtém a lista de itens armazenados.
    ---
    tags:
      - Items
    responses:
      200:
        description: Retorna a lista de itens armazenados.
        schema:
          type: array
          items:
            type: object
    """
    return jsonify(items)

@items_api.route('/items', methods=['POST'])  # Define um endpoint que responde a requisições POST na rota /items
@BasicAuthentication.auth.login_required
def create_item():
    """
    Adiciona um novo item à lista.
    ---
    tags:
      - Items
    parameters:
      - name: item
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Nome do item a ser adicionado.
            description:
              type: string
              description: Descrição do item.
    responses:
      201:
        description: O item foi criado com sucesso.
        schema:
          type: object
      400:
        description: Erro ao criar item.
    """
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

@items_api.route('/items/<int:item_id>', methods=['PUT'])  # Define um endpoint que responde a requisições PUT para atualizar um item específico
@BasicAuthentication.auth.login_required
def update_item(item_id):
    """
    Atualiza um item existente pelo índice.
    ---
    tags:
      - Items
    parameters:
      - name: item_id
        in: path
        type: integer
        required: true
        description: Índice do item a ser atualizado.
      - name: item
        in: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Item atualizado com sucesso.
        schema:
          type: object
      404:
        description: Item não encontrado.
    """
    data = request.get_json()

    if 0 <= item_id < len(items):
        items[item_id].update(data)
        return jsonify(items[item_id])

    return jsonify({"error": "item not found"}), 404

@items_api.route('/items/<int:item_id>', methods=['DELETE'])  # Define um endpoint que responde a requisições DELETE para remover um item específico
@BasicAuthentication.auth.login_required
def delete_item(item_id):
    """
    Remove um item pelo índice.
    ---
    tags:
      - Items
    parameters:
      - name: item_id
        in: path
        type: integer
        required: true
        description: Índice do item a ser removido.
    responses:
      200:
        description: Item removido com sucesso.
        schema:
          type: object
      404:
        description: Item não encontrado.
    """
    if 0 <= item_id < len(items):
        removed = items.pop(item_id)
        return jsonify(removed)

    return jsonify({"error": "item not found"}), 404

if __name__ == '__main__':
    items_api.run(debug=True)
