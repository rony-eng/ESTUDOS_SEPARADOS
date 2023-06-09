# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua poção inteira.
# Ex: Digite o número: 6,127
# o número 6,127 tem a parte inteira 6

# estratégia 1
import math # biblioteca para funções matemática
num = float(input('Digite um número: '))
print('O número foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))

# estratégia 2
num = float(input('Digite um número: '))
print('O número foi {} e a sua porção inteira é {}.'.format(num, int(num)))