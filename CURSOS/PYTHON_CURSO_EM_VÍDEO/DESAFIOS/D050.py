# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES, SE O VALOR DIGITADO FOR IMPAR DESCONSIDERE-O.
soma = 0
for i in range(1, 7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares é {}'.format(soma))