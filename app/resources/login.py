from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)
from passlib.hash import pbkdf2_sha256

from db import db
from models import PessoaModel
from schemas import PessoaSchema, LoginSchema
from blocklist import BLOCKLIST

blp = Blueprint("Login", "login", description="Autenticação e controle de usuário")

@blp.route("/login")
class LoginView(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, dados_login):
        usuario = PessoaModel.query.filter(
            PessoaModel.email == dados_login["email"]
        ).first()
        
        if usuario and pbkdf2_sha256.verify(dados_login["senha"], usuario.senha):
            token_acesso = create_access_token(identity=usuario.id_pessoa, fresh=True)
            token_refresh = create_refresh_token(usuario.id_pessoa)
            return {"token_acesso": token_acesso, "token_refresh": token_refresh}, 200

        abort(401, message="Credenciais inválidas.")

@blp.route("/logout")
class LogoutView(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"mensagem": "Sessão encerrada com sucesso."}, 200

@blp.route("/refresh")
class AtualizacaoTokenView(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        usuario_atual = get_jwt_identity()
        novo_token = create_access_token(identity=usuario_atual, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"token_acesso": novo_token}, 200
