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

# DESSAFIO CONCLUÍDO, AINDA NÃO VI A RESOLUÇÃO