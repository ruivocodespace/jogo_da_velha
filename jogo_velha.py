import os
from check_winf import check_win
from check_impf import check_imp
from print_tabf import print_tab

tab = [' '] * 9

#---FUNCOES AUXILIARES---

#Imprime as instruções(posições)
def print_instructions():
    print("Posições no tabuleiro:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

#---FUNÇÃO PRINCIPAL---
def main():
    print_tab(tab)
    while True:
        #Jogador seleciona o simbolo que irá usar
        escolha_jogador = input("Jogador 1, escolha X ou O:").upper()
        #Check se a entrada é válida
        if escolha_jogador in ["X", "O"]:
            break
        else: 
            print("Entrada inválida. Escolha entre O e X")
    #Define o simbolo de cada jogador
    if escolha_jogador == "X":
        jogador = "X"
        jogador1 = "O"
    else:   
        jogador = "O"
        jogador1 = 'X'

    atual = jogador
    
    #---Loop das jogadas---
    while True:
        os.system('cls')  
        print_tab(tab)
        try:
            pos = int(input(f"Jogador ({atual}), escolha uma posição (0-8): "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if not check_imp(tab, atual, pos):
            print("Posição inválida ou ocupada, tente novamente.")
            continue

        #checa se alguém ganhou ou empatou
        ganhou, vencedor = check_win(tab)
        if ganhou == "empate":
            print_tab(tab)
            print("Deu velha! Empate!")
            break
        elif ganhou:
            print_tab(tab)
            print(f"Jogador {vencedor} venceu!")
            break

        #alterna jogador
        atual = jogador1 if atual == jogador else jogador


print_instructions()
main()

