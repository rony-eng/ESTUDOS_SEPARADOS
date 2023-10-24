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

# RESOLUÇÃO DE ACORDO COM O CURSO
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('''
          [ 1 ] somar
          [ 2 ] multiplicar
          [ 3 ] maior
          [ 4 ] novos números
          [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')