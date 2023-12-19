from db import db
from datetime import datetime
import uuid

class ContaModel(db.Model):
    id_conta = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'))  # Adicionando chave estrangeira para Pessoa
    saldo = db.Column(db.Numeric(10, 2))
    limite_saque_diario = db.Column(db.Numeric(10, 2))
    flag_ativo = db.Column(db.Boolean)
    tipo_conta = db.Column(db.Integer)
    data_criacao = db.Column(db.Date)
    transacoes = db.relationship('Transacao', backref='conta', lazy=True)

class TransacaoModel(db.Model):
    id_transacao = db.Column(db.Integer, primary_key=True)
    id_conta = db.Column(db.String(36), db.ForeignKey('conta.id_conta'), nullable=False)
    valor = db.Column(db.Numeric(10, 2))
    data_transacao = db.Column(db.Date)

class PessoaModel(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(255))  # campo adicional 
    cpf = db.Column(db.String(14))
    data_nascimento = db.Column(db.Date)
    email = db.Column(db.String(255), unique=True)  # campo adicional para autenticação
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)  # campo adicional para, caso necessário, controle de usuários
    is_deleted = db.Column(db.Boolean, default=False)  # campo adicional para, caso necessário, exclusão lógica ou soft delete
    contas = db.relationship('Conta', backref='pessoa', lazy=True)