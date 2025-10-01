from model import Atividade
from database import db
from datetime import datetime

class AtividadeService:
    @staticmethod
    def get_all():
        return Atividade.query.all()

    @staticmethod
    def get_by_funcional(funcional):
        return Atividade.query.filter_by(funcional=funcional).all()

    @staticmethod
    def create(registo_atividade):
        atividade = Atividade(
            funcional=registo_atividade["funcional"], 
            dataHora=datetime.fromisoformat(registo_atividade["dataHora"]),
            codigoAtividade=registo_atividade["codigoAtividade"],
            descricaoAtividade=registo_atividade["descricaoAtividade"],
        )
        
        db.session.add(atividade)
        db.session.commit()
        return atividade


