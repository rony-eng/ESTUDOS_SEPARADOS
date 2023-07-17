#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA 
#VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SÁLARIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

print('')
print('----------------------------------------')

vlc = float(input('Insira o valor da casa: '))
sal = float(input('Insira seu salário: '))
anos = int(input('Em quantos anos você pretende pagar? '))

print('----------------------------------------')
print('')


porcentagem = (30*sal) / 100
valor_prestacao = vlc / (anos * 12)

if valor_prestacao > porcentagem:
    print('A prestação ficou no valor de {:.2f}R$ mensais.'.format(valor_prestacao))
    print('A prestação excedeu os 30% do seu sálario que é no valor de {}R$'.format(porcentagem))
    print('Emprestimo negado!')
else:
    print('Emprestimo autorizado!')
    print('A prestação ficou no valor de {:.2f}R$ mensais.'.format(valor_prestacao))

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM CURSO EM VÍDEO
# casa = float(input('Valor da casa: R$'))
# salário = float(input('Salário do comprador: R$'))
# anos = int(input('Quantos anos de financiamento? '))
# prestação = casa / (anos * 12)
# mínimo = salário * 30 / 100
# print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
# print(' a prestação será de R${:.2f}'.format(prestação))
# if prestação <= mínimo:
#     print('Emprestimo pode ser CONCEDIDO!')
# else:
#     print('Emprestimo NEGADO!')