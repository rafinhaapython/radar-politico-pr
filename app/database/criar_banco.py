from app.database.database import engine
from app.models.base import Base

# Importa os modelos para que o SQLAlchemy os registre
from app.models.candidatos import Candidato


def criar_banco():
    Base.metadata.create_all(engine)
    print("Banco criado com sucesso!")