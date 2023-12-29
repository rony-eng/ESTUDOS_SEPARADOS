# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, 
# QUE É A CONDIÇÃO DE PARADO. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS A QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG).


# minha resolução, incompleta
num = int(input('Digite um número inteiro: '))
contador = 0

while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != num:
        soma = num + num
    contador += 1

print('')
print('Você digitou {} números inteiros!'.format(contador))
print('a soma dos valores foi de {}!'.format(soma))
print('')

# resolução de acordo com o curso

núm = 0
cont = 0
soma = 0
# núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))