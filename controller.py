from flask import Blueprint, request, jsonify, abort
from service import AtividadeService
from datetime import datetime

atividades = Blueprint("atividades", __name__)

@atividades.route("/atividades", methods=["GET"])
def get_atividades():
    atividades = AtividadeService.get_all()
    return jsonify([a.to_dict() for a in atividades])


@atividades.route("/atividades/<int:funcional>", methods=["GET"]) 
def get_atividades_by_funcional(funcional): 
    atividades = AtividadeService.get_by_funcional(funcional) 

    if not atividades:
        abort(404, description=f"Nenhuma atividade encontrada para {funcional}")

    return jsonify([a.to_dict() for a in atividades])


@atividades.route("/atividades", methods=["POST"])
def create_atividade():
    data = request.get_json()
    required_fields = ["funcional", "dataHora", "codigoAtividade", "descricaoAtividade"]

    for field in required_fields:
        if field not in data:
            abort(400, description=f"Campo '{field}' é obrigatório")

    try:
        datetime.fromisoformat(data["dataHora"])
    except ValueError:
        abort(400, description="Campo 'dataHora' deve estar no formato ISO (YYYY-MM-DDTHH:MM:SS)")

    atividade = AtividadeService.create(data)
    return jsonify({ "mensagem": "Atividade cadastrada com sucesso!", "atividade": atividade.to_dict()}), 201

