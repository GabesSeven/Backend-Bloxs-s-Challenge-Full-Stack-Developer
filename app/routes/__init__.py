from flask import Blueprint

conta_bp = Blueprint('conta', __name__)
pessoa_bp = Blueprint('pessoa', __name__)
login_bp = Blueprint('login', __name__)

from app.routes import conta, pessoa, login  # Importação das rotas
