import sqlite3
import pandas as pd

def consolidar_dados_pr():
    conn = sqlite3.connect("radar.db")
    
    # Lista de tabelas que queremos unir (focando no PR)
    tabelas_pr = [
        "consulta_cand_2024_PR",
        "bem_candidato_2024_PR",
        "rede_social_candidato_2024_PR"
    ]
    
    for nome_tabela in tabelas_pr:
        # Lê os dados da tabela original
        df = pd.read_sql(f"SELECT * FROM {nome_tabela}", conn)
        
        # Cria uma tabela "limpa" chamada 'pr_candidatos', 'pr_bens', etc
        novo_nome = nome_tabela.replace("_2024_PR", "").lower()
        df.to_sql(f"pr_{novo_nome}", conn, if_exists='replace', index=False)
        print(f"✅ Tabela pr_{novo_nome} criada.")
    
    conn.close()

if __name__ == "__main__":
    consolidar_dados_pr()