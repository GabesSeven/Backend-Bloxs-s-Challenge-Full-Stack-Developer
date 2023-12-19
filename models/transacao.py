from db import db
from datetime import datetime
import uuid

class TransacaoModel(db.Model):
    __tablename__ = "transacao"
    
    # id_transacao = db.Column(db.Integer, primary_key=True)
    id_transacao = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_conta = db.Column(db.String(36), db.ForeignKey('conta.id_conta'), nullable=False)
    valor = db.Column(db.Numeric(10, 2))
    data_transacao = db.Column(db.Date)