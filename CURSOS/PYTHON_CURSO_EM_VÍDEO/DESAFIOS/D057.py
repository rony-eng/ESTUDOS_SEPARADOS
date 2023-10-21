# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS 
# VALORES ‘M’ OU ‘F’. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE 
# ATÉ TER UM VALOR CORRETO
sexo = str(input('Qual o seu sexo? [M]/[F] ')).upper()

while sexo != 'SAIR':
    if sexo == 'M':
        print('Seu sexo é masculino!')
        break
    if sexo == 'F':
        print('Seu sexo é feminino!')
        break
    print('')
    print('RESPOSTA ERRADA! TENTE NOVAMENTE!')    
    sexo = str(input('Qual o seu sexo? [M]/[F] ')).upper()


# RESPOSTA DE ACORDO COM O CURSO

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por Favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

# DESAFIO CONCLUÍDO