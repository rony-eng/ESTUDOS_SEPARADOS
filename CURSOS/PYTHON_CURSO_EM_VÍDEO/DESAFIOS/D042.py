#REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO: 
#EQUILÁTERO TODOS OS LADOS IGUAIS, ISÓSCELES DOIS LADOS IGUAIS, ESCALENO TODOS OS LADOS DIFERENTES.

print('')
print('----------------------------------------')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

print('----------------------------------------')
print('')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 and r1 == r3:
        print('[SEU TRIÂNGULO É EQUILÁTERO]') #OK
    elif r1 == r2 and r1!= r3 or r1 == r3 and r1 != r2 or r2 == r1 and r2 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2 or r3 == r2 and r3 != r1:
        print('[SEU TRIÂNGULO É ISÓSCELES]')
    else:
        print('[SEU TRIÂNGULO É ESCALENO]')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

print('----------------------------------------')
print('')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO