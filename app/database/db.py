import sqlite3
from pathlib import Path


class Database:

    def __init__(self):
        self.db_path = Path("data/radar.db")
        self.db_path.parent.mkdir(exist_ok=True)

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def criar_tabelas(self):

        conn = self.conectar()

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

        )
        """)

        conn.commit()

        conn.close()

        print("✅ Banco preparado com sucesso!")