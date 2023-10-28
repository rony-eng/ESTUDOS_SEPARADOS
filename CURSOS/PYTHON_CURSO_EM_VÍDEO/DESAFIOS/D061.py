# D061 REFAÇA O DESAFIO 051 LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA,
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.
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
