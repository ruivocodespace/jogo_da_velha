def main():
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
        print_tab(tab)
        try:
            pos = int(input(f"Jogador ({atual}), escolha uma posição (0-8): "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if not check_imp(tab, atual, pos):
            print("Posição inválida ou ocupada, tente novamente.")
            continue

        # checa se alguém ganhou ou empatou
        ganhou, vencedor = check_win(tab)
        if ganhou == "empate":
            print_tab(tab)
            print("Deu velha! Empate!")
            break
        elif ganhou:
            print_tab(tab)
            print(f"Jogador {vencedor} venceu!")
            break

        # alterna jogador
        atual = jogador1 if atual == jogador else jogador