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


# INCOMPLETO