#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR 80KM/H , MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

print('')
print('------------------------------')
vel = int(input('Insira sua velocidade: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado no valor de {}R$!'.format(multa))
print('------------------------------')

# DESAFIO CONCLUÍDO, FALTA VER RESOLUÇÃO