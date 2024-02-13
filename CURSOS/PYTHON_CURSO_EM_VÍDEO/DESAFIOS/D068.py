#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder.
#Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# MINHA RESOLUÇÃO
print('')
jogador = int(input('Seu valor:  '))
if jogador % 2 == 0:
    print('Sua escolha foi PAR!')
else:
    print('Sua escolha foi IMPAR!')
print('')

# RESOLUÇÃO DE ACORDO COM O CURSO

#from random import randint
#v = 0
#while True:
#    jogador = int(input('Diga um valor: '))
#    computador = randint(0, 10)
#    total = jogador + computador
#    tipo = ''
#    while tipo not in 'PI':
#        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
#    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
#    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
#    if tipo == 'P':
#        if total % 2 == 0:
#            print('Você VENCEU!')
#            v += 1
#        else:
#            print('Você PERDEU!')
#            break
#    elif tipo == 'I':
#        if total % 2 == 1:
#            print('Você VENCEU!')
#            v += 1
#        else:
#            print('Você PERDEU!')
#            break
#    print('Vamos jogar novamente...')
#print(f'GAME OVER! Você venceu {v} vezes.')
