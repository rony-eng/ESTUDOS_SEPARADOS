# CORES NO TERMINAL
#print('\33[31;43mOlá mundo!') #para letra vermelha e fundo amarelo
print('\033[1;31;43mOlá, mundo!\033[m') #letra vermelha e negrita, fundo amarelo e tamanho de fundo até a letra

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b)) #colorindo os números com verde e vermelho

# outra forma de colorir usando o format
name = 'Rony'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', name, '\033[m'))

# outra forma de colorir usando variaveis
nome = 'rony'
cores = {'limpar': '\033[m' , 
         'azul': '\033[34m' , 
         'amarelo': '\033[33m' , 
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpar']))