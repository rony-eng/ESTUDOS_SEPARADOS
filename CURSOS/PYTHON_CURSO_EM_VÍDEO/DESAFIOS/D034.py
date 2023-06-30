#ESCREVA UM PROGRAMA QUE PERGUNTE O SÁLARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SÁLARIOS SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAIS O AUMENTO É DE 15%
salario = float(input('Insira seu sálario e descubra seu aumento: '))
aum10 = (salario * 10) / 100
aum15 = (salario * 15) / 100

if salario > 1.250:
    print('O aumento no seu sálario será de {}R$.'.format(aum10))
else:
    print('O aumento no seu sálario será de {}R$.'.format(aum15))

# DESAFIO CONCLUÍDO ----------------------------------------------

# RESOLUÇÃO SEGUNDO CURSO ----------------------------------------
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))