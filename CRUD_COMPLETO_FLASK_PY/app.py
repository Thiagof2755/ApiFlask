from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB

app = Flask(__name__) # APLICACÃO FLASK
app.secret_key = "super secret key" # CHAVE SECRETA
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}" # CONEXÃO COM O BANCO DE DADOS
db = SQLAlchemy(app) # 

from routes.Routes import * # IMPORTANDO ROTAS DA APLICACÃO



if __name__ == '__main__': # INICIALIZANDO APLICACÃO
    app.run(debug=True) # RODANDO APLICACÃO EM MODO DE DESENVOLVIMENTO (DEBUG)    
