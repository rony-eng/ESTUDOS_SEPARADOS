# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE 
# ELA COMEÇA OU NÃO COM O NOME “SANTO”.

print('')
cidade = str(input('Insira o nome de uma cidade: ')).strip() # strip() elimina os espaços
print(cidade[:5].upper() == 'SANTO')
print('')