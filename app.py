from flask import Flask, jsonify
from database import db
from controller import atividades
from utils.app_error import AppError

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(atividades)

    with app.app_context():
        db.create_all()

    @app.errorhandler(AppError)
    def http_exception(e):
        print(e)
        return jsonify({
            "erro": e.message,
            "codigo": e.code,
        }), e.code
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "erro": "Rota não encontrada",
            "codigo": 404
        }), 404
    
    @app.errorhandler(Exception)
    def server_exception(e):
        return jsonify({
            "erro": "Erro interno no servidor",
            "codigo": 500
        }), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
