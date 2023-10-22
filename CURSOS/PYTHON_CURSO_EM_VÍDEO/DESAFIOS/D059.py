# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA

# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

print('')
print('[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] MAIOR')
print('[4] NOVOS NÚMEROS')
print('[5] SAIR DO PROGRAMA')
escolha = int(input('ESCOLHA A OPERAÇÃO QUE VOCÊ DESEJA: '))
print('')

while escolha != 0:
    if escolha == 1:
        soma = num1 + num2
        print(soma)
        nova_escolha = str(input('DESEJA FAZER UMA NOVA OPERAÇÃO: [S/N] '))
        if nova_escolha == 'S' or 's':
            print('')
            print('[1] SOMAR')
            print('[2] MULTIPLICAR')
            print('[3] MAIOR')
            print('[4] NOVOS NÚMEROS')
            print('[5] SAIR DO PROGRAMA')
            escolha = int(input('ESCOLHA A OPERAÇÃO QUE VOCÊ DESEJA: '))
            print('')
        else:
            break

    if escolha == 2:
        multiplicação = num1 * num2
        print(multiplicação)
        nova_escolha = str(input('DESEJA FAZER UMA NOVA OPERAÇÃO: [S/N] '))
        if nova_escolha == 'S' or 's':
            print('')
            print('[1] SOMAR')
            print('[2] MULTIPLICAR')
            print('[3] MAIOR')
            print('[4] NOVOS NÚMEROS')
            print('[5] SAIR DO PROGRAMA')
            escolha = int(input('ESCOLHA A OPERAÇÃO QUE VOCÊ DESEJA: '))
            print('')
        else:
            break

    if escolha == 3:
        if num1 > num2:
            print('O número maior é {}.'.format(num1))
            nova_escolha = str(input('DESEJA FAZER UMA NOVA OPERAÇÃO: [S/N] '))
            if nova_escolha == 'S' or 's':
                print('')
                print('[1] SOMAR')
                print('[2] MULTIPLICAR')
                print('[3] MAIOR')
                print('[4] NOVOS NÚMEROS')
                print('[5] SAIR DO PROGRAMA')
                escolha = int(input('ESCOLHA A OPERAÇÃO QUE VOCÊ DESEJA: '))
                print('')
            else:
                break
        else:
            print('O número maior é {}.'.format(num2))
            nova_escolha = str(input('DESEJA FAZER UMA NOVA OPERAÇÃO: [S/N] '))
            if nova_escolha == 'S' or 's':
                print('')
                print('[1] SOMAR')
                print('[2] MULTIPLICAR')
                print('[3] MAIOR')
                print('[4] NOVOS NÚMEROS')
                print('[5] SAIR DO PROGRAMA')
                escolha = int(input('ESCOLHA A OPERAÇÃO QUE VOCÊ DESEJA: '))
                print('')
            else:
                break

    if escolha == 4:
        num1 = int(input('Insira o primeiro valor: '))
        num2 = int(input('Insira o segundo valor: '))
        print('')
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] MAIOR')
        print('[4] NOVOS NÚMEROS')
        print('[5] SAIR DO PROGRAMA')
        escolha = int(input('ESCOLHA A OPERAÇÃO QUE VOCÊ DESEJA: '))

    if escolha == 5:
        break

print('FIM DO PROGRAMA!')