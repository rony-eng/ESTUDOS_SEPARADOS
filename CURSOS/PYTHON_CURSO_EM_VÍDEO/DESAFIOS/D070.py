#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
#    No final mostre:
#    A) Qual é o total gasto na compra 
#    B) Quantos produtos custam mais de 1000
#    C) Qual é o nome do produto mais barato

#totG = pM1000 = pMB = 0
#while True:
#    produto = str(input('Produto: '))
#    preço = int(input('Valor: '))
#    if 
#    resposta = ' '
#    while resposta not in "SN":
#        resposta = str(input('Deseja adicionar outro produto? ')).strip().upper()[0]
#    if resposta == 'N':
#        break



# Programa feito pelo copilot
# Lista para armazenar os produtos
produtos = []

while True:
    # Lê o nome e o preço do produto
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))

    # Adiciona o produto à lista
    produtos.append({"nome": nome, "preco": preco})

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja adicionar mais produtos? (S/N): ").strip().lower()
    if continuar != "s":
        break

# Exibe a lista de produtos
print("\nProdutos adicionados:")
for produto in produtos:
    print(f"{produto['nome']} - R${produto['preco']:.2f}")
