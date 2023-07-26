#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ. 
import random
print('')
print('----------------------------------------')

print('[JOGO INICIADO]')
print('')

print('1 [PEDRA]')
print('2 [PAPEL]')
print('3 [TESOURA]')
minha_escolha = int(input('ESCOLHA UMA OPÇÃO: '))

opções = ['1 [PEDRA]', '2 [PAPEL]', '3 [TESOURA]']

while (minha_escolha != 0):
    if minha_escolha == 1:
        random.shuffle(opções) #comando para embalhara
        escolha_pc = random.choice(opções) #comando para sortear
        print('EU: ', '1 [PEDRA]')
        print('PC: ', escolha_pc)
        if escolha_pc == '1 [PEDRA]':
            print('RESULTADO: EMPATE')
        elif escolha_pc == '2 [PAPEL]':
            print('RESULTADO: PC VENCEU')
        elif escolha_pc == '3 [TESOURA]':
            print('RESULTADO: VOCÊ VENCEU')
    elif minha_escolha == 2:
        random.shuffle(opções) #comando para embalhara
        escolha_pc = random.choice(opções) #comando para sortear
        print('EU: ', '2 [PAPEL]')
        print('PC: ', escolha_pc)
        if escolha_pc == '1 [PEDRA]':
            print('RESULTADO: VOCÊ VENCEU')
        elif escolha_pc == '2 [PAPEL]':
            print('RESULTADO: EMPATE')
        elif escolha_pc == '3 [TESOURA]':
            print('RESULTADO: PC VENCEU')
    elif minha_escolha == 3:
        random.shuffle(opções) #comando para embalhara
        escolha_pc = random.choice(opções) #comando para sortear
        print('EU: ', '3 [TESOURA]')
        print('PC: ', escolha_pc)
        if escolha_pc == '1 [PEDRA]':
            print('RESULTADO: PC VENCEU')
        elif escolha_pc == '2 [PAPEL]':
            print('RESULTADO: VOCÊ VENCEU')
        elif escolha_pc == '3 [TESOURA]':
            print('RESULTADO: EMPATE')
    else:
        print('[ESCOLHA INVALIDA]')

    print('')
    minha_escolha = int(input('ESCOLHA UMA OPÇÃO: '))
    print('')

print('[JOGO ENCERRADO]')
print('----------------------------------------')
print('')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
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