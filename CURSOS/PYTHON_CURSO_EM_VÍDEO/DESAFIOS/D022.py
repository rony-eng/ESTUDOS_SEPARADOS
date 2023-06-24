# D022: CRIE UM PROGRAMA QUE LEIA ONOME COMPLETO DE UMA PESSOA E MOSTRE:

# - O NOME COM TODAS AS LETRAS MAIÚSCULAS
# - O NOME COM TODAS MINÚSCULAS
# - QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = input('Insira seu nome completo: ')

print('')
print('[Letras Maiusculas:] ', nome.upper()) # letras maiusculas
print('[Letras Minusculas:] ', nome.lower()) # letras minusculas
print('[Cumprimento String:]', len(nome), 'letras') # Cumprimento da String
print('[Comprimento 1° Nome:]')
print('')