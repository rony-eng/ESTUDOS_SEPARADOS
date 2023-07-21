#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, 
#DE ACORDO COM A MÉDIA ATINGIDA: MÉDIA ABAIXO DE 5.0 REPROVADO, MÉDIA ENTRE 5.0 E 6.9 RECUPERAÇÃO, MÉDIA 7.0 OU SUPERIOR APROVADO.

print('')
print('----------------------------------------')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

print('----------------------------------------')
print('')

media = (n1 + n2) / 2
if media < 5.0:
    print('[REPROVADO]')
    print('Sua média foi de {:.2f}.'.format(media))
elif media > 5.0 and media < 6.9:
    print('[RECUPERAÇÃO]')
    print('Sua média foi de {:.2f}.'.format(media))
else:
    print('[APROVADO]')
    print('Sua média foi de {:.2f}.'.format(media))

print('')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')