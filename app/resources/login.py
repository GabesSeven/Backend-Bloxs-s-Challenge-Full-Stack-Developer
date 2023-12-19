
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from werkzeug.security import check_password_hash
from datetime import datetime
from db import db
from ..models import PessoaModel
from schemas import PessoaSchema

blp = Blueprint('login', __name__, url_prefix='/login')

class LoginView(MethodView):
    """
    AUTENTICAÇÃO
    """
    @blp.arguments(PessoaSchema)  
    @blp.response(200, PessoaSchema)  
    def post(self, tag_data):
        try:
            email = tag_data.get('email')  # Assumindo que o email é fornecido nos dados enviados

            # Busca a pessoa pelo email
            pessoa = PessoaModel.query.filter_by(email=email).first()

            if pessoa and check_password_hash(pessoa.senha_hash, tag_data.get('senha')):
                # Serializa os dados da Pessoa para retorno
                serialized_pessoa = {'id_pessoa': pessoa.id_pessoa, 'nome': pessoa.nome, 'email': pessoa.email}
                return serialized_pessoa, 200
            else:
                abort(401, message='Credenciais inválidas')
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))

