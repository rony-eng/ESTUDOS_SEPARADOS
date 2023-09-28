# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
numero = int(input('Insira um número para saber sua tabuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(numero, i, numero*i))

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
