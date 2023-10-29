# MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR
# MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.

print('')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razão
    cont += 1
print('FIM')

print('')
novo_termo = str(input('Gostaria de inserir novo termo? [S/N]'))
while novo_termo not in 'Nn':
    if novo_termo in 'Ss':
        primeiro = int(input('Primeiro termo: '))
        razão = int(input('Razão da PA: '))
        termo = primeiro
        cont = 1
        while cont <= 10:
            print('{} -> '.format(termo), end='')
            termo = termo + razão
            cont += 1
        print('FIM')

        print('')
        novo_termo = str(input('Gostaria de inserir novo termo? [S/N]'))
    else:
        break

print('FIM DO PROGRAMA!')

# DESAFIO CONCLUÍDO