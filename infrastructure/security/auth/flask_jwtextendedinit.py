from infrastructure.database.flask_sqlalchemyinit import db, app
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

jwt = JWTManager(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")