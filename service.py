from models import Atividade
from database import db
from datetime import datetime
from flask import abort

class AtividadeService:
    @staticmethod
    def get_all():
        return Atividade.query.all()

    @staticmethod
    def get_by_funcional(funcional):
        return Atividade.query.filter_by(funcional=funcional).all()

    @staticmethod
    def create(data):
        atividade = Atividade(
            funcional=data["funcional"], 
            dataHora=datetime.fromisoformat(data["dataHora"]),
            codigoAtividade=data["codigoAtividade"],
            descricaoAtividade=data["descricaoAtividade"],
        )
        
        db.session.add(atividade)
        db.session.commit()
        return atividade

