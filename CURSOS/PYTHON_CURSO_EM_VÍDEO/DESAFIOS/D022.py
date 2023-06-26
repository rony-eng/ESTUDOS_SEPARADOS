# D022: CRIE UM PROGRAMA QUE LEIA ONOME COMPLETO DE UMA PESSOA E MOSTRE:

# - O NOME COM TODAS AS LETRAS MAIÚSCULAS
# - O NOME COM TODAS MINÚSCULAS
# - QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

print('------------------------------')
nome = str(input('Insira seu nome completo: ')).strip() #strip() elimina os espaços antes e depois
separa = nome.split() # split() separa o nome em uma lista

print('')
print('Analisando seu nome...')
print('')
print('[Letras Maiusculas:] ', nome.upper()) # letras maiusculas
print('[Letras Minusculas:] ', nome.lower()) # letras minusculas
print('[Cumprimento String:]', len(nome)-nome.count(' '), 'letras') # Cumprimento da String, count() elimina os espaços entre os nomes
print('[Comprimento 1° Nome:]',separa[0], ':', len(separa[0]), 'letras')
print('')

print(separa)
print('------------------------------')