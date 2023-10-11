# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))