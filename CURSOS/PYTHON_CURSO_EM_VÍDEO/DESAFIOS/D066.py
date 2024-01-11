#Crie um programa que leia vários números inteiros pelo teclado.  O programa só
#vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final mostra quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print()
n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} números digitados vale {s}')
print()