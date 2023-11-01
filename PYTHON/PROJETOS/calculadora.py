# MONTAR PROJETO DE CALCULOS MATEMÁTICOS COMO, SABER A SEQUÊNCIA DE FIBONACCI
# OU ARÉA DE UM RETANGULO, OU SABER A HIPOTENUSA...
import math
print('')
print('-=-' * 10)
print('OPERAÇÕES:')
print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
''')
print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
operação = int(input('ESCOLHA > [1] [2] [3] [4] [5] [0]: '))
print('-=-' * 10)
print('')

while operação != 0:
    if operação == 1: #operação de soma
            print('[OPERAÇÃO DE SOMAR]')
            n1 = int(input('Insira o primeiro número: '))
            n2 = int(input('Insira o segundo número: '))
            soma = n1 + n2
            print('')
            print('O resultado de {} + {} = {}.'.format(n1, n2, soma))
            print('')
            escolha = str(input('[DESEJA FAZER UMA NOVA OPERAÇÃO] [S/N]: '))
            if escolha in 'Ss':
                print('')
                print('-=-' * 10)
                print('OPERAÇÕES:')
                print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
                ''')
                print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
                operação = int(input('QUAL OPERAÇÃO DESEJA EFETUAR: '))
                print('-=-' * 10)
                print('')
            else:
                break
    elif operação == 2: #operação de subtrair
        print('[OPERAÇÃO DE SUBTRAIR]')
        n1 = int(input('Insira o primeiro número: '))
        n2 = int(input('Insira o segundo número: '))
        sub = n1 - n2
        print('')
        print('O resultado de {} - {} = {}.'.format(n1, n2, sub))
        print('')
        escolha = str(input('[DESEJA FAZER UMA NOVA OPERAÇÃO] [S/N]: '))
        if escolha in 'Ss':
            print('')
            print('-=-' * 10)
            print('OPERAÇÕES:')
            print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
                ''')
            print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
            operação = int(input('QUAL OPERAÇÃO DESEJA EFETUAR: '))
            print('-=-' * 10)
            print('')
        else:
            break
    elif operação == 3: #operação de dividir
        print('[OPERAÇÃO DE DIVIDIR]')
        n1 = int(input('Insira o primeiro número: '))
        n2 = int(input('Insira o segundo número: '))
        div = n1 / n2
        print('')
        print('O resultado de {} / {} = {}.'.format(n1, n2, div))
        print('')
        escolha = str(input('[DESEJA FAZER UMA NOVA OPERAÇÃO] [S/N]: '))
        if escolha in 'Ss':
            print('')
            print('-=-' * 10)
            print('OPERAÇÕES:')
            print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
                ''')
            print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
            operação = int(input('QUAL OPERAÇÃO DESEJA EFETUAR: '))
            print('-=-' * 10)
            print('')
        else:
            break
    elif operação == 4: #operação de multiplicar
        print('[OPERAÇÃO DE MULTIPLICAR]')
        n1 = int(input('Insira o primeiro número: '))
        n2 = int(input('Insira o segundo número: '))
        mul = n1 * n2
        print('')
        print('O resultado de {} * {} = {}.'.format(n1, n2, mul))
        print('')
        escolha = str(input('[DESEJA FAZER UMA NOVA OPERAÇÃO] [S/N]: '))
        if escolha in 'Ss':
            print('')
            print('-=-' * 10)
            print('OPERAÇÕES:')
            print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
                ''')
            print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
            operação = int(input('QUAL OPERAÇÃO DESEJA EFETUAR: '))
            print('-=-' * 10)
            print('')
        else:
            break
    elif operação == 5: #operação de fatorial
        print('OPERAÇÃO DE FATORIAL')
        num = int(input('Insira um número e descubra seu fatorial: '))
        f = math.factorial(num)
        print('')
        print('O fatorial de {} é {}'.format(num, f))
        print('')
        escolha = str(input('[DESEJA FAZER UMA NOVA OPERAÇÃO] [S/N]: '))
        if escolha in 'Ss':
            print('')
            print('-=-' * 10)
            print('OPERAÇÕES:')
            print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
                ''')
            print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
            operação = int(input('QUAL OPERAÇÃO DESEJA EFETUAR: '))
            print('-=-' * 10)
            print('')
        else:
            break
    else:
        print('OPERAÇÃO INCORRETA! TENTE NOVAMENTE')
        print('')
        print('-=-' * 10)
        print('OPERAÇÕES:')
        print('''
            [1] SOMAR
            [2] SUBTRAIR
            [3] DIVIDIR
            [4] MULTIPLICAR
            [5] FACTORIAL
            [0] FECHAR PROGRAMA
            ''')
        print('OBS: POR ENQUANTO ESTAMOS FUNCIONANDO COM OPERAÇÕES SIMPLES DE DOIS NÚMEROS.')
        operação = int(input('ESCOLHA > [1] [2] [3] [4] [5] [0]: '))
        print('-=-' * 10)
        print('')

print('FIM DO PROGRAMA!')

# O PRIMEIRO TERMO E A RAZÃO DE UMA PA
#print('')
#primeiro = int(input('Primeiro termo: '))
#razão = int(input('Razão da PA: '))
#termo = primeiro
#cont = 1
#while cont <= 10:
    #print('{} -> '.format(termo), end='')
    #termo = termo + razão
    #cont += 1
#print('FIM')