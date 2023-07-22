#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA 
#E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE: ATÉ 9 ANOS MIRIM, ATÉ 14 ANOS INFANTIL, ATÉ 19 ANOS JUNIOR, ATÉ 20 ANOS SÊNIOR, ACIMA MASTER
from datetime import date
print('')
print('----------------------------------------')

ano_nascimento = int(input('[INFORME SEU ANO DE NASCIMENTO] '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('----------------------------------------')
print('')

if idade <= 9:
    print('{} anos'.format(idade))
    print('[CATEGORIA MIRIN]')
elif idade <= 14:
    print('{} anos'.format(idade))
    print('[CATEGORIA INFANTIL]')
elif idade <= 19:
    print('{} anos'.format(idade))
    print('[CATEGORIA JUNIOR]')
elif idade > 19 and idade <= 20:
    print('{} anos'.format(idade))
    print('[CATEGORIA SÊNIOR]')
else:
    print('{} anos'.format(idade))
    print('[CATEGORIA MASTER]')

print('')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO