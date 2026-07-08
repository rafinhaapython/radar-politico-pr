class CandidatoService:

    def pesquisar(
        self,
        session,
        nome=None,
        partido=None,
        cargo=None,
        municipio=None,
        situacao=None,
        ano=None,
    ):