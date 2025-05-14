from infrastructure.security.auth.flask_jwtextendedinit import (app, db, jwt_required, get_jwt_identity, create_access_token)
from infrastructure.database.flask_sqlalchemyinit import ConfigSQLAlchemy
from flasgger import Swagger
from flask import Flask, jsonify, request  # Importação dos componentes principais do Flask

swagger = Swagger(app)

@app.route('/register', methods=['POST'])
def register_user():
    """
    Registra um novo usuário.
    ---
    tags:
      - Usuários
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                example: "usuario123"
              password:
                type: string
                example: "senhaSegura"
    responses:
      201:
        description: Usuário criado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "User created"
      400:
        description: Usuário já existe
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "User already exists"
    """

    data = request.get_json()

    if ConfigSQLAlchemy.User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = ConfigSQLAlchemy.User(username=data['username'], password=data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Faz login do usuário e retorna um JWT.
    ---
    tags:
      - Autenticação
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                example: "usuario123"
              password:
                type: string
                example: "senhaSegura"
    responses:
      200:
        description: Login bem sucedido, retorna JWT
        content:
          application/json:
            schema:
              type: object
              properties:
                access_token:
                  type: string
                  example: "eyJ0eXAiOiJKV1QiLCJh..."
      401:
        description: Credenciais inválidas
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Invalid credentials"
    """
    data = request.get_json()
    
    user = ConfigSQLAlchemy.User.query.filter_by(username=data['username']).first()
    
    if user and user.password == data['password']:
        token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": token}), 200
    
    return jsonify(error="Invalid credentials"), 401


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Retorna uma mensagem indicando que o usuário autenticado acessou a rota protegida.
    ---
    tags:
      - Autenticação
    security:
      - BearerAuth: []
    responses:
      200:
        description: Acesso autorizado à rota protegida
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Usuário com ID 1 acessou a rota protegida."
      401:
        description: Token JWT ausente ou inválido
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Missing Authorization Header"
    """
    current_user_id = get_jwt_identity()
    return jsonify({"msg": f"Usuário com ID {current_user_id} acessou a rota protegida."}), 200


if __name__ == "__main__":
    app.run(debug=True)
