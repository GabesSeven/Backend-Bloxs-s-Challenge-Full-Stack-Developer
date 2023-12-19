from db import db
from datetime import datetime
import uuid

class PessoaModel(db.Model):
    __tablename__ = "pessoa"
    
    # id_pessoa = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True)  

    senha = db.Column(db.String(80), nullable=False)
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(255))  
    cpf = db.Column(db.String(14))
    data_nascimento = db.Column(db.Date)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)  
    is_deleted = db.Column(db.Boolean, default=False)  
    contas = db.relationship('ContaModel', backref='pessoa', lazy=True)  # Relacionamento com ContaModel