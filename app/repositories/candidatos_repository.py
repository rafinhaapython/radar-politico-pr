from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.candidatos import Candidato


class CandidatoRepository:

    def __init__(self, session: Session):
        self.session = session

    def buscar(self):

        return self.session.query(Candidato)

    def listar(self):

        return (
            self.session
            .query(Candidato)
            .order_by(Candidato.nome_urna)
            .all()
        )