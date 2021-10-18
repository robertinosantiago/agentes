from Regra import Regra

class RoboReativoSimples:
    """
    Agente inteligente
    Robo Aspirador Reativo Simples
    """

    def __init__(self, regras, interpretador):
        self.regras = regras
        self.interpretador = interpretador

    def encontrarRegra(self, estado, regras):
        for regra in regras:
            if regra.eIgual(estado):
                return regra
        return None

    def programa(self, percepcao):
        estado = self.interpretador(percepcao)
        regra = self.encontrarRegra(estado, self.regras)
        acao = regra.getAcao()
        return acao

    def getPrograma(self):
        return self.programa

    def agir(self, nomeQuarto, status):
        if status:
            estado = 'sujo'
            return self.regras[estado]
        return self.regras[nomeQuarto]
        