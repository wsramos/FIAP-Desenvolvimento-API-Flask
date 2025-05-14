# Não vi que tinha usado a lib errada e acabei pesquisando com implementar essa versão
# Fica aqui como histórico caso seja necessário
# Após a execução do script será criado um arquivo recipes.db na raíz do projeto, contedo a tabela user

from flask import Flask
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('infrastructure.config')

class Base (DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password : Mapped[str] = mapped_column(String(120), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
        Base.metadata.create_all(engine)
        print("Banco de dados criado!")