# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4  PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
# → A MÉDIA DE IDADE DO GRUPO
# → QUAL É O NOME DO HOMEM MAIS VELHO
# → QUANTAS MULHERES TEM MENOS DE 20 ANOS.

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('')
print('----- RESULTADO -----')
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
print('')