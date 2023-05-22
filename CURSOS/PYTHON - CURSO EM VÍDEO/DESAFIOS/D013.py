# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo sálario, com 15% de aumento

n = int(input('Insira seu sálario atual: '))
ad = int(15 * n / 100)

print('Seu novo sálario com 15% de aumento é {}R$'.format(n + ad))
print ('O aumento foi de {}'.format(ad))