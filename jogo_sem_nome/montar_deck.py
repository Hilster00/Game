#montar deck

import os

#Recebe o deck do jogador para ser montado, o nome dele para exibir no titulo 
#mana e vida do oponente para caso digite o codigo especial eles serem modificados

def montar_deck(deck_do_jogador,jogador,vida_do_oponente,mana_do_oponente):

    #titulo com nome do jogador

    os.system(f"titel Jogador {jogador}")

    #deck do jogador e limpo para garantir que nao tenha nenhuma carta nele

    deck_do_jogador=[]

    #cartas disponiveis para serem adicionadas ao deck

    cartas_disponiveis=["1","2","3","4","5"]

    #mensagem para a escolha de uma carta

    definir_deck_mensagem="\n\nDigite qual carta deseja:"    
    
    #montagem do deck com 25 cartas

    while len(deck_do_jogador) != 25:

        #limpa a tela

        os.system("cls")

        #a variavel recebe uma mensagem que informa a quantidade atual de cartas no deck do jogador

        printar=f"Seu deck possui {len(deck_do_jogador)} cartas no momento."

        #exibe a mensagem

        print(printar)

        #prina a variavel com as cartas disponiveis para escolha

        print(f"\ncartas disponiveis {cartas_disponiveis}")

        #a variavel escolha recebe a carta que o jogador digitou 

        escolha=input(definir_deck_mensagem)

        #verificar se a carta está disponivel

        #caso não esteja, é verificado se ele digitou um comando especial

        if escolha not in cartas_disponiveis:

            #comando padrão para deck pre definido

            if escolha.lower() == "padrão" or escolha.lower() == "padrao":

                #deck com 5 cartas de cada

                deck_do_jogador=["1","2","3","4","5","1","2","3","4","5","1","2","3","4","5","1","2","3","4","5","1","2","3","4","5"]

            #comando especial para o oponente ter apenas 1 de vida e 1 de mana, e o jogador ter apenas cartas 3 no deck

            if escolha.lower() == "hilster":

                #deck com apenas cartas 3

                deck_do_jogador=["3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3"]

                #a vida do oponente e limitada para 1 ponto
               
                vida_do_oponente=1

                #a mana do oponente e limitada para 1 ponto

                mana_do_oponente=1

            #comando para um deck com cartas 5,1 e 2 como prioridade

            if escolha.lower() == "compra":

                #o deck e montado

                deck_do_jogador=["5","5","5","5","5","5","1","1","1","1","1","1","2","2","2","2","2","2","3","3","3","3","3","3","4"]
                
            #caso não seja um dos comandos, ele volta ao inicio do laço

            continue
        
        deck_do_jogador.append(escolha)

        #verifica se o limite de 6 cartas iguais no deck foi atingido 

        if deck_do_jogador.count(escolha) == 6:

            #se o limite de 6 cartas foi atingido, a carta nao estara mais disponivel para escolha
            
            cartas_disponiveis.remove(escolha)

    #retorna o deck montado e a vida/mana do oponente
    
    return [deck_do_jogador,vida_do_oponente,mana_do_oponente]



