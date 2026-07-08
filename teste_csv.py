from app.etl.read_csv import LeitorCSV


arquivo = "data/extracted/consulta_cand_2024_PR.csv"


leitor = LeitorCSV()

df = leitor.ler(arquivo)