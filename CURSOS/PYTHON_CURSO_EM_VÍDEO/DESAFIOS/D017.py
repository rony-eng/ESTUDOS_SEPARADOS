# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

import math #biblioteca para funções matematica

# estratégia 1, sem usar uma importação
co = float(input('Coloque o valor do cateto oposto: '))
ca = float(input('Coloque o valor do cateto adjacente: '))

h = (co**2 + ca**2) ** (1/2)

print('O comprimento da hipotenusa é {:.2f}'.format(h))

# estratégia 2, usando importação da biblioteca math com o metodo hypot
co = float(input('Coloque o valor do cateto oposto: '))
ca = float(input('Coloque o valor do cateto adjacente: '))

h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))