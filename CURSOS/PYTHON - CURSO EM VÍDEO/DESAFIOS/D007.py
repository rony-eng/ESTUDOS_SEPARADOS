# Desenvolva um programa que leia os duas 
# notas de um aluno, calcule e mostre a sua média. ordem de precedência
# a média é calculada somando-se todos os valores de um conjunto de dados e dividindo-se pelo número de elementos deste conjunto.

n1 = int(input('Insira a 1° nota: '))
n2 = int(input('Insira a 2° nota: '))
n3 = int(input('Insira a 3° nota: '))
n4 = int(input('Insira a 4° nota: '))

m = (n1 + n2 + n3 + n4) / 4

print('A sua média é: {}'.format(m))