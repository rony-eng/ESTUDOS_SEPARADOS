# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO, NO FINAL DA EXECUÇÃO,
# MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. 
# O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.

núm = int(input('Insira um valor:  '))
cont = 0
soma = 0
maior = 0
menor = 0
while núm != 0:
    soma += núm
    cont += 1
    média = soma / cont
    núm = int(input('Insira um valor:  '))
    if núm < núm:
        maior = núm
    elif núm > núm:
        menor = núm
print()
print('-=' * 30)
print('A média dos valores digitados é {}'.format(média))
print('O maior valor digitado foi {}'.format(maior))
#print('O menor valor digitado foi {}')

# resolução de acordo com o curso
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}',format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Acabou')