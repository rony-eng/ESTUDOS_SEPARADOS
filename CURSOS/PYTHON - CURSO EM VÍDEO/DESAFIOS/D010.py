# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. quanto estar a cotação 
# do dolar e multiplique. Considere USS 1.00 = 3,27 

n = int(input('Insera quanto dinheiro você tem na carteira e veja quantos dolares você pode comprar:'))
cd = int(3.27)

print('{} é o valor em dolar que seu dinheiro pode comprar'.format(n/cd))