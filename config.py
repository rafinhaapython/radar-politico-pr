from pathlib import Path

# Estado que será analisado
UF = "PR"

# Ano da eleição
ANO_ELEICAO = 2024

# Pasta principal dos dados
DATA_DIR = Path("data")

# Pasta dos arquivos baixados
RAW_DIR = DATA_DIR / "raw"

# Pasta dos arquivos processados
PROCESSED_DIR = DATA_DIR / "processed"

# Banco SQLite
DATABASE_PATH = DATA_DIR / "radar.db"