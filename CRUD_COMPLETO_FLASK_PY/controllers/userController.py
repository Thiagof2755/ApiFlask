from flask import session
from models.usermodel import Usuario

def logar(email, senha): # FUNÇÃO DE LOGIN
    
    # Verifica se o usuário com o email fornecido existe no banco de dados
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        # Verifica se a senha fornecida está correta
        if usuario.senha == senha:
            # Define o ID do usuário na sessão para indicar que ele está logado
            session['user_id'] = usuario.id
            return True
    return False

def deslogar(): # FUNÇÃO DE DESLOGAR 
    # Remove o ID do usuário da sessão para indicar que ele não está mais logado
    session.pop('user_id', None)
