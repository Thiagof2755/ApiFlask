from flask import jsonify, request, render_template, redirect, url_for, flash , session
from app import app
from controllers.produtosController import get_all_produtos, get_produtos_by_nome, create_produto, update_produto, delete_produto, get_produto_by_id
from controllers.userController import logar, deslogar

# ROTAS
# SOMENTE ACESSIVEL POR USUÁRIOS LOGADOS (USANDO SESSÃO)

@app.route('/', methods=['GET']) # ROTA PRINCIPAL DA APLICACÃO
def get_produtos():
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    produtos = get_all_produtos()
    output = [{'id': produto.id, 'nome': produto.nome, 'descricao': produto.descricao, 'preco': produto.preco} for produto in produtos]
    return render_template('produtos.html', produtos=output)


@app.route('/buscar_produtos', methods=['GET']) # ROTA DE BUSCA DE PRODUTOS POR NOME
def buscar_produtos_por_nome():
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    nome_do_produto = request.args.get('nome')
    produtos = get_produtos_by_nome(nome_do_produto)
    if produtos:
        return render_template('produtos.html', produtos=produtos)
    else:
        return render_template('produtos.html', produtos=[], message='Nenhum produto encontrado com esse nome.')


@app.route('/criar') # ROTA DE CRIACÃO DE NOVO PRODUTO TELA (GET)
def criar():
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    return render_template('criar.html')


@app.route('/criar_produto', methods=['POST']) # ROTA DE CRIACÃO DE NOVO PRODUTO (POST)
def criar_produto():
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        novo_produto = create_produto(nome, descricao, preco)
        return redirect(url_for('get_produtos'))


@app.route('/editar_produto/<int:id>') # ROTA DE EDICAO DE PRODUTO TELA
def editar_produto(id):
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    produto = get_produto_by_id(id)
    return render_template('editar.html', produto=produto)


@app.route('/atualizar_produto/<int:id>', methods=['POST']) # ROTA DE EDICAO DE PRODUTO (POST)
def atualizar_produto(id): 
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        produto = update_produto(id, nome, descricao, preco)
        return redirect(url_for('get_produtos'))


@app.route('/produtos/<int:id>', methods=['POST']) # ROTA DE EXCLUSÃO DE PRODUTO
def delete_produto_route(id):
    if 'usuario_logado' not in session:
        return redirect(url_for('login_route'))
    if request.form['_method'] == 'DELETE':
        if delete_produto(id):
            flash('Produto excluído com sucesso!', 'success')
        else:
            flash('Produto não encontrado!', 'error')
    return redirect(url_for('get_produtos'))


@app.route('/login', methods=['GET', 'POST']) # ROTA DE LOGIN
def login_route():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if logar(email, senha):
            session['usuario_logado'] = True
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('get_produtos'))
            
        else:
            flash('Credenciais inválidas. Por favor, tente novamente.', 'error')
    return render_template('login.html')



@app.route('/logout') # ROTA DE LOGOUT
def logout_route():
    deslogar()
    session.pop('usuario_logado', None)
    flash('Logout bem-sucedido!', 'success')
    return redirect(url_for('login_route'))
