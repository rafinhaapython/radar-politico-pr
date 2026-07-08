import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Configuração inicial da página
st.set_page_config(page_title="Radar Político PR", layout="wide")

st.title("📊 Radar Político 2024 - Paraná")

# Função para conectar ao banco e ler dados
def carregar_dados_sql(query):
    conn = sqlite3.connect("radar.db")
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# --- SEU CÓDIGO ANTERIOR ---
# (Mantenha aqui os filtros ou gráficos que você já tinha feito antes)

# --- RANKING DOS MILIONÁRIOS (Corrigido) ---
st.divider()
st.subheader("💰 Top 10 Candidatos Mais Ricos (PR)")

try:
    # Query focada nas tabelas exatas do seu banco
    query_ricos = """
    SELECT 
        c.NM_CANDIDATO, 
        SUM(b.VR_BEM_CANDIDATO) as PATRIMONIO_TOTAL
    FROM consulta_cand_2024_PR c
    JOIN bem_candidato_2024_PR b ON c.SQ_CANDIDATO = b.SQ_CANDIDATO
    GROUP BY c.NM_CANDIDATO
    ORDER BY PATRIMONIO_TOTAL DESC
    LIMIT 10
    """
    
    df_ricos = carregar_dados_sql(query_ricos)
    
    # Exibir gráfico de barras
    if not df_ricos.empty:
        fig = px.bar(
            df_ricos, 
            x='PATRIMONIO_TOTAL', 
            y='NM_CANDIDATO', 
            orientation='h',
            title="Patrimônio Declarado (Top 10)",
            labels={'PATRIMONIO_TOTAL': 'Valor em R$', 'NM_CANDIDATO': 'Candidato'}
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Não foram encontrados dados de patrimônio para o PR.")

except Exception as e:
    st.error(f"Erro ao carregar o ranking: {e}")
    st.write("Verifique se os nomes das tabelas no banco de dados correspondem exatamente ao SQL acima.")