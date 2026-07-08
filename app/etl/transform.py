import pandas as pd


class TransformadorCandidatos:

    def preparar(self, df):

        print("🔄 Preparando dados...")

        dados = df[
            [
                "SQ_CANDIDATO",
                "ANO_ELEICAO",
                "SG_UF",
                "NM_UE",
                "DS_CARGO",
                "NR_CANDIDATO",
                "NM_CANDIDATO",
                "NM_URNA_CANDIDATO",
                "SG_PARTIDO",
                "DS_SITUACAO_CANDIDATURA"
            ]
        ].copy()


        dados.columns = [
            "sq_candidato",
            "ano",
            "uf",
            "municipio",
            "cargo",
            "numero",
            "nome",
            "nome_urna",
            "partido",
            "situacao"
        ]


        print("✅ Dados preparados!")

        print(dados.head())

        return dados