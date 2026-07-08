import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_PATH

def realizar_analises():
    print("Conectando ao banco de dados...")
    # Cria a conexão com o banco SQLite usando o caminho do seu config.py
    engine = create_engine(f"sqlite:///{DATABASE_PATH}")

    try:
        # ATENÇÃO: Substitua 'candidatos' pelo nome real da sua tabela no banco!
        query = "SELECT * FROM candidatos"
        df = pd.read_sql(query, engine)
        
        print(f"\nSucesso! Foram carregados {len(df)} candidatos do banco.")
        
        # 1. Análise: Quantidade de candidatos por partido
        # Substitua 'sg_partido' pelo nome da coluna que tem a sigla do partido
        if 'sg_partido' in df.columns:
            print("\n--- Top 5 Partidos com mais candidatos ---")
            top_partidos = df['sg_partido'].value_counts().head(5)
            print(top_partidos)
        else:
            print("\nColuna de partido não encontrada. Verifique o nome da coluna.")

        # 2. Análise: Quantidade por Cargo
        # Substitua 'ds_cargo' pelo nome da coluna que tem o cargo
        if 'ds_cargo' in df.columns:
            print("\n--- Distribuição por Cargo ---")
            cargos = df['ds_cargo'].value_counts()
            print(cargos)

        # 3. Análise (Opcional): Candidatos mais ricos
        # Substitua 'vr_despesa_max_campanha' ou a coluna de bens se você tiver
        if 'vr_despesa_max_campanha' in df.columns:
            print("\n--- Top 5 Maiores Tetos de Gasto de Campanha ---")
            # Converte para numérico caso esteja como texto
            df['vr_despesa_max_campanha'] = pd.to_numeric(df['vr_despesa_max_campanha'], errors='coerce')
            top_ricos = df.nlargest(5, 'vr_despesa_max_campanha')[['nm_candidato', 'sg_partido', 'vr_despesa_max_campanha']]
            print(top_ricos)

    except Exception as e:
        print(f"\nErro ao ler o banco de dados. Detalhes: {e}")
        print("Dica: Verifique se o nome da tabela realmente é 'candidatos'.")

if __name__ == "__main__":
    realizar_analises()