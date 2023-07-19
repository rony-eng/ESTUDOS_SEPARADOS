#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO 
#ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO: 1=BINÁRIO 2=OCTAL 3=HEXADECIMAL

print('')
print('----------------------------------------')

nume = int(input('Insira um número para a conversão: '))
base = int(input('Qual base deseja? [1 = BINÁRIO] [2 = OCTAL] [3 = HEXADECIMAL]: '))

print('----------------------------------------')
print('')

if base == 1:
    print('CONVERSÃO BINÁRIA:')
    print('RESULTADO [{}]'.format(bin(nume)[2:]))
    print('')
elif base == 2:
    print('CONVERSÃO OCTAL:')
    print('RESULTADO [{}]'.format(oct(nume)[2:]))
    print('')
elif base == 3:
    print('CONVERSÃO HEXADECIMAL:')
    print('RESULTADO [{}]'.format(hex(nume)[2:]))
    print('')
else:
    print('Opção Invalida! Tente Novamente.')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO VERSÃO DO CURSO
#num = int(input('Digite um número inteiro: '))
#print('''Escolha uma das bases para conversão:
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''')
#opção = int(input('Sua opção: '))
#if opção == 1:
#    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
#elif opção == 2:
#    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
#elif opção == 3:
#    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
#else:
#    print('Opção inválida. Tente novamente.')