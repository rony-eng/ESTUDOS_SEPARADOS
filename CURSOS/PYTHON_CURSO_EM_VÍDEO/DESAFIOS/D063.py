# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E
# MOSTRE NA TELA AS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI.
# EX: 0→1→1→2→3→5→8
# FORMULA = F(n + 2) = F(n + 1) + F(n)

n = int(input('Insira um número e descubra sua sequência de Fibonacci: '))
q_elementos = int(input('Quantos elementos da sequência deseja ver? '))
c = 0
while c < q_elementos:
    f = (n+1) + n
    print(f)
    c += 1
    f = (f+1) + f
    print(f)

# DESAFIO INCOMPLETO