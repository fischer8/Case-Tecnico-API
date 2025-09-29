from database import db

class Atividade(db.Model):
    __tablename__ = "atividades"

    idAtividade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funcional = db.Column(db.Integer, nullable=False)
    codigoAtividade = db.Column(db.String(20), nullable=False)  
    dataHora = db.Column(db.DateTime, nullable=False)
    descricaoAtividade = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "idAtividade": self.idAtividade,
            "funcional": self.funcional,
            "dataHora": self.dataHora.isoformat(),
            "codigoAtividade": self.codigoAtividade,
            "descricaoAtividade": self.descricaoAtividade,
        }

