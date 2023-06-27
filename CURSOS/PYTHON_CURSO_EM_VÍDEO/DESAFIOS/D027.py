# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E ULTIMO NOME SEPARADAMENTE.

# EX: ANA MARIA DE SOUZA

# - PRIMEIRO: ANA
# - ULTIMO: SOUZA

print('')
print('------------------------------')
n = str(input('Insira seu nome completo: ')).strip().upper()
nome = n.split()

print('')
print('[SEU PRIMEIRO NOME É {}]'.format(nome[0]))
print('[SEU SEGUNDO NOME É {}]'.format(nome[1]))
print('[SEU ÚLTIMO NOME É {}]'.format(nome[len(nome)-1]))
print('------------------------------')
print('')

# DESAFIO COMPLETO