# Faça um programa que leia um número inteiro e mostra na tela seu sucessor e seu antecessor.

n = int (input('Insira um número:'))

a = int(-1)
s = int(+1)

print ('O antecessor do número que você digitou é {} e seu sucessor é {}'.format(n+a, n+s))

# se for só pra mostrar o resultado e não precisar guardar igual mostrado acima podemos usar assim:
# print('O antecessor do número que você digitou é {} e o seu sucesso é {}'.format(n-1, n+1))