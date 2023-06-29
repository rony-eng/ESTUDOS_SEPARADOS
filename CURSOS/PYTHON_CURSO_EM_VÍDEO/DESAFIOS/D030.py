#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO 
#E MOSTRE NA TELA SE ELE É PAR OU IMPAR.
num = int(input('Insira um número: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))

# DESAFIO CONCLUÍDO ----------------------------------------------

# RESOLUÇÃO SEGUNDO CURSO ----------------------------------------
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é IMPAR'.format(número))