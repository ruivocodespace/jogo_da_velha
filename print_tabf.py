#import os

def print_tab(tab):

    #Limpa a tela
    #os.system('cls')    
    #Imprime tabuleiro
    print("  " + tab[0], tab[1], tab[2], sep=" | ")
    print("+---+---+---+")
    print("  " + tab[3], tab[4], tab[5], sep=" | ")
    print("+---+---+---+")
    print("  " + tab[6], tab[7], tab[8], sep=" | ")