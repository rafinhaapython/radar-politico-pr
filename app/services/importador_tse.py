from pathlib import Path
import requests


class ImportadorTSE:

    def __init__(self):
        self.pasta_dados = Path("data/raw")
        self.pasta_dados.mkdir(parents=True, exist_ok=True)

    def listar_arquivos(self):
        arquivos = list(self.pasta_dados.glob("*"))

        if not arquivos:
            print("Nenhum arquivo encontrado em data/raw")
            return

        print("\nArquivos encontrados:\n")

        for arquivo in arquivos:
            print(arquivo.name)

    def baixar_arquivo(self, url, nome_arquivo):
        destino = self.pasta_dados / nome_arquivo

        if destino.exists():
            print(f"{nome_arquivo} já existe.")
            return

        print("Baixando arquivo...")

        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()

        with open(destino, "wb") as arquivo:
            for bloco in resposta.iter_content(1024):
                if bloco:
                    arquivo.write(bloco)

        print("Download concluído!")