#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder.
#Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# MINHA RESOLUÇÃO
from random import randint

def jogar_par_impar():
  """
  Função para jogar par ou ímpar com o computador.
  """
  vitorias_consecutivas = 0
  while True:
    # Escolha do jogador
    jogador_escolha = input("Digite 'par' ou 'ímpar': ").lower()
    while jogador_escolha not in ("par", "ímpar"):
      jogador_escolha = input("Digite 'par' ou 'ímpar': ").lower()

    # Escolha do computador
    computador_escolha = "ímpar" if randint(0, 1) == 0 else "par"

    # Soma dos valores
    soma = int(input("Digite um número: ")) + randint(0, 10)

    # Resultado
    resultado = "par" if soma % 2 == 0 else "ímpar"

    # Exibir as escolhas e o resultado
    print(f"Você escolheu {jogador_escolha} e o computador escolheu {computador_escolha}.")
    print(f"A soma dos valores é {soma}, que é {resultado}.")

    # Verificar o vencedor
    if jogador_escolha == resultado:
      print("Você ganhou!")
      vitorias_consecutivas += 1
    else:
      print("O computador ganhou!")
      break

    # Perguntar se o jogador deseja continuar
    continuar = input("Deseja continuar jogando (s/n)? ").lower()
    if continuar not in ("s", "sim"):
      break

  print(f"Você conseguiu {vitorias_consecutivas} vitórias consecutivas!")

# Iniciar o jogo
jogar_par_impar()



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# RESOLUÇÃO DE ACORDO COM O CURSO

#from random import randint
#v = 0
#while True:
#    jogador = int(input('Diga um valor: '))
#    computador = randint(0, 10)
#    total = jogador + computador
#    tipo = ''
#    while tipo not in 'PI':
#        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
#    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
#    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
#    if tipo == 'P':
#        if total % 2 == 0:
#            print('Você VENCEU!')
#            v += 1
#        else:
#            print('Você PERDEU!')
#            break
#    elif tipo == 'I':
#        if total % 2 == 1:
#            print('Você VENCEU!')
#            v += 1
#        else:
#            print('Você PERDEU!')
#            break
#    print('Vamos jogar novamente...')
#print(f'GAME OVER! Você venceu {v} vezes.')
