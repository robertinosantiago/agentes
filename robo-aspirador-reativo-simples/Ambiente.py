from Coisa import Coisa
from Agente import Agente
import random

class Ambiente:

    def __init__(self, quartos) -> None:
        self.coisas = []
        self.agentes = []
        self.quartos = quartos
        
        self.status = {}
        for quarto in self.quartos:
            #self.status[quarto] = random.choice(['limpo', 'sujo'])
            self.status[quarto] = 'sujo'

        print("\nStatus inicial dos quartos")
        print(self.status)

    def perceber(self, agente):
        return agente.localizacao, self.status[agente.localizacao]

    def executarAcao(self, agente, acao):
        if acao == 'direita':
            agente.localizacao = self.quartos[1]
            agente.desempenho -= 1
        elif acao == 'esquerda':
            agente.localizacao = self.quartos[0]
            agente.desempenho -= 1
        elif acao == 'limpar':
            if self.status[agente.localizacao] == 'sujo':
                agente.desempenho += 10
                '''
                @TODO: melhorar essa busca
                '''
                for i in range(len(self.quartos)):
                    if self.quartos[i] == agente.localizacao:
                        self.quartos[i].quantidadeSujeira -= 1
                        if self.quartos[i].estaLimpo():
                            self.status[agente.localizacao] = 'limpo'
            

    def localizacaoPadrao(self, coisa):
        return random.choice(self.quartos)

    def mudanca(self):
        pass

    def passo(self):
        if not self.estaFinalizado():
            acoes = []
            for agente in self.agentes:
                if agente.vivo:
                    acoes.append(agente.programa(self.perceber(agente)))
                else:
                    acoes.append("")
            for (agente, acao) in zip(self.agentes, acoes):
                self.executarAcao(agente, acao)
            self.mudanca()


    def executar(self, passos=1000):
        while not self.estaFinalizado():
            self.passo()
        #for passo in range(passos):
        #    if self.estaFinalizado():
        #        return
        #    self.passo()

    def estaFinalizado(self):
        for quarto in self.quartos:
            if not quarto.estaLimpo():
                return False
        return True
        #return any(quarto.estaLimpo() for quarto in self.quartos)
        #return not any(agente.estaVivo() for agente in self.agentes)

    def adicionaCoisa(self, coisa, localizacao=None):
        if not isinstance(coisa, Coisa):
            coisa = Agente(coisa)
        if coisa in self.coisas:
            print('Não é possível adicionar a mesma coisa duas vezes')
        else:
            coisa.localizacao = localizacao if localizacao is not None else self.localizacaoPadrao(coisa)
            self.coisas.append(coisa)
            if isinstance(coisa, Agente):
                self.agentes.append(coisa)
    
    def removeCoisa(self, coisa):
        try:
            self.coisas.remove(coisa)
        except ValueError as e:
            print(e)
        if coisa in self.agentes:
            self.agentes.remove(coisa)