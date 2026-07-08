import pandas as pd


class LeitorCSV:

    def ler(self, arquivo):

        print("📄 Lendo arquivo CSV...")

        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin1",
            low_memory=False
        )

        print("\n✅ Arquivo carregado!")
        print(f"Total de registros: {len(df)}")

        print("\nColunas encontradas:")
        for coluna in df.columns:
            print("-", coluna)

        return df