# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.quanto vale metro e centimetro e converta o numero escrito

n = int(input('Insira o número que será convertido: '))
c = n * 100
m = n * 1000

print('O valor em centimetro é {} o valor em milimetro é {}'.format(c, m))

