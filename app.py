from flask import Flask, jsonify
from database import db
from controller import atividades
from werkzeug.exceptions import HTTPException

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///atividades.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(atividades)

    with app.app_context():
        db.create_all()

    @app.errorhandler(HTTPException)
    def http_exception(e):
        return jsonify({
            "erro": e.description,
            "codigo": e.code,
        }), e.code

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

