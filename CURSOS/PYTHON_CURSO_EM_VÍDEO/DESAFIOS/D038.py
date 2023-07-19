#ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM: 
#O PRIMEIRO VALOR É MAIOR, O SEGUNDO VALOR É MAIOR, NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.

print('')
print('----------------------------------------')

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

print('----------------------------------------')
print('')

if num1 > num2:
    print('O número {} é maior que {}.'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que {}.'.format(num2, num1))
else:
    print('Não existe valor maior, os dois são iguais!')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DO CURSO

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')