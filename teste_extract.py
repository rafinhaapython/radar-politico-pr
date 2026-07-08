from app.etl.extract import Extractor

extractor = Extractor()

extractor.extrair("data/raw/consulta_cand_2024.zip")