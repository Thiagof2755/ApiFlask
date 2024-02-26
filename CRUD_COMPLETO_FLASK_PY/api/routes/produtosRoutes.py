from flask import jsonify, request
from app import app
from controllers.produtosController import get_all_produtos , get_produto_by_id , create_produto , update_produto , delete_produto

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = get_all_produtos()
    output = [{'id': produto.id, 'nome': produto.nome, 'descricao': produto.descricao, 'preco': produto.preco} for produto in produtos]
    return jsonify({'produtos': output})

@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    produto = get_produto_by_id(id)
    return jsonify({'id': produto.id, 'nome': produto.nome, 'descricao': produto.descricao, 'preco': produto.preco})

@app.route('/produtos', methods=['POST'])
def create_produto_route():
    data = request.json
    novo_produto = create_produto(data['nome'], data['descricao'], data['preco'])
    # Aqui, você pode criar um dicionário com os atributos do novo produto
    produto_serializado = {
        'id': novo_produto.id,
        'nome': novo_produto.nome,
        'descricao': novo_produto.descricao,
        'preco': novo_produto.preco
    }
    return jsonify({'message': 'Produto criado com sucesso!', 'produto': produto_serializado}), 201


@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto_route(id):
    data = request.json
    produto = update_produto(id, data['nome'], data['descricao'], data['preco'])
    if produto:
        produto_serializado = {
            'id': produto.id,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': produto.preco
        }
        return jsonify({'message': 'Produto atualizado com sucesso!', 'produto': produto_serializado})
    return jsonify({'message': 'Produto não encontrado!'}), 404

@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto_route(id):
    if delete_produto(id):
        return jsonify({'message': 'Produto deletado com sucesso!'})
    return jsonify({'message': 'Produto não encontrado!'}), 404