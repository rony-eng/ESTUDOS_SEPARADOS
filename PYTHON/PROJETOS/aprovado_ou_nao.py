init = input('Deseja iniciar o programa: ')

while init != 'N' or 'n':
    print('')
    idade = int(input('Digite sua idade: '))
    mdi = idade >= 18

    if idade == 0:
        break

    if mdi: #true
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade.')
