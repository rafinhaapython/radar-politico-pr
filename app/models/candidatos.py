from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Candidato(Base):
    __tablename__ = "candidatos"

    id: Mapped[int] = mapped_column(primary_key=True)

    sq_candidato: Mapped[int] = mapped_column(Integer, unique=True)

    ano_eleicao: Mapped[int] = mapped_column(Integer)

    nome_urna: Mapped[str] = mapped_column(String(150))

    nome_civil: Mapped[str] = mapped_column(String(200))

    numero: Mapped[str] = mapped_column(String(10))

    partido: Mapped[str] = mapped_column(String(20))

    cargo: Mapped[str] = mapped_column(String(80))

    municipio: Mapped[str] = mapped_column(String(120))

    uf: Mapped[str] = mapped_column(String(2))

    situacao: Mapped[str] = mapped_column(String(80))

    patrimonio: Mapped[float] = mapped_column(Float)