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
from schemas import PessoaSchema
from blocklist import BLOCKLIST


blp = Blueprint("Login", "login", description="Autenticação e controle de usuário")

@blp.route("/registro")
class RegistroUsuarioView(MethodView):
    @blp.arguments(PessoaSchema)
    def post(self, dados_usuario):
        if PessoaSchema.query.filter(PessoaSchema.email == dados_usuario["email"]).first():
            abort(409, message="Já existe um usuário com esse e-mail.")

        usuario = PessoaSchema(
            email=dados_usuario["email"],
            senha=pbkdf2_sha256.hash(dados_usuario["senha"]),
        )
        db.session.add(usuario)
        db.session.commit()

        return {"mensagem": "Usuário criado com sucesso."}, 201

@blp.route("/login")
class LoginView(MethodView):
    @blp.arguments(PessoaSchema)
    def post(self, dados_usuario):
        usuario = PessoaSchema.query.filter(
            PessoaSchema.email == dados_usuario["email"]
        ).first()

        if usuario and pbkdf2_sha256.verify(dados_usuario["senha"], usuario.senha):
            token_acesso = create_access_token(identity=usuario.id, fresh=True)
            token_refresh = create_refresh_token(usuario.id)
            return {"token_acesso": token_acesso, "token_refresh": token_refresh}, 200

        abort(401, message="Credenciais inválidas.")

@blp.route("/logout")
class LogoutView(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"mensagem": "Sessão encerrada com sucesso."}, 200

@blp.route("/usuario/<int:id_usuario>")
class UsuarioView(MethodView):
    @blp.response(200, PessoaSchema)
    def get(self, id_usuario):
        usuario = PessoaSchema.query.get_or_404(id_usuario)
        return usuario

    def delete(self, id_usuario):
        usuario = PessoaSchema.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return {"mensagem": "Usuário deletado."}, 200

@blp.route("/refresh")
class AtualizacaoTokenView(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        usuario_atual = get_jwt_identity()
        novo_token = create_access_token(identity=usuario_atual, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"token_acesso": novo_token}, 200
