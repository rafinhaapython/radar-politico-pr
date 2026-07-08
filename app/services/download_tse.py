import requests
from pathlib import Path


class DownloadTSE:

    def baixar(self, url, destino):

        destino = Path(destino)

        destino.parent.mkdir(parents=True, exist_ok=True)

        print("Iniciando download...")

        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()

        with open(destino, "wb") as arquivo:
            for bloco in resposta.iter_content(1024):
                if bloco:
                    arquivo.write(bloco)

        print("Download concluído!")