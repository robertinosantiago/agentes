import random

class Quarto:
    """
    Classe para definir quartos a serem limpos pelo robô
    """
    def __init__(self, nome):
        #self.status = 'sujo'
        #self.quantidadeSujeira = random.randint(1,100)
        self.nome = nome
    
    def getNome(self):
        return self.nome

    #def getStatus(self):
    #    return self.status
    
    #def setStatus(self, status):
    #    self.status = status

    #def getQuantidadeSujeira(self):
    #    return self.quantidadeSujeira

    #def setQuantidadeSujeira(self, quantidade):
    #    self.quantidadeSujeira = quantidade

    def __repr__(self) -> str:
        return self.nome