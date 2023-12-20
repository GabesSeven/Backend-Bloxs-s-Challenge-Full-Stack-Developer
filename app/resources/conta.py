from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from datetime import datetime
from db import db
from models import ContaModel, TransacaoModel, PessoaModel
from schemas import ContaSchema, TransacaoSchema
from decimal import Decimal

# Instância de Blueprint
blp = Blueprint("Conta", "conta", description="Operações em contas")


@blp.route("/conta")
class ContaCriacaoView(MethodView):
    """
    CRIAR CONTA
    """
    @blp.arguments(ContaSchema)
    @blp.response(201, ContaSchema)
    def post(self, dados_conta):
        # Verifica dados de entrada
        try:
            id_pessoa = dados_conta['id_pessoa']
            usuario = PessoaModel.query.get(id_pessoa)
        except:
            abort(500, message="Validação incorreta")
        
        # Verifica se o usuário com o id_pessoa especificado existe
        if not usuario:
            abort(404, message=f"Usuário não encontrado.")
            
        try:
            nova_conta = ContaModel(
                id_pessoa=dados_conta['id_pessoa'],
                saldo=dados_conta['saldo'],
                limite_saque_diario=dados_conta['limite_saque_diario'],
                tipo_conta=dados_conta['tipo_conta'],
                data_criacao=datetime.now().date()
            )
            db.session.add(nova_conta)
            db.session.commit()

            return nova_conta, 201
        except:
            db.session.rollback()
            # abort(500, message="Não foi possível criar conta")

@blp.route("/conta/<id_conta>")
class ContaDelecaoView(MethodView):
    """
    DELETAR / BLOQUEAR CONTA
    """
    @blp.response(204)
    def delete(self, id_conta):
        # Verifica dados de entrada
        try:
            conta = ContaModel.query.get(id_conta)
        except:
            abort(500, message="Validação incorreta")

        # Verifica se conta existe
        if not conta:
            abort(404, message='Conta não encontrada')
        
        # Verifica se conta está ativa
        if not conta.flag_ativo:
            abort(403, message='Conta não está ativa')

        try:
            conta.flag_ativo = False
            db.session.commit()
            return {'message': 'Conta bloqueada com sucesso'}, 200
        except:
            db.session.rollback()
            abort(500, message="Não foi possível bloquear conta")

    """
    SALDO DE CONTA
    """
    @blp.response(200, ContaSchema)
    def get(self, id_conta):
        # Verifica dados de entrada
        try:
            conta = ContaModel.query.get(id_conta)
        except:
            abort(500, message="Validação incorreta")

        # Verifica se conta existe
        if not conta:
            abort(404, message='Conta não encontrada')
        
        # Verifica se conta está ativa
        if not conta.flag_ativo:
            abort(403, message='Conta não está ativa')
    
        return {'saldo': float(conta.saldo)}, 200

@blp.route("/operacao")
class OperacaoDepositoView(MethodView):
    """
    DEPÓSITO
    """
    @blp.arguments(TransacaoSchema)
    @blp.response(200)
    def put(self, dados_conta):
        # Verifica dados de entrada
        try:
            id_conta = dados_conta['id_conta']
            valor = dados_conta['valor']
            conta = ContaModel.query.get(id_conta)
        except:
            abort(500, message="Validação incorreta")

        # Verifica se conta existe
        if not conta:
            abort(404, message='Conta não encontrada')

        # Verifica se conta está ativa
        if not conta.flag_ativo:
            abort(403, message='Conta não está ativa')
        
        try:    
            valor = Decimal(valor)
            conta.saldo += valor
            nova_transacao = TransacaoModel(
                id_conta=id_conta,
                valor=valor,
                data_transacao=datetime.now().date()
            )
            db.session.add(nova_transacao)
            db.session.commit()

            return {'message': 'Depósito realizado com sucesso', "deposito": valor, "saldo": conta.saldo}, 200
        except:
            db.session.rollback()
            abort(500, message="Não foi possível obter depósito")

# @blp.route("/operacao/<id_conta>")
# class OperacaoSaqueETransacaoView(MethodView):
#     """
#     SAQUE
#     """
#     @blp.response(200, TransacaoSchema)
#     def delete(self, id_conta):
#         # Verifica dados de entrada
#         try:
#             conta = ContaModel.query.get(id_conta)
#         except:
#             abort(500, message="Validação incorreta")
        
#         # Verifica se conta existe
#         if not conta:
#             abort(404, message='Conta não encontrada')

#         # Verifica se conta está ativa
#         if not conta.flag_ativo:
#             abort(403, message='Conta não está ativa')

#         # Verifica saldo
#         if conta.saldo < data['valor']:
#             abort(400, message='Saldo insuficiente')

#         ##############
#         # Lógica para verificação de limite
#         # Pegar valores de saque de todas datas correspondentes e verificar se é menor que o limite diário 
#         ##############

#         try:
#             conta.saldo -= data['valor']
#             nova_transacao = TransacaoModel(
#                 id_conta=id_conta,
#                 valor=-data['valor'],
#                 data_transacao=datetime.now().date()
#             )
#             db.session.add(nova_transacao)
#             db.session.commit()
#             return {'message': 'Saque realizado com sucesso'}, 200
#         except:
#             db.session.rollback()
#             abort(500, message="Não foi possível obter saque")

#     """
#     EXTRATO
#     """
#     @blp.response(200, TransacaoSchema(many=True))
#     def get(self, id_conta):
#         # Verifica dados de entrada
#         try:
#             conta = ContaModel.query.get(id_conta)
#         except:
#             abort(500, message="Validação incorreta")

#         # Verifica se conta existe
#         if not conta:
#             abort(404, message='Conta não encontrada')

#         # Verifica se conta está ativa
#         if not conta.flag_ativo:
#             abort(403, message='Conta não está ativa')

#         try:
#             transacoes = TransacaoModel.query.filter_by(id_conta=id_conta).all()
#             extrato = [{'id_transacao': t.id_transacao, 'valor': float(t.valor), 'data_transacao': str(t.data_transacao)} for t in transacoes]
#             return {'extrato': extrato}, 200
#         except:
#             db.session.rollback()
#             abort(500, message="Não foi possível obter extrato")
