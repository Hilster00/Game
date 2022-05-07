#bonus de vitoria

import os

#O bonus e dado quado o jogador vence a partida, podendo escolher entre vida e mana

def bonus_de_vitoria(vida_do_jogador,mana_do_jogador):  

    #Laço de repetiçao eterno

    while True:

        #limpa a tela e exibe as opçoes disponiveis 

        os.system("cls")

        print("Escolha um bônus\n(1)+2000 PV\n(2)+1000 Mana")

        #o jogador escolhe uma opçao

        escolha=input("Digite a opção desejada:")

        #Validaçao da opçao 1

        if escolha == "1":

            #bonus de vida caso seja a escolhida

            vida_do_jogador+=2000

            #finaliza o laco

            break

        #validaçao da opçao 2

        elif escolha == "2":

            #bonus de mana caso seja o escolhido

            mana_do_jogador+=1000

            #finaliza o laco

            break

    #devolve a vida e mana com o bous aplicado    
        
    return [vida_do_jogador,mana_do_jogador]
