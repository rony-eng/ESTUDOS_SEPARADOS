# Um professor quer sortear um dos seus quatro alunos 
# para apagar o quadro. Faça um programa que ajuda ele, 
# lendo o nome deles e escrevendo o nome do escolhido.

import random #biblioteca para gerar números pseudo-aleatórios

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

sorteio = [a1, a2, a3, a4]
escolhido = random.choice(sorteio) #comando para sortear

print('O aluno escolhido foi {}.'.format(escolhido))
