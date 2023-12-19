from db import db
from datetime import datetime
import uuid

class ContaModel(db.Model):
    __tablename__ = "conta"
    
    id_conta = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)  # Chave estrangeira para Pessoa
    saldo = db.Column(db.Numeric(10, 2))
    limite_saque_diario = db.Column(db.Numeric(10, 2))
    flag_ativo = db.Column(db.Boolean)
    tipo_conta = db.Column(db.Integer)
    data_criacao = db.Column(db.Date)
    transacoes = db.relationship('TransacaoModel', backref='conta', lazy=True)  # Relacionamento com TransacaoModel
