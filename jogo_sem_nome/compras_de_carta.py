from random import choice
import os

def comprar_carta(deck_do_jogador,mao_do_jogador):

    carta_comprada=choice(deck_do_jogador)

    mao_do_jogador.append(carta_comprada)

    deck_do_jogador.remove(carta_comprada)

    while True:

        os.system("cls")

        cartas_disponiveis=["1","2","3","4","5"]

        print(f"Cartas na sua mao {sorted(mao_do_jogador)}\n\n")

        print("Escolha uma destas cartas para ser adicionada a sua mão [1, 2, 3, 4, 5]")

        carta_escolhida=input("\n\n\nDigite a carta desejada:")

        if carta_escolhida in cartas_disponiveis:

            mao_do_jogador.append(carta_escolhida)
            
            break

    while len(mao_do_jogador) > 13:

        remove=choice(mao_do_jogador)

        mao_do_jogador.remove(remove)    

    return [deck_do_jogador,mao_do_jogador]

def comprar_mao_inicial(deck_do_jogador,mao_do_jogador):

    mao_do_jogador=[]

    carta_comprada=choice(deck_do_jogador)

    mao_do_jogador.append(carta_comprada)

    deck_do_jogador.remove(carta_comprada)

    carta_comprada=choice(deck_do_jogador)

    mao_do_jogador.append(carta_comprada)

    deck_do_jogador.remove(carta_comprada)

    carta_comprada=choice(deck_do_jogador)

    mao_do_jogador.append(carta_comprada)

    deck_do_jogador.remove(carta_comprada)

    compra=comprar_carta(deck_do_jogador,mao_do_jogador)

    deck_do_jogador=compra[0]

    mao_do_jogador=compra[1]

    mao_do_jogador=sorted(mao_do_jogador)
    
    return [deck_do_jogador,mao_do_jogador]
