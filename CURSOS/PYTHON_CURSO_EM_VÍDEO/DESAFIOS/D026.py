# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:

# - QUANTAS VEZES APARECE A LETRA “A”
# - EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
# - EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ
print('')
print('------------------------------')
frase = str(input('Insira uma frase: ')).strip().upper()

print('')
print('[A LETRA "A" APARECE {} VEZES]'.format(frase.count('A')))
print('[A LETRA "A" APARECE A PRIMEIRA VEZ NA POSIÇÃO {}]'.format(frase.find('A')+1))
print('[A LETRA "A" APARECE A ULTIMA VEZ NA POSIÇÃO {}]'.format(frase.rfind('A')+1))
print('------------------------------')
print('')