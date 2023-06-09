# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m2

l = int(input('Qual a largura de sua parede? '))
a = int(input('Qual a altura de sua parede? '))

area = l * a
litro = int(area / 2)

print('A área de sua parede é {}m e {} litros de tintas para pintar ela toda'.format(area, litro))