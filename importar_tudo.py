import pandas as pd
import sqlite3
import os
import glob

# Pasta onde você extraiu os CSVs
PASTA_EXTRACTED = "data/extracted"
DB_PATH = "radar.db"

def importar_todos_csvs():
    conn = sqlite3.connect(DB_PATH)
    # Procura todos os arquivos .csv na pasta
    arquivos = glob.glob(os.path.join(PASTA_EXTRACTED, "*.csv"))
    
    for arquivo in arquivos:
        nome_tabela = os.path.basename(arquivo).replace(".csv", "")
        print(f"Importando {nome_tabela}...")
        
        try:
            # O encoding 'latin-1' é essencial para dados do TSE
            df = pd.read_csv(arquivo, sep=';', encoding='latin-1', low_memory=False)
            df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
            print(f"✅ Tabela {nome_tabela} criada com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao importar {nome_tabela}: {e}")
            
    conn.close()

if __name__ == "__main__":
    importar_todos_csvs()