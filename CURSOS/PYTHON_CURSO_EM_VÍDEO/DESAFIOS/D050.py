# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES, SE O VALOR DIGITADO FOR IMPAR DESCONSIDERE-O.
soma = 0
for i in range(1, 7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares é {}'.format(soma))

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))