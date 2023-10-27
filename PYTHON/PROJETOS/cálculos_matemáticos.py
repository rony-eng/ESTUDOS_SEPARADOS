# MONTAR PROJETO DE CALCULOS MATEMÁTICOS COMO, SABER A SEQUÊNCIA DE FIBONACCI
# OU ARÉA DE UM RETANGULO, OU SABER A HIPOTENUSA...

# SOMAR
soma = n + y

# SUBTRAIR
sub = n - y

# DIVIDIR
div = n / y

# MULTIPLICAR
mul = n * y

# FIBONACCI

# O PRIMEIRO TERMO E A RAZÃO DE UMA PA
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