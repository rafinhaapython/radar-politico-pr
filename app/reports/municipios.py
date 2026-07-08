from sqlalchemy import func

from app.database.session import SessionLocal
from app.models.candidatos import Candidato


def main():
    db = SessionLocal()

    print("\nCANDIDATOS POR MUNICÍPIO\n")

    resultados = (
        db.query(
            Candidato.municipio,
            func.count(Candidato.id)
        )
        .group_by(Candidato.municipio)
        .order_by(func.count(Candidato.id).desc())
        .all()
    )

    for municipio, total in resultados:
        print(f"{municipio}: {total}")

    db.close()


if __name__ == "__main__":
    main()