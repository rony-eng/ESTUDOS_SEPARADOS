#DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, 
#DE ACORDO COM A TABELA ABAIXO: ABAIXO DE 18.5 ABAIXO DO PESO, ENTRE 18.5 E 25 PESO IDEAL, 25 ATÉ 30 SOBREPESO, 
#30 ATÉ 40 OBESIDADE, ACIMA DE 40 OBESIDADE MÓRBIDA

print('')
print('----------------------------------------')

peso = float(input('[INFORME SEU PESO] '))
altura = float(input('[INFORME SUA ALTURA] '))
imc = peso / altura ** 2

print('----------------------------------------')
print('')

print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('[ABAIXO DO PESO]')
elif imc >= 18.5 and imc < 25:
    print('[PESO IDEAL]')
elif imc >= 25 and imc < 30:
    print('[SOBREPESO]')
elif imc >= 30 and imc < 40:
    print('[OBESIDADE]')
else:
    print('OBESIDADE MÓRBIDA')
print('')

# DESAFIO CONCLUÍDO

# RSOLUÇÃO DE ACORDO COM O CURSO