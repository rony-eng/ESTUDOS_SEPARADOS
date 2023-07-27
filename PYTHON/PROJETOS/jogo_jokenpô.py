from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('INICIANDO JOGO')
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

while jogador != 00:
    print('-=' * 11)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('Jogador jogou {}'.format(itens[jogador]))
    print('Computador jogou {}'.format(itens[computador]))
    if computador == 0: # computador jogou Pedra
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif computador == 1: # computador jogou Papel
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif computador == 2: # computador jogou Tesoura
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')
    print('-=' * 11)
    print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    

print('FIM DE JOGO')
# JOGO INCOMPLETO / FALTA AJEITAR UM ERRO QUANDO COLOCA O NUMERO 0 NO JOGADOR, ELE FECHA O JOGO O QUE NÃO 
# ERA PRA ACONTECER.