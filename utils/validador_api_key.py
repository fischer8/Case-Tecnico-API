from flask import Flask, request
from utils.app_error import AppError

app = Flask(__name__)

API_KEY = "case_tecnico"

def check_api_key(f):
    def decorated(*args, **kwargs):
        key = request.headers.get("x-api-key")

        if key != API_KEY:
            raise AppError("Chave API inválida", code=401)

        return f(*args, **kwargs)
    decorated.__name__ = f.__name__ 
    return decorated