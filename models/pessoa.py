from db import db
from datetime import datetime
import uuid

class PessoaModel(db.Model):
    __tablename__ = "pessoa"
    
    # id_pessoa = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    conta = db.relationship("ContaModel", backref="pessoa")
    email = db.Column(db.String(255), unique=True, nullable=False)  
    senha = db.Column(db.String(80), nullable=False)
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(255))  
    cpf = db.Column(db.String(11), unique=True)
    data_nascimento = db.Column(db.Date)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)  
    usuario_ativo = db.Column(db.Boolean, default=False)