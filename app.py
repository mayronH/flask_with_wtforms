"""Ponto de partida da aplicação."""
from app_wtforms import create_app

# Chama o método criado __init__.py
app = create_app()

if __name__ == "__main__":
    app.run()