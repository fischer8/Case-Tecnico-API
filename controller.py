from flask import Blueprint, request, jsonify
from service import AtividadeService
from utils.validador_api_key import check_api_key
from datetime import datetime
from utils.app_error import AppError

atividades = Blueprint("atividades", __name__)

@atividades.route("/atividades", methods=["GET"])
@check_api_key
def get_atividades():
    atividades = AtividadeService.get_all()
    return jsonify([atividade.to_dict() for atividade in atividades])


@atividades.route("/atividades/<int:funcional>", methods=["GET"])
@check_api_key
def get_atividades_by_funcional(funcional): 
    atividades = AtividadeService.get_by_funcional(funcional) 

    if not atividades:
        raise AppError(f"Nenhuma atividade encontrada para {funcional}", code=404)

    return jsonify([atividade.to_dict() for atividade in atividades])


@atividades.route("/atividades", methods=["POST"])
@check_api_key
def create_atividade():
    atividade_json = request.get_json()
    required_fields = ["funcional", "dataHora", "codigoAtividade", "descricaoAtividade"]

    for field in required_fields:
        if field not in atividade_json:
            raise AppError(f"Campo '{field}' é obrigatório", code=400)

    try:
        datetime.fromisoformat(atividade_json["dataHora"])
    except ValueError:
        raise AppError("Campo 'dataHora' deve estar no formato ISO (YYYY-MM-DDTHH:MM:SS)", code=400)

    atividade = AtividadeService.create(atividade_json)
    return jsonify({ "mensagem": "Atividade cadastrada com sucesso!", "atividade": atividade.to_dict()}), 201



