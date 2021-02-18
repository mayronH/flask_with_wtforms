"""Inicializa a aplicação Flask"""
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # Carrega as configurações de config.py
    app.config.from_object("config.Config")

    with app.app_context():
        # Chamas as rotas de routes.py
        from . import routes

        return app