from infrastructure.security.auth.flask_jwtextendedinit import (app, db, jwt_required, get_jwt_identity, create_access_token)
from infrastructure.database.flask_sqlalchemyinit import ConfigSQLAlchemy
from flasgger import Swagger
from flask import Flask, jsonify, request  # Importação dos componentes principais do Flask

swagger = Swagger(app)


@app.route('/recipes', methods=['POST'])
@jwt_required()
def create_recipe():
    """
    Cria uma nova receita.
    ---
    tags:
      - Receitas
    security:
      - BearerAuth: []
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - title
              - ingredients
              - time_minutes
            properties:
              title:
                type: string
                example: "Bolo de cenoura"
              ingredients:
                type: string
                example: "cenoura, farinha, ovos, açúcar"
              time_minutes:
                type: integer
                example: 45
    responses:
      201:
        description: Receita criada com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Recipe created"
      401:
        description: Token não fornecido ou inválido
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Missing Authorization Header"
    """
    data = request.get_json()
    new_recipe = ConfigSQLAlchemy.Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        time_minutes=data['time_minutes']
    )

    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({"msg": "Recipe created"}), 201

@app.route('/recipes', methods=['GET'])
@jwt_required()
def get_recipes():
    """
    Lista receitas com filtros opcionais.
    ---
    tags:
      - Receitas
    security:
      - BearerAuth: []
    parameters:
      - in: query
        name: ingredient
        schema:
          type: string
        required: false
        description: Filtra por ingrediente
      - in: query
        name: max_time
        schema:
          type: integer
        required: false
        description: Tempo máximo de preparo (minutos)
    responses:
      200:
        description: Lista de receitas filtradas.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  title:
                    type: string
                    example: "Bolo de chocolate"
                  time_minutes:
                    type: integer
                    example: 45
                  ingredients:
                    type: array
                    items:
                      type: string
                    example: ["chocolate", "farinha", "açúcar"]
    """
    ingredient = request.args.get('ingredient')
    max_time = request.args.get('max_time', type=int)

    query = ConfigSQLAlchemy.Recipe.query

    if ingredient:
        query = query.filter(ConfigSQLAlchemy.Recipe.ingredients.ilike(f'%{ingredient}%'))
    
    if max_time is not None:
        query = query.filter(ConfigSQLAlchemy.Recipe.time_minutes <= max_time)

    recipes = query.all()
    
    return jsonify([
        {
            'id': r.id,
            'title': r.title,
            'time_minutes': r.time_minutes,
            'ingredients': r.ingredients.split(',')
        }
        for r in recipes 
    ])

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
@jwt_required()
def update_recipe(recipe_id):
    """
    Atualiza uma receita existente.
    ---
    tags:
      - Receitas
    security:
      - BearerAuth: []
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
        description: ID da receita a ser atualizada
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              title:
                type: string
                example: "Torta de maçã"
              ingredients:
                type: string
                example: "maçã, farinha, açúcar"
              time_minutes:
                type: integer
                example: 60
    responses:
      200:
        description: Receita atualizada
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Receita atualizada!"
      404:
        description: Receita não encontrada
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Receita não encontrada"
      401:
        description: Token não fornecido ou inválido
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Missing Authorization Header"
    """
    data = request.get_json()
    
    recipe = ConfigSQLAlchemy.Recipe.query.get_or_404(recipe_id)
    
    if 'title' in data:
        recipe.title = data['title']
        
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
        
    if 'time_minutes' in data:
        recipe.time_minutes = data['time_minutes']
        
    db.session.commit()
    
    return jsonify({"message": "Receita atualizada!"})

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id):
    """
    Remove uma receita existente.
    ---
    tags:
      - Receitas
    security:
      - BearerAuth: []
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
        description: ID da receita a ser removida
    responses:
      200:
        description: Receita removida com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Receita removida!"
      404:
        description: Receita não encontrada
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Receita não encontrada"
      401:
        description: Token não fornecido ou inválido
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Missing Authorization Header"
    """
    recipe = ConfigSQLAlchemy.Recipe.query.get_or_404(recipe_id)

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({"message": "Receita removida!"}), 200


if __name__ == "__main__":
    app.run(debug=True)