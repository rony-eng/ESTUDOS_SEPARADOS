#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR 80KM/H , MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

print('')
print('------------------------------')
vel = int(input('Insira sua velocidade: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado no valor de {}R$!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
print('------------------------------')

# DESAFIO CONCLUÍDO ----------------------------------------------

# RESOLUÇÃO SEGUNDO CURSO ----------------------------------------
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')