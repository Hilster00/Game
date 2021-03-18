# Tela

import os

#recebe todos os dados que serao exibidos 

def tela(vida_do_jogador,mana_do_jogador,escudo_do_jogador,dobro_do_jogador,mao_do_jogador,deck_do_jogador,vida_do_oponente,mana_do_oponente,mao_do_oponente,campo):
    
    #limpa a tela

    os.system("cls")

    #mensagem especial e criada vazia, para so ter uma mensagem caso uma condiçao seja atendida

    mensagem_especial=""

    #titulo

    os.system("title RandomGame")

    #condiçao 1

    if escudo_do_jogador != 0:

        #mensagem recebe o numero de escudos que o jogador tem

        mensagem_especial=f"escudo ({escudo_do_jogador})"

    #condiçao 2

    elif dobro_do_jogador != 0:

        #mensagem recebe o numero de dobros que o jogador tem

        mensagem_especial=f"dobro ({dobro_do_jogador})"




#____________________________________________________________________________

    if vida_do_jogador < 1000:

        #arruma a variavel vida para que 4 digitos sejam exibidos exibidos no minimo sempre, ex 0012


        #coloca 000 no começo, ex 12 para 00012

        vida_do_jogador=f"000{vida_do_jogador}"

        #inverte a ordem dos caracteres da variavel, ex 00012 para 21000

        vida_do_jogador=vida_do_jogador[::-1]
        
        #pega apenas os 4 primeiros digitos, ex 21000 para 2100

        vida_do_jogador=vida_do_jogador[0:4]

        #entao inverte novamente, ex 2100 para 0012

        vida_do_jogador=vida_do_jogador[::-1]




#____________________________________________________________________________

    if vida_do_oponente < 1000:

        #arruma a variavel vida para que 4 digitos sejam exibidos exibidos no minimo sempre, ex 0012


        #coloca 000 no começo, ex 12 para 00012

        vida_do_oponente=f"000{vida_do_oponente}"

        #inverte a ordem dos caracteres da variavel, ex 00012 para 21000

        vida_do_oponente=vida_do_oponente[::-1]

        #pega apenas os 4 primeiros digitos, ex 21000 para 2100

        vida_do_oponente=vida_do_oponente[0:4]

        #entao inverte novamente, ex 2100 para 0012

        vida_do_oponente=vida_do_oponente[::-1]




#____________________________________________________________________________
    
    if mana_do_jogador < 1000:

        #arruma a variavel mana para que 4 digitos sejam exibidos exibidos no minimo sempre, ex 0012

        #coloca 000 no começo, ex 12 para 00012  
        
        mana_do_jogador=f"000{mana_do_jogador}"

        #inverte a ordem dos caracteres da variavel, ex 00012 para 21000

        mana_do_jogador=mana_do_jogador[::-1]

        #pega apenas os 4 primeiros digitos, ex 21000 para 2100

        mana_do_jogador=mana_do_jogador[0:4]

        #entao inverte novamente, ex 2100 para 0012

        mana_do_jogador=mana_do_jogador[::-1]




#____________________________________________________________________________

    if mana_do_oponente < 1000:

        #arruma a variavel mana para que 4 digitos sejam exibidos no minimo sempre, ex 0012

        #coloca 000 no começo, ex 12 para 00012

        mana_do_oponente=f"000{mana_do_oponente}"

        #inverte a ordem dos caracteres da variavel, ex 00012 para 21000

        mana_do_oponente=mana_do_oponente[::-1]

        #pega apenas os 4 primeiros digitos, ex 21000 para 2100

        mana_do_oponente=mana_do_oponente[0:4]

        #entao inverte novamente, ex 2100 para 0012

        mana_do_oponente=mana_do_oponente[::-1]



#____________________________________________________________________________   
    
    print("Player 1\t\t\t\t\t\t\t  Player 2")

    #Exibe a vida dos 2 jogadores

    print(f"Vida {vida_do_jogador}\t\t\t\t\t\t\t  Vida {vida_do_oponente}")

    #exibe a mana dos 2 jogadores

    print(f"Mana {mana_do_jogador}\t\t\t\t\t\t\t  Mana {mana_do_oponente}")

    #printa a mensagem especial(numero de escudos/dobros caso tenha) e o numero de cartas na mao do oponente

    print(f"\n{mensagem_especial}\t\t\t\t\t\t   Cartas do Jogador 2 ({mao_do_oponente})\n\n\n")

    #exibe o campo com as cartas que estiverem nele

    print(f"\t\t\t[ {campo[0]} ]\t [ {campo[1]} ]\t [ {campo[2]} ]\n\n\n")

    #printa o numero de cartas no deck do jogador

    print(f"\n\nDECK({len(deck_do_jogador)})")

    #mostra as cartas que o jogador tem na mao
    
    print(mao_do_jogador)
