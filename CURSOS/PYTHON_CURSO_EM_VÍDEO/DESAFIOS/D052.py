# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

# RESOLUÇÃO DE ACORDO COM O CURSO
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\nO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('É por isso ele é PRIMO')
else:
    print('É por isso ele NÃO É PRIMO')