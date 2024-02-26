from models.produtosModel import Produto
from app import db

def get_all_produtos():
    return Produto.query.all()

def get_produto_by_id(id):
    return Produto.query.filter_by(id=id).first()


def create_produto(nome, descricao, preco):
    novo_produto = Produto(nome=nome, descricao=descricao, preco=preco)
    db.session.add(novo_produto)
    db.session.commit()
    return novo_produto

def update_produto(id, nome, descricao, preco):
    produto = get_produto_by_id(id)
    if produto:
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        db.session.commit()
        return produto
    return None

def delete_produto(id):
    produto = get_produto_by_id(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False
