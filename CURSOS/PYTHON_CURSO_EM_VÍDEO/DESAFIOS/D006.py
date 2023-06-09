# Crie um algoritmo que leia um número e mostre o seu dobro, tripo e a raiz quadrada.

n = int(input('Insira um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)

print ('O dobro de {} vale {}.'.format(n, d))
print ('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

# ainda falta araiz quadrada, para calcula pode ser assim: pow(n, (1/2))