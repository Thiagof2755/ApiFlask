from models.produtosModel import Produto
from app import db


def get_all_produtos(): # FUNÇÃO DE LISTAR TODOS OS PRODUTOS
    return Produto.query.all()

def get_produto_by_id(id): # FUNÇÃO DE BUSCAR UM PRODUTO PELO ID
    return Produto.query.filter_by(id=id).first()


def get_produtos_by_nome(parte_do_nome): # FUNÇÃO DE BUSCAR UM PRODUTO PELO NOME
    return Produto.query.filter(Produto.nome.like(f'%{parte_do_nome}%')).all()

def create_produto(nome, descricao, preco): # FUNÇÃO DE CRIAR UM NOVO PRODUTO 
    novo_produto = Produto(nome=nome, descricao=descricao, preco=preco)
    db.session.add(novo_produto)
    db.session.commit()
    return novo_produto

def update_produto(id, nome, descricao, preco): # FUNÇÃO DE ATUALIZAR UM PRODUTO PELO ID
    produto = get_produto_by_id(id)
    if produto:
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        db.session.commit()
        return produto
    return None

def delete_produto(id): # FUNÇÃO DE EXCLUIR UM PRODUTO PELO ID
    produto = get_produto_by_id(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False
