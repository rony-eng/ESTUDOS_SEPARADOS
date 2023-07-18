#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO 
#ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO: 1=BINÁRIO 2=OCTAL 3=HEXADECIMAL

print('')
print('----------------------------------------')

num = int(input('Insira um número para a conversão: '))
base = input('Qual base deseja? [1 = BINÁRIO] [2 = OCTAL] [3 = HEXADECIMAL]: ')

print('----------------------------------------')
print('')

if base == '1':
    print('CONVERSÃO BINÁRIA:')
    print('RESULTADO []')
    print('')
elif base == '2':
    print('CONVERSÃO OCTAL:')
    print('RESULTADO []')
    print('')
else:
    print('CONVERSÃO HEXADECIMAL:')
    print('RESULTADO []')
    print('')