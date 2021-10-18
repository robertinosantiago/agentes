from RoboReativoSimples import RoboReativoSimples
from Quarto import Quarto
from Regra import Regra
from Agente import Agente
from Ambiente import Ambiente

def temSujeira(quartos):
    for quarto in quartos:
        if quarto.getStatus():
            return True
    return False

def interpretador(estado):
    return estado

quartoA = Quarto('quarto-A')
quartoB = Quarto('quarto-B')

regras = [
    Regra((quartoA, 'sujo'), 'limpar'),
    Regra((quartoB, 'sujo'), 'limpar'),
    Regra((quartoA, 'limpo'), 'direita'),
    Regra((quartoB, 'limpo'), 'esquerda'),
]

quartos = [quartoA, quartoB]
robo = RoboReativoSimples(regras, interpretador)
programa = robo.getPrograma()

agente = Agente(programa)
ambiente = Ambiente(quartos)
ambiente.adicionaCoisa(agente)
ambiente.executar()

print("\nStatus final dos quartos")
print(ambiente.status)

print("Desempenho do agente: {}".format(agente.desempenho))

assert ambiente.status == {quartoA: 'limpo', quartoB: 'limpo'}
