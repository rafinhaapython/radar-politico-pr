from app.database.db import Database


class CarregadorCandidatos:

    def salvar(self, df):

        print("💾 Salvando no banco...")

        db = Database()

        conn = db.conectar()

        df.to_sql(
            "candidatos",
            conn,
            if_exists="append",
            index=False
        )

        conn.close()

        print(f"✅ {len(df)} candidatos importados!")