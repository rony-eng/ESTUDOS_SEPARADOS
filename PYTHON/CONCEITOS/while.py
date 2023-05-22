# O while é uma estrutura de repetição utilizada quando queremos que determinado 
# bloco de código seja executado ENQUANTO (do inglês while) determinada condição for satisfeita.

#while <condição>:
    # Bloco aser executado

# Aqui, <condição> é uma expressão que pode ser reduzida à True ou False, podendo ser:
# A verificação do valor de uma variável;
# Determinada estrutura de dados alcançar um tamanho;
# O retorno de uma função se igualar a determinado valor;
# Algum valor externo ser alterado (por exemplo um valor armazenado em Banco de Dados).
contador = 0

#while contador < 10:
 #   print(f'Valor do contador é {contador}')
  #  contador += 1

while contador < 10:
    contador += 1
    print(f'Valor do contador é {contador}')    
else:
    print(f'Fim do while e o valor do contador é {contador}')


# Já com while, também podemos utilizar o break em uma condição utilizando if, assim:
num = 0
while num < 5:
    num += 1

    if num == 3:
        break
        
    print(num)

# Em loops com while a lógica é a mesma. O continue irá finalizar o loop atual, iniciando novamente no início do while.
# Veja o exemplo:
num = 0
while num < 5:
    num += 1

    if num == 3:
        continue
        
    print(num)