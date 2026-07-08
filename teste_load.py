from app.etl.read_csv import LeitorCSV
from app.etl.transform import TransformadorCandidatos
from app.etl.load import CarregadorCandidatos


arquivo = "data/extracted/consulta_cand_2024_PR.csv"


# EXTRACT

leitor = LeitorCSV()

df = leitor.ler(arquivo)


# TRANSFORM

transformador = TransformadorCandidatos()

dados = transformador.preparar(df)


# LOAD

carregador = CarregadorCandidatos()

carregador.salvar(dados)