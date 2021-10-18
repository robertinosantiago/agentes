from Coisa import Coisa
import collections

class Agente(Coisa):


    def __init__(self, programa=None) -> None:
        self.vivo = True
        self.desempenho = 0
        self.programa = programa
