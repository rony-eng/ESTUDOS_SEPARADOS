# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.
# EX: 5° = 5x4x3x2x1 = 120

# from math import factorial
# num = int(input('Insira um número e descubra seu fatorial: '))
# f = factorial(num)
# print('O fatorial de {} é {}'.format(num, f))

# RESOLUÇÃO DE ACORDO COM O CURSO
num = int(input('Insira um número e descubra seu fatorial: '))
c = num
f = 1 
print('Calculando {}!'.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

# DESAFIO CONCLUÍDO
# DESAFIO PROPOSTO, FAZER O MESMO DESAFIO COM O FOR