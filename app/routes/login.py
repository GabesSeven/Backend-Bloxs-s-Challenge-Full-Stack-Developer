from flask import Blueprint, request, jsonify
from app.models import Pessoa
from app import db
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    id_pessoa = data.get('id_pessoa')
    senha = data.get('senha')

    # Busca a pessoa pelo ID
    pessoa = Pessoa.query.filter_by(id_pessoa=id_pessoa).first()

    if pessoa and check_password_hash(pessoa.senha_hash, senha):
        # Se a pessoa existe e a senha está correta, retorna 'Login bem-sucedido'
        return jsonify({'message': 'Login bem-sucedido'}), 200
    else:
        # Caso contrário, retorna 'Credenciais inválidas'
        return jsonify({'message': 'Credenciais inválidas'}), 401