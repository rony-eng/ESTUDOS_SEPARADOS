# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))