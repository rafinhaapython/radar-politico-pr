from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Candidato(Base):
    __tablename__ = "candidatos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    nome_urna = Column(String)
    numero = Column(String)
    partido = Column(String)
    cargo = Column(String)
    municipio = Column(String)
    ano = Column(Integer)
    votos = Column(Integer)
    patrimonio = Column(Float)