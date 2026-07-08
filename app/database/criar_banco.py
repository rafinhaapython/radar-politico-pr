import sqlite3
from pathlib import Path


DB_PATH = Path("data/radar.db")


def criar_banco():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidatos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        sq_candidato TEXT,

        ano INTEGER,

        uf TEXT,

        municipio TEXT,

        cargo TEXT,

        numero INTEGER,

        nome TEXT,

        nome_urna TEXT,

        partido TEXT,

        situacao TEXT

    );
    """)

    conn.commit()

    conn.close()

    print("Banco criado com sucesso!")