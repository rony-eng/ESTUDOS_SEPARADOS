#nome = str(input('Qual o seu nome? '))
#if nome == 'Rony':
#    print(nome, 'Menezes')
#print('Bom dia!', nome)

# ----------------------------------- #

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(n))
if n >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')