from db import db
from datetime import datetime
import uuid

class ContaModel(db.Model):
    __tablename__ = "conta"
    
    # id_conta = db.Column(db.Integer, primary_key=True)
    id_conta = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_pessoa = db.Column(db.String, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    transacao = db.relationship("TransacaoModel", backref="conta")
    saldo = db.Column(db.Numeric(10, 2))
    limite_saque_diario = db.Column(db.Numeric(10, 2))
    flag_ativo = db.Column(db.Boolean, default=True)
    tipo_conta = db.Column(db.Integer)
    data_criacao = db.Column(db.Date)

