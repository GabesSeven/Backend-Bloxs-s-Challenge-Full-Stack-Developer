from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Conta(db.Model):
    id_conta = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_pessoa = db.Column(db.Integer)
    saldo = db.Column(db.Numeric(10, 2))
    limite_saque_diario = db.Column(db.Numeric(10, 2))
    flag_ativo = db.Column(db.Boolean)
    tipo_conta = db.Column(db.Integer)
    data_criacao = db.Column(db.Date)
    transacoes = db.relationship('Transacao', backref='conta', lazy=True)

class Transacao(db.Model):
    id_transacao = db.Column(db.Integer, primary_key=True)
    id_conta = db.Column(db.String(36), db.ForeignKey('conta.id_conta'), nullable=False)
    valor = db.Column(db.Numeric(10, 2))
    data_transacao = db.Column(db.Date)

class Pessoa(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14))
    data_nascimento = db.Column(db.Date)
    contas = db.relationship('Conta', backref='pessoa', lazy=True)