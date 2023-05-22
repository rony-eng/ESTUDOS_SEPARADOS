# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n = int(input('Insira o valor do produto: '))
d = int(5 * n / 100)

print('O valor do produto com desconto é {}R$'.format(n - d))