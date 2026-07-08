from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Candidato(Base):
    __tablename__ = "candidatos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    nome_urna: Mapped[str]
    numero: Mapped[str]
    partido: Mapped[str]
    cargo: Mapped[str]
    municipio: Mapped[str]

    from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Candidato(Base):
    __tablename__ = "candidatos"

    id: Mapped[int] = mapped_column(primary_key=True)

    ano_eleicao: Mapped[int] = mapped_column(Integer)

    nome_completo: Mapped[str] = mapped_column(String(200))

    nome_urna: Mapped[str] = mapped_column(String(120))

    numero: Mapped[str] = mapped_column(String(10))

    partido: Mapped[str] = mapped_column(String(20))

    cargo: Mapped[str] = mapped_column(String(100))

    municipio: Mapped[str] = mapped_column(String(120))

    uf: Mapped[str] = mapped_column(String(2))

    situacao: Mapped[str] = mapped_column(String(100))

    patrimonio_total: Mapped[float] = mapped_column(Float)