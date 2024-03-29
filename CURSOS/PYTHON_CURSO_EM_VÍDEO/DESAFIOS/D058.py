# MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI ‘PENSAR’ EM UM
# NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ
# ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA
# VENCER.
import random
from time import sleep

contador = 1
escolha = [1,2,3,4,5,6,7,8,9,10]
computador = random.choice(escolha) # faz o computador 'pensar'

print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3) # faz o computador "dormir" por 3 segundos.

while jogador != computador:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))
    print('TENTE NOVAMENTE!')
    print('')
    contador += 1
    computador = random.choice(escolha) # faz o computador 'pensar'
    jogador = int(input('Em que número eu pensei? '))

print('PARABENS! Você conseguiu me vencer em {} tentativas!'.format(contador))

# RESOLUÇÃO DE ACORDO COM O CURSO
# OBS: COLOCANDO SE O JOGADOR ESTAR MAIS PERTO OU LONGE, COM O
# COMPUTADOR DIZENDO SE ESTAR MAIS PERTO OU MENOS.

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas!'.format(palpites))
