from pathlib import Path
import pandas as pd


class ImportadorCandidatos:

    def importar(self, arquivo_csv):

        arquivo = Path(arquivo_csv)

        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

        print("📄 Lendo arquivo...")

        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin1",
            low_memory=False
        )

        print(f"Total de registros: {len(df)}")

        return df