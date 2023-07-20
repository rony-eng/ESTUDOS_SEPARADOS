#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE: 
#SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA DE SE ALISTAR, SE JÁ PASSOU DO TEMPO 
#DE ALISTAMENTO. SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU PASSOU DO PRAZO.

from datetime import date

print('')
print('----------------------------------------')

ano_n = int(input('Informe seu ano de nascimento: '))
ano_a = date.today().year

print('----------------------------------------')
print('')

resultado = ano_a - ano_n
if resultado < 18:
    comparação = 18 - resultado
    print('Você ainda vai se alistar!')
    print('Falta {} anos para você se alistar'.format(comparação))
elif resultado == 18:
    print('Está na hora de se alistar!')
else:
    comparação = resultado - 18
    print('Você já passou da hora de se alistar!')
    print('{} anos atrasados para o alistamento'.format(comparação))

print('')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO