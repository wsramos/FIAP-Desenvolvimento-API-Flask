from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Após a execução do script, será criada uma pasta chamada instance, contendo um arquivo chamado recipes.db
# Este arquivo contém a descrição do banco em sqlite, banco de dados em memória para python
# É como se fosse o h2 do java, mas em python

app = Flask(__name__)
app.config.from_object('infrastructure.config_app_local')

db = SQLAlchemy(app)

class ConfigSQLAlchemy:

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(120), nullable=False)

    class Recipe(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        ingredients = db.Column(db.Text, nullable=False)
        time_minutes = db.Column(db.Integer, nullable=False)

    if __name__ == '__main__':
        with app.app_context():
            db.create_all()
            print("Banco de dados criado!")