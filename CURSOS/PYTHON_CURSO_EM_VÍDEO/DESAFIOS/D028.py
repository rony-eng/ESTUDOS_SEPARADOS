#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR “PENSAR” 
#EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO 
#TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

import random
pensar = [0,1,2,3,4,5]
escolhido = random.choice(pensar)
num = int(input('Digite um número de 0 a 5: '))
if num == escolhido:
    print('Número correto!')
else:
    print('Número incorreto!')
    print('Numero correto é {}!'.format(escolhido))

# DESAFIO CONCLUÍDO, FALTA VER RESOLUÇÃO