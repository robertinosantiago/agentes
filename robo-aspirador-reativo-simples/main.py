from RoboReativoSimples import RoboReativoSimples
from Quarto import Quarto

def temSujeira(quartos):
    for quarto in quartos:
        if quarto.getStatus():
            return True
    return False

quartos = [Quarto('quarto-A'), Quarto('quarto-B')]
robo = RoboReativoSimples()

indice = 0
while temSujeira(quartos):
    acao = robo.agir(quartos[indice].getNome(), quartos[indice].getStatus());
    if acao == 'limpar':
        totalSujeiraQuarto = quartos[indice].getQuantidadeSujeira()
        quartos[indice].setQuantidadeSujeira(totalSujeiraQuarto-1)
        if quartos[indice].getQuantidadeSujeira() == 0:
            quartos[indice].setStatus(0)
    if acao == 'direita':
        indice = 1
    if acao == 'esquerda':
        indice = 0
    print(quartos[indice])
