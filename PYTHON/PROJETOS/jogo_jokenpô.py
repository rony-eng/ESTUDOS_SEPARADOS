from random import randint
from time import sleep

print('INICIANDO JOGO')
print('''Suas opções:
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

while jogador != 0:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0,2)
    print('-=' * 11)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    if jogador == 1:
        print('Jogador jogou Pedra')
    elif jogador == 2:
        print('Jogador jogou Papel')
    elif jogador == 3:
        print('Jogador jogou Tesoura')

    print('Computador jogou {}'.format(itens[computador]))
    if computador == 0: # computador jogou Pedra
        if jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        elif jogador == 3:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif computador == 1: # computador jogou Papel
        if jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        elif jogador == 3:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif computador == 2: # computador jogou Tesoura
        if jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        elif jogador == 3:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')
    print('-=' * 11)
    print('''Suas opções:
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    

print('FIM DE JOGO')
# JOGO CONCLUÍDO