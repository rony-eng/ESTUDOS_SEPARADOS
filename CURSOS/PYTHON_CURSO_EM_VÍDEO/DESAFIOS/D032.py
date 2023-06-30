#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE 
#SE ELE É BISSEXTO.
ano = int(input('Insira o ano em que estar para saber se é Bissexto: '))
if ano % 4 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é Bissexto!'.format(ano))

# DESAFIO CONCLUÍDO ----------------------------------------------

# RESOLUÇÃO SEGUNDO CURSO ----------------------------------------
from datetime import date
ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # para pegar o ano atual de sua maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # ano BISSEXTO TEM OUTRAS EXCEÇÕES
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))