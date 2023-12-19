from flask import Blueprint, request, jsonify
from app.models import Pessoa
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

pessoa_bp = Blueprint('pessoa', __name__, url_prefix='/pessoa')

@pessoa_bp.route('/registrar', methods=['POST'])
def registrar_pessoa():
    data = request.json
    nome = data.get('nome')
    cpf = data.get('cpf')
    data_nascimento = data.get('data_nascimento')
    senha = data.get('senha')

    # Gera o hash da senha fornecida
    senha_hash = generate_password_hash(senha)

    nova_pessoa = Pessoa(
        nome=nome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        senha_hash=senha_hash
    )
    
    db.session.add(nova_pessoa)
    db.session.commit()
    
    return jsonify({'message': 'Pessoa registrada com sucesso'}), 201