from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from db import db
from models import ContaModel, TransacaoModel, PessoaModel
from schemas import ContaSchema, TransacaoSchema, PessoaSchema

# Instância de Blueprint
blp = Blueprint("Pessoa", "pessoa", description="Operações em usuários")

@blp.route("/criar-usuario")
class PessoaCriacaoView(MethodView):
    """
    CRIAR PESSOA E ASSOCIAR UMA CONTA
    """
    @blp.arguments(PessoaSchema)
    @blp.response(201, PessoaSchema)
    def post(self, dados_pessoa):

        # Verifica se o usuário com o email especificado já existe
        email = dados_pessoa['email']
        usuario_existente = PessoaModel.query.filter_by(email=email).first()
        if usuario_existente:
            abort(409, message="Já existe um usuário com esse e-mail.")

        # Verifica se o usuário com o email especificado já existe
        cpf = dados_pessoa['cpf']
        usuario_existente = PessoaModel.query.filter_by(cpf=cpf).first()
        if usuario_existente:
            abort(409, message="Já existe um usuário com esse cpf.")

        try:
            data_nascimento_str = str(dados_pessoa['data_nascimento'])
            data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
        except:
            abort(409, message="Data de Nascimento deve ter formato de data: YYYY-MM-DD.")
            
        try:
            nova_pessoa = PessoaModel(
                email=email,
                senha=pbkdf2_sha256.hash(dados_pessoa["senha"]),
                nome=dados_pessoa['nome'],
                sobrenome=dados_pessoa['sobrenome'],
                cpf=cpf,
                data_nascimento=data_nascimento,
            )
            db.session.add(nova_pessoa)
            db.session.commit()

            # Cria uma nova conta associada à pessoa criada para renderizar diretamente na página principal
            nova_conta = ContaModel(
                id_pessoa=nova_pessoa.id_pessoa,
                saldo=0,
                limite_saque_diario=1000,  
                data_criacao=datetime.now().date()
            )
            db.session.add(nova_conta)
            db.session.commit()

            return nova_pessoa, 201
        except:
            db.session.rollback()
            abort(500, message="Não foi possível criar usuário")