#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR “PENSAR” 
#EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO 
#TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

import random
from time import sleep

pensar = [0,1,2,3,4,5]
escolhido = random.choice(pensar)
num = int(input('Digite um número de 0 a 5: '))
if num == escolhido:
    print('Número correto!')
else:
    print('Número incorreto!')
    print('Numero correto é {}!'.format(escolhido))

# DESAFIO CONCLUÍDO ----------------------------------------------

# RESOLUÇÃO ------------------------------------------------------
computador = random.randiant(0,5) # faz o computador 'pensar'
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3) # faz o computador "dormir" por 3 segundos.
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))