#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
#quer ou não continuar. No final mostre:
#    A) quantas pessoas tem mais de 18 anos.
#    B) quantos homens foram cadastrados
#    C) quantas mulheres tem menos de 20 anos

continuar = 'Ss'
while continuar in 'Ss':
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    continuar = str(input('Deseja cadastrar outra pessoa? '))
    print('')
    if continuar in 'Nn':
        break