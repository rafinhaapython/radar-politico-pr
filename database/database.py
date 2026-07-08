from sqlalchemy import create_engine

# Caminho do banco SQLite
DATABASE_URL = "sqlite:///data/radar.db"

# Cria a conexão com o banco
engine = create_engine(DATABASE_URL, echo=True)

print("Conexão criada com sucesso!")