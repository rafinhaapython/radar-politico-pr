from pathlib import Path
import zipfile


class Extractor:

    def extrair(self, arquivo_zip):

        arquivo_zip = Path(arquivo_zip)

        destino = Path("data/extracted")

        destino.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(arquivo_zip, "r") as zip_ref:
            zip_ref.extractall(destino)

        print("✅ Arquivo extraído com sucesso!")

        return destino