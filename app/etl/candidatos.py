from pathlib import Path
import pandas as pd


class ETLCandidatos:

    def carregar(self, arquivo):

        arquivo = Path(arquivo)

        if not arquivo.exists():
            raise FileNotFoundError(f"{arquivo} não encontrado.")

        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin1",
            low_memory=False
        )

        print(f"\nTotal de registros: {len(df)}")

        return df