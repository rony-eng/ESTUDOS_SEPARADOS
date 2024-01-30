#Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo
#usuário. O programa será interrompido quando o número solicitado for negativo.

num = int(input('Digite um número para ver sua tabuada: '))

while num >= 0:
    print('')
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num*c))
    print('')
    num = int(input('Digite um número para ver sua tabuada: '))

print('Fim do programa')

#Desafio concluído

#Resolução de acordo com o curso em vídeo
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')

