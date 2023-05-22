nome = str(input('Digite o nome de algum membro da família: '))
pai = 'raimundo'
mae = 'maria'
filhos = [
    'valdiano', 'valdiana', 'claudiana', 'claudiano', 'hadyla', 'rony', 'roniely'
]
familia = [
    pai, mae, filhos
]

while nome != 'sair':
    if nome in familia:
        print('Membro é pai ou mãe da família.')
        nome = str(input('Digite o nome de algum membro da família: '))
    elif nome in filhos:
        print('Membro é filho(a) da família.')
        nome = str(input('Digite o nome de algum membro da família: '))
    else:
        print('Membro não faz parte da família.')
        nome = str(input('Digite o nome de algum membro da família: '))

print('Seu programa acabou')