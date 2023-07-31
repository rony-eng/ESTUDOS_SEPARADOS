# ESTRUTUEA DE REPETIÇÃO FOR

# ESTRUTURA, para o boneco chega até a maça e pegar:
#for c in range(1,10):
#    passo
#pega

# ESTRUTURA, para o boneco dá um passo e pular e depois pegar a maça
#for c in range(0,3):
#    passo
#    pula
#passo
#pega

# ESTRUTURA, para o boneco dá um passo, pular, pega moeda e depois pegar a maça
#for c in range(0,3):
#    if tiver moeda:
#        pega
#    passo
#    pula
#passo
#pega

# ------------------------------------------------------------------------------
# PARTE PRÁTICA
for c in range(0,6):
    print('Oi')
    print('FIM')
print('TERMINO DO FOR')

# PARA A ORDEM AO CONTRÁRIO
for c in range (6, 0, -1): # o terceiro parametro é o passo, em quanto em quanto será contado, nesse caso sera contato de frente pra traz
    print(c)
print('Fim!')

# PARA UMA CONTAGEM, INFORMADO POR UMA VARIAVEL
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

# FAZER UM SOMATÓRIO A PARTIR DO FOR
s = 0
for c in range(0, 4):
    n = int(input('DIGITE UM VALOR: '))
    s += n # += é a mesma coisa de s = s + n
print('O SOMATÓRIO DE TODOS OS VALORES FOI {}'.format(s))