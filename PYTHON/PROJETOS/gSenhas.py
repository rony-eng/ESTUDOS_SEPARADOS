import random

cMax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cMin = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
cEsp = "!@#$%&*"

comp = cMax + cMin + num + cEsp
digitos = 15

senha1 = "".join(random.sample(comp, digitos))

print(' ')
print('Senha 1: ' + senha1)
print(' ')
