from app import db

class Produto(db.Model): # MODELO DE PRODUTO (ENTIDADE)
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float, nullable=False)

