from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime
from db import db
from ..models import ContaModel, TransacaoModel
from schemas import ContaSchema, TransacaoSchema

# Instância de Blueprint
blp = Blueprint('conta', __name__, url_prefix='/conta')

@blp.route("/conta")
class ContaView(MethodView):
    """
    CRIAR CONTA
    """
    @blp.arguments(ContaSchema)
    @blp.response(201, ContaSchema)
    def post(self, tag_data):
        try:
            nova_conta = ContaModel(
                id_pessoa=tag_data['id_pessoa'],
                saldo=tag_data['saldo'],
                limite_saque_diario=tag_data['limite_saque_diario'],
                flag_ativo=tag_data['flag_ativo'],
                tipo_conta=tag_data['tipo_conta'],
                data_criacao=datetime.now().date()
            )
            db.session.add(nova_conta)
            db.session.commit()
            return nova_conta, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))

    """
    DELETAR / BLOQUEAR CONTA
    """
    @blp.response(204)
    def delete(self, id_conta):
        conta = ContaModel.query.get(id_conta)
        if not conta:
            abort(404, message='Conta não encontrada')

        try:
            conta.flag_ativo = False
            db.session.commit()
            return {'message': 'Conta bloqueada com sucesso'}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))

    """
    SALDO DE CONTA
    """
    # @blp.response(200, ContaSchema(many=True))
    @blp.response(200, ContaSchema)
    def get(self, id_conta):
        conta = ContaModel.query.get(id_conta)
        if not conta:
            abort(404, message='Conta não encontrada')

        return {'saldo': float(conta.saldo)}, 200

@blp.route("/operacao")
class ContaOperacaoView(MethodView):
    """
    DEPÓSITO
    """
    @blp.arguments(TransacaoSchema)
    @blp.response(200, TransacaoSchema)
    def put(self, id_conta):
        data = request.json
        conta = ContaModel.query.get(id_conta)
        if not conta:
            abort(404, message='Conta não encontrada')

        try:
            conta.saldo += data['valor']
            nova_transacao = TransacaoModel(
                id_conta=id_conta,
                valor=data['valor'],
                data_transacao=datetime.now().date()
            )
            db.session.add(nova_transacao)
            db.session.commit()
            return {'message': 'Depósito realizado com sucesso'}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))

    """
    SAQUE
    """
    @blp.response(200, TransacaoSchema)
    def delete(self, id_conta):
        data = request.json
        conta = ContaModel.query.get(id_conta)
        if not conta:
            abort(404, message='Conta não encontrada')

        if conta.saldo < data['valor']:
            abort(400, message='Saldo insuficiente')

        try:
            conta.saldo -= data['valor']
            nova_transacao = TransacaoModel(
                id_conta=id_conta,
                valor=-data['valor'],
                data_transacao=datetime.now().date()
            )
            db.session.add(nova_transacao)
            db.session.commit()
            return {'message': 'Saque realizado com sucesso'}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))

    """
    EXTRATO
    """
    @blp.response(200, TransacaoSchema(many=True))
    def get(self, id_conta):
        conta = ContaModel.query.get(id_conta)
        if not conta:
            abort(404, message='Conta não encontrada')

        try:
            transacoes = TransacaoModel.query.filter_by(id_conta=id_conta).all()
            extrato = [{'id_transacao': t.id_transacao, 'valor': float(t.valor), 'data_transacao': str(t.data_transacao)} for t in transacoes]
            return {'extrato': extrato}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
