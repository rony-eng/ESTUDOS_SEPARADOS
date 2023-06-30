#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA 
#DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, 
#COBRANDO R$0.50 POR KM PARA VIAGENS DE ATÉ 200KM E 
#R$0.45 PARA VIAGENS MAIS LONGAS.
km = int(input('Qual a distância de sua viagem em Km: '))
p1 = km * 0.50
p2 = km * 0.45
if km < 200:
    print('Sua passagem custa {}R$.'.format(p1))
else:
    print('Sua passagem custa {}R$.'.format(p2))

# DESAFIO CONCLUÍDO ----------------------------------------------

# RESOLUÇÃO SEGUNDO CURSO ----------------------------------------

# 1° forma
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

# 2° forma com if simplificado - não muito indicado
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))