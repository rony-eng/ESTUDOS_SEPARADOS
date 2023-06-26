# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA 
# TELA CADA UM DOS DIGITOS SEPARADOS.

# EX: DIGITE UM NÚMERO: 1834

# - UNIDADE: 4
# - DEZENA: 3
# - CENTENA: 8
# - MILHAR: 1

print('------------------------------')
num = int(input('Insira um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('')
print('[UNIDADE:]', u)
print('[DEZENA:]', d)
print('[CENTENA:]', c)
print('[MILHAR:]', m)
print('------------------------------')

# DESAFIO CONCLUÍDO, USANDO A MATEMÁTICA PARA RESOLVER, SEM CONDIÇÕES