class RoboReativoSimples:
    """
    Agente inteligente
    Robo Aspirador Reativo Simples
    """

    def __init__(self):
        self.regras = {
            'sujo': 'limpar',
            'quarto-A': 'direita',
            'quarto-B': 'esquerda'
        }
        
    def agir(self, nomeQuarto, status):
        if status:
            estado = 'sujo'
            return self.regras[estado]
        return self.regras[nomeQuarto]
        