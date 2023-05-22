# programa que pede um nome e fala se o nome está na familia e se é pai, mãe ou filho
nome = str(input('Digite o nome de um membro da família: '))
filhos = [
    'rony', 'roniely', 'hadyla', 'claudiano', 'claudiana', 'valdiana', 'valdiano'
]
pais = [
    'maria', 'raimundo'
]

if nome in pais:
    print('Membro é pai ou mãe da família.')
elif nome in filhos:
    print('Membro é filho(a) da família.')
else:
    print('Membro não faz parte da família.')

# está dando erro ainda não resolvido