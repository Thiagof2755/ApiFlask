from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
db = SQLAlchemy(app)

# Importe as rotas após a inicialização do app e do SQLAlchemy
from routes.produtosRoutes import *



if __name__ == '__main__':
    app.run(debug=True)
    
    
    
