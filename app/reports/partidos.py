from app.database.db import Database


class RelatorioPartidos:

    def executar(self):

        db = Database()

        conn = db.conectar()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                partido,
                COUNT(*) quantidade
            FROM candidatos
            GROUP BY partido
            ORDER BY quantidade DESC
        """)

        resultados = cursor.fetchall()

        conn.close()

        return resultados


if __name__ == "__main__":

    relatorio = RelatorioPartidos()

    dados = relatorio.executar()

    print("\nCANDIDATOS POR PARTIDO\n")

    for partido, quantidade in dados:
        print(f"{partido}: {quantidade}")