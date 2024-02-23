#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
#    No final mostre:
#    A) Qual é o total gasto na compra 
#    B) Quantos produtos custam mais de 1000
#    C) Qual é o nome do produto mais barato

# Programa feito pelo copilot
# Lista para armazenar os produtos
produtos = []
totG = pM1000 = pMB = 0
nome_produto_MB = ''

while True:
    # Lê o nome e o preço do produto
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$"))

    # Adiciona o produto à lista
    produtos.append({"nome": nome, "preco": preco})

    # total gasto das compras
    if preco != 0:
        totG += preco
    
    # Quantos produtos custam mais de 1000
    if preco > 1000:
        pM1000 += 1
    
    # Qual o nome do produto mais barato
    pMB = preco
    if preco < pMB: # está parte está errada
        nome_produto_MB = nome

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja adicionar mais produtos? (S/N): ").strip().lower()
    print('')
    if continuar != "s":
        break

# Exibe a lista de produtos
print("\nProdutos adicionados:")
for produto in produtos:
    print(f"{produto['nome']} - R${produto['preco']:.2f}")
print('')
print(f'Total gasto: R${totG}')
print(f'{pM1000} produtos custam mais de 1000 reais')
print(f'O produto mais barato foi {nome_produto_MB}')