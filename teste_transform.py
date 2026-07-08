from app.etl.read_csv import LeitorCSV
from app.etl.transform import TransformadorCandidatos


arquivo = "data/extracted/consulta_cand_2024_PR.csv"


leitor = LeitorCSV()

df = leitor.ler(arquivo)


transformador = TransformadorCandidatos()

dados = transformador.preparar(df)