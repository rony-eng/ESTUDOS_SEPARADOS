#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL 
#É O MAIOR E QUAL É O MENOR.
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 > n2 and n1 > n3 :
    print('')
    print('O número maior é {}'.format(n1))
    if n2 < n3 :
        print('O número menor é {}'.format(n2))
    else:
        print('O número menor é {}'.format(n3))

if n2 > n1 and n2 > n3 :
    print('')
    print('O número maior é {}'.format(n2))
    if n1 < n3 :
        print('O número menor é {}'.format(n1))
    else:
        print('O número menor é {}'.format(n3))

if n3 > n1 and n3 > n2 :
    print('')
    print('O número maior é {}'.format(n3))
    if n2 < n1 :
        print('O número menor é {}'.format(n2))
    else:
        print('O número menor é {}'.format(n1))
    
# DESAFIO CONCLUÍDO, AINDA NÃO VI A RESOLUÇÃO, ACREDITO QUE O CÓDIGO ESTÁ GRANDE