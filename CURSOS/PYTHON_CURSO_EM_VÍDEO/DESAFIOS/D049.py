# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
num = int(input('Insira um número para saber sua tabuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))

# DESAFIO CONCLUÍDO