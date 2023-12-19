from flask import Blueprint, request, jsonify
from app.models import Conta, Transacao
from app import db
from datetime import datetime

conta_bp = Blueprint('conta', __name__, url_prefix='/conta')

@conta_bp.route('/criar', methods=['POST'])
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

# Endpoint para operação de depósito em uma conta
@conta_bp.route('/deposito/<id_conta>', methods=['PUT'])
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
@conta_bp.route('/saldo/<id_conta>', methods=['GET'])
def consulta_saldo(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    return jsonify({'saldo': float(conta.saldo)}), 200

# Endpoint para operação de saque em uma conta
@conta_bp.route('/saque/<id_conta>', methods=['PUT'])
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
@conta_bp.route('/bloquear_conta/<id_conta>', methods=['PUT'])
def bloquear_conta(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    conta.flag_ativo = False
    db.session.commit()
    return jsonify({'message': 'Conta bloqueada com sucesso'}), 200

# Endpoint para recuperar o extrato de transações de uma conta
@conta_bp.route('/extrato/<id_conta>', methods=['GET'])
def extrato(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    transacoes = Transacao.query.filter_by(id_conta=id_conta).all()
    extrato = [{'id_transacao': t.id_transacao, 'valor': float(t.valor), 'data_transacao': str(t.data_transacao)} for t in transacoes]
    return jsonify({'extrato': extrato}), 200