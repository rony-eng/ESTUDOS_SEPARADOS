# Faça um programa que leia um ângulo qualquer e mostre na tela 
# o valor de seno, cosseno e tangente desse ângulo

import math #biblioteca para funções matemática

ang = float(input('Coloque o ângulo: '))

seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}.'.format(ang, seno))

cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(ang, cos))

tan = math.tan(math.radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(ang, tan))