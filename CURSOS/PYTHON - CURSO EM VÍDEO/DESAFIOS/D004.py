# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

a = input('Digite algo:')

print ('O tipo primitivo desse valor é ', type(a))  # para mostrar o tipo primitivo
print ('Só tem espaços? ', a.isspace())             # para saber se é espaço
print ('É um número? ', a.isnumeric())              # para saber se é um número
print ('É alfabético? ', a.isalpha())               # para saber se é alfabético
print ('É alfanúmerico?', a.isalnum())              # para saber se é alfanúmerico
print ('Está em maiúscula? ', a.isupper())          # para saber se é maiúscula
print ('Está em minúscula? ', a.islower())          # para saber se é minúscula
print ('Está capitalizada? ', a.istitle())          # para saber se é captalizada (Se tá maiúscula e minúscula)