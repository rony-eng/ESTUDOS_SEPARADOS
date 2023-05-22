# O for é utilizado para percorrer ou iterar sobre uma sequência de dados 
# (seja esse uma lista, uma tupla, uma string), executando um conjunto de instruções em cada item.

lista = [0,1,2,3,4,5]
familia = ['maria', 'raimundo', 'valdiano', 'valdiana', 'caludiana', 'claudiano', 'hadyla', 'rony', 'roniely']

#for item in lista: #item é a variavel que vai receber os valores da lista
#   print(item)

for membros in familia:
    print(membros)
else: #Adicionar o else ao final do for nos possibilita executar um bloco de código após o iterável ter sido completamente percorrido.
    print('Esses são todos os membros da família.')





# Podemos também percorrer os dicionários do Python (que são uma estrutura de dados muito importante).
notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}
for chave, valor in notas.items():
    print(f"{chave}: {valor}")


#Também podemos percorrer strings, pois elas também são um tipo iterável:
for caractere in 'Python':
    print(caractere)






# Existem 3 comandos que nos auxiliam quando queremos alterar o fluxo de uma estrutura de repetição.
# São eles: break, continue e pass.





# Auxiliador break
#É usado para finalizar um loop, isto é, é usado para parar sua execução.
#Geralmente vem acompanhado de alguma condição para isso, com um if.
#Veja um exemplo:
for num in range(10):
    # Se o número for igual a = 5, devemos parar o loop
    if num == 5:
        # Break faz o loop finalizar
        break
    else:
        print(num)





# Auxiliador continue
# Funciona de maneira similar ao break, contudo ao invés de encerrar o loop ele pula todo código que estiver abaixo dele (dentro do loop) partindo para a próxima iteração.
# Vamos ao exemplo:
for num in range(5):
    if num == 3:
        print("Encontrei o 3")
        # Executa o continue, pulando para o próximo laço
        continue
    else:
        print(num)

    print("Estou abaixo do IF")





# Auxiliador pass
#O pass nada mais é que uma forma de fazer um código que não realiza operação nenhuma.
#Tipo o Magikarp do Pokemon :laughing: :laughing: :laughing:
#Mas calma, ele tem uma razão de existir no Python!
#Como os escopos de Classes, Funções, If/Else e loops for/while são definidos pela indentação do 
# código (e não por chaves {} como geralmente se vê em outras linguagens de programação), usamos o pass para dizer ao Python que o bloco de código está vazio.
#Veja alguns exemplos:

for item in range(5000):
    pass

while False:
    pass

class Classe:
    pass

if True:
    pass
else:
    pass

def funcao():
    pass





# A função range()
# A função range é de grande ajuda quando o tema é repetição, laços, for etc…
# Ela gera uma sequência de números pela qual podemos iterar!

#Com ela, conseguimos especificar:

# O inicio de uma sequência;
# O passo (ou pulo); e
# O valor final da sequência.
# Com isso o Python nos entrega uma sequência de números para utilizarmos!





# Funcão enumerate()
# Uma dica bem bacana para se usar com o for, é a função enumerate().
# Ela nos entrega um contador embutido no próprio for! :heart_eyes:
# Ao invés de fazer isso:
contador = 0
computador = ['Processador', 'Teclado', 'Mouse']

for elemento in computador:
    print(f"Índice={contador} | Valor={elemento}")
    contador += 1

#Jogue esse contador fora e faça isso:

computador = ['Processador', 'Teclado', 'Mouse']
for indice, valor in enumerate(computador):
    print(f"Índice={indice} | Valor={valor}")
#Esse código é o que chamamos de Pythônico (que segue as melhores práticas da linguagem)! :wink:





#Outra maneira de iterar sobre os índices, é combinar as funções range() e len().
#A função len() retorna o tamanho de um iterável (lista, tupla, set).
#Podemos combiná-los da seguinte forma:
computador = ['Processador', 'Teclado', 'Mouse']
for indice in range(len(computador)):
    print(f"Índice={indice} | valor={computador[indice]}")
