#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL 
#E CONDIÇÃO DE PAGAMENTO: Á VISTA DINHEIRO / CHEQUE 10% DE DESCONTO, À VISTA NO CARTÃO 5% DE DESCONTO, 
#EM ATÉ 2X NO CARTÃO PREÇO NORMAL, 3X OU MAIS NO CARTÃO 20% DE JUROS.

print('')
print('----------------------------------------')

print('[OPÇÕES DE PAGAMENTO:]')
print('1 [EM DINHEIRO]')
print('2 [CHEQUE - 10% DE DESCONTO]')
print('3 [CARTÃO À VISTA - 5% DE DESCONTO]')
print('4 [2X NO CARTÃO - PREÇO NORMAL]')
print('5 [3X OU MAIS NO CARTÃO - 20% DE JUROS]')

print('----------------------------------------')
print('')

p_x = 150
op = int(input('INFORME SUA FORMA DE PAGAMENTO: '))

if op == 1:
    print('1 [EM DINHEIRO]')
    print('O PRODUTO FICA NO VALOR DE {:.0f}R$'.format(p_x))
elif op == 2:
    d = (p_x * 10) / 100
    print('2 [CHEQUE - 10% DE DESCONTO]')
    print('DESCONTO DE {:.0f}R$'.format(d))
    print('O PRODUTO FICA NO VALOR DE {:.0f}R$'.format(p_x - d))
elif op == 3:
    d = (p_x * 5) / 100
    print('3 [CARTÃO À VISTA - 5% DE DESCONTO]')
    print('DESCONTO DE {:.0f}R$'.format(d))
    print('O PRODUTO FICA NO VALOR DE {:.0f}R$'.format(p_x - d))
elif op == 4:
    print('4 [2X NO CARTÃO - PREÇO NORMAL]')
    print('O PRODUTO FICA NO VALOR DE {:.0f}R$'.format(p_x))
elif op == 5:
    j = (p_x * 20) / 100
    print('5 [3X OU MAIS NO CARTÃO - 20% DE JUROS]')
    print('JUROS DE {:.0f}R$'.format(j))
    print('O PRODUTO FICA NO VALOR DE {:.0f}R$'.format(p_x + j))
else:
    print('[OPÇÃO INVALIDA!]')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO
preço = float(input('Preço das compras: R$ '))
print(''' Formas de Pagamento
[1] á vista dinheiro / cheque
[2] á visa cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcela em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('OPÇÃO INVALIDA!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))