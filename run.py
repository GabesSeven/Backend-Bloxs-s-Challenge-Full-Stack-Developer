from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Pessoa, Conta, Transacao  # Importando os modelos do app
from datetime import datetime
from dotenv import load_dotenv
import os

from app.models import Conta, Transacao  # Importando os modelos do app
from datetime import datetime

# Inicializa do app e configuração de rota do Banco de Dados
app = Flask(__name__)

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Habilita CORS para todas as rotas
CORS(app) 

# Configuração da conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy(app)

# Endpoint para criação de conta
@app.route('/criar_conta', methods=['POST'])
def criar_conta():
    data = request.json
    nova_conta = Conta(
        id_pessoa=data['id_pessoa'],
        saldo=data['saldo'],
        limite_saque_diario=data['limite_saque_diario'],
        flag_ativo=data['flag_ativo'],
        tipo_conta=data['tipo_conta'],
        data_criacao=datetime.now().date()
    )
    db.session.add(nova_conta)
    db.session.commit()
    return jsonify({'message': 'Conta criada com sucesso'}), 201

# Endpoint para registrar uma nova pessoa com senha criptografada
@app.route('/registrar_pessoa', methods=['POST'])
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

# Endpoint para realizar login
@app.route('/login', methods=['POST'])
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


# Endpoint para operação de depósito em uma conta
@app.route('/deposito/<id_conta>', methods=['PUT'])
def deposito(id_conta):
    data = request.json
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    conta.saldo += data['valor']
    nova_transacao = Transacao(
        id_conta=id_conta,
        valor=data['valor'],
        data_transacao=datetime.now().date()
    )
    db.session.add(nova_transacao)
    db.session.commit()
    return jsonify({'message': 'Depósito realizado com sucesso'}), 200

# Endpoint para consulta de saldo em determinada conta
@app.route('/saldo/<id_conta>', methods=['GET'])
def consulta_saldo(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    return jsonify({'saldo': float(conta.saldo)}), 200

# Endpoint para operação de saque em uma conta
@app.route('/saque/<id_conta>', methods=['PUT'])
def saque(id_conta):
    data = request.json
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    if conta.saldo < data['valor']:
        return jsonify({'message': 'Saldo insuficiente'}), 400
    conta.saldo -= data['valor']
    nova_transacao = Transacao(
        id_conta=id_conta,
        valor=-data['valor'],
        data_transacao=datetime.now().date()
    )
    db.session.add(nova_transacao)
    db.session.commit()
    return jsonify({'message': 'Saque realizado com sucesso'}), 200

# Endpoint para bloquear uma conta
@app.route('/bloquear_conta/<id_conta>', methods=['PUT'])
def bloquear_conta(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    conta.flag_ativo = False
    db.session.commit()
    return jsonify({'message': 'Conta bloqueada com sucesso'}), 200

# Endpoint para recuperar o extrato de transações de uma conta
@app.route('/extrato/<id_conta>', methods=['GET'])
def extrato(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    transacoes = Transacao.query.filter_by(id_conta=id_conta).all()
    extrato = [{'id_transacao': t.id_transacao, 'valor': float(t.valor), 'data_transacao': str(t.data_transacao)} for t in transacoes]
    return jsonify({'extrato': extrato}), 200

# Função main 
if __name__ == '__main__':
    app.run(debug=True)
