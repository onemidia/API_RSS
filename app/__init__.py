from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Se utilizar banco de dados

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@host/banco_de_dados'  # Configuração do banco de dados
db = SQLAlchemy(app)

from app import routes  # Importa as rotas