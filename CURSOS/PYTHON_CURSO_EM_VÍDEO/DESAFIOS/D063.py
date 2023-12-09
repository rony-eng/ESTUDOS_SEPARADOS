# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E
# MOSTRE NA TELA AS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI.
# EX: 0→1→1→2→3→5→8
# FORMULA = F(n + 2) = F(n + 1) + F(n)

#n = int(input('Insira um número e descubra sua sequência de Fibonacci: '))
#q_elementos = int(input('Quantos elementos da sequência deseja ver? '))
#c = 0
#while c < q_elementos:
#    f = (n+1) + n
#    print(f)
#    c += 1
#    f = (f+1) + f
#    print(f)

# DESAFIO INCOMPLETO

print('-' *  30)
print('Sequência de Fibonacci')
print('-' *  30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')