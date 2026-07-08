from pathlib import Path
import zipfile
import pandas as pd


class ETL:

    def extrair_zip(self, arquivo_zip, destino):

        destino = Path(destino)

        destino.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(arquivo_zip, "r") as zip_ref:
            zip_ref.extractall(destino)

        print("Arquivo descompactado com sucesso!")

    def ler_csv(self, arquivo):

        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin1",
            low_memory=False
        )

        print(df.head())

        return df