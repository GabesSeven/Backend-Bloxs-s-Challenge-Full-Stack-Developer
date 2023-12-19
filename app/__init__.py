from flask import Flask
from flask_migrate import Migrate

import os

from db import db

def create_app():
    app = Flask(__name__)

    # Conguração Banco de Dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    db.init_app(app)
    migrate = Migrate(app, db)    

    # Conguração rotas
    from app.routes.conta import conta_bp
    from app.routes.pessoa import pessoa_bp
    from app.routes.login import login_bp
    app.register_blueprint(conta_bp)
    app.register_blueprint(pessoa_bp)
    app.register_blueprint(login_bp)

    return app
