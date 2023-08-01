# D046 - FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE 
# FOGOS DE ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.
from time import sleep
# sleep(1) para dá um segundo de um processo para o outro

print('Contagem regressiva para o estouro dos FOGOS!')
sleep(1)
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('Feliz Ano Novo!')

# DESAFIO CONCLUÍDO

# RESOLUÇÃO DE ACORDO COM O CURSO
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')