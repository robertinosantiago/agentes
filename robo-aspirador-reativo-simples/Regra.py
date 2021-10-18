class Regra:

    def __init__(self, estado, acao) -> None:
        self.estado = estado
        self.acao = acao

    def eIgual(self, estado) -> bool:
        return self.estado == estado

    def getAcao(self):
        return self.acao
    