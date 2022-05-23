import os

import random

from  jogo_sem_nome.jogador import jogador

from random import randint

from jogo_sem_nome.tela import tela

from jogo_sem_nome.compras_de_carta import comprar_carta

from jogo_sem_nome.montar_deck import montar_deck

from jogo_sem_nome.compras_de_carta import comprar_mao_inicial

from jogo_sem_nome.bonus import bonus_de_vitoria

from jogo_sem_nome.magias import magia

from jogo_sem_nome.bot import bot

# variaveis principais
def jogo():
    os.system("title GAME SEM NOME")

    deck_p1=[]

    mao_p1=[]

    life_p1=4000

    life_p2=4000

    mana_p1=2000

    mana_p2=2000

    vida_padrao=4000

    mana_padrao=2000

    # efeitos e custos

    dobro=0

    escudo=0

    #escolha de deck

    configuracoes_iniciais=montar_deck(deck_p1,"1",life_p2,mana_p2)

    deck_p1=configuracoes_iniciais[0]

    life_p2=configuracoes_iniciais[1]

    mana_p2=configuracoes_iniciais[2]

    # mão e vida inicial

    configuracoes_de_deck_e_mao=comprar_mao_inicial(deck_p1,mao_p1)

    deck_p1=configuracoes_de_deck_e_mao[0]

    mao_p1=configuracoes_de_deck_e_mao[1]

    mao_p2=3

    #quantidade de cartas que o bot compra por turno comum valor inicial

    compras=1

    # tela(life_p1,life_p2,mana_p1,mana_p2,mao_p2,mao_p2)

    primeiro_turno=True

    while life_p1 != 0:

        #verificar quantidade de cartas no deck

        #se tiver 0 cartas perde

        if len(deck_p1) != 0 and primeiro_turno != True:

            comprar=comprar_carta(deck_p1,mao_p1)

            deck_p1=comprar[0]

            mao_p1=comprar[1]

        else:

            if primeiro_turno != True:

                motivo_derrota="Sem cartas no deck"

                break

        #arrumando o campo

        campo=["","",""]

        while True:

            primeiro_turno = False

            #movimentos do jogador 1

            tela(life_p1,mana_p1,escudo,dobro,mao_p1,deck_p1,life_p2,mana_p2,mao_p2,campo)

            acao_jogador=jogador(campo,life_p1,mana_p1,mao_p1,deck_p1,dobro,escudo,vida_padrao,mana_padrao,compras,life_p2,mana_p2,mao_p2)
            
            campo=acao_jogador[0]

            life_p1=acao_jogador[1]

            mana_p1=acao_jogador[2]

            mao_p1=acao_jogador[3]

            dobro=acao_jogador[4]

            escudo=acao_jogador[5]

            vida_padrao=acao_jogador[6]

            mana_padrao=acao_jogador[7]

            compras=acao_jogador[8]

            life_p2=acao_jogador[9]

            mana_p2=acao_jogador[10]

            mao_p2=acao_jogador[11]

            sair=acao_jogador[12]

            if sair == "sair" or sair == "end turn":

                break
            
        if sair == "sair":

            break

        # Jogador 2 (bot)

        movimentos_do_oponente=0

        while True:

            if mao_p2 >1:

                movimentos_do_oponente+=1

                jogada_do_bot=bot(mao_p2,life_p2,mana_p2,life_p1,escudo,dobro)

                mao_p2=jogada_do_bot[0]

                life_p2=jogada_do_bot[1]

                mana_p2=jogada_do_bot[2]

                life_p1=jogada_do_bot[3]

                escudo=jogada_do_bot[4]

                mensagem=jogada_do_bot[5]

                os.system("cls")

                print(mensagem)

                os.system("pause")

            else:

                mensagem="Bot finalizou o turno"

                if movimentos_do_oponente == 0:

                    mensagem=f"{mensagem} sem fazer jogadas"

                os.system("cls")

                print(mensagem)

                os.system("pause")


                break

            if life_p1 <= 0:

                motivo_derrota="Bot zerou a sua vida"

                life_p1=0

                break

    #derrota
    if sair != "sair":

        os.system("cls")

        os.system("title VOCÊ PERDEU")

        print("VOCÊ PERDEU")

        print(motivo_derrota)

        bots_vencidos=vida_padrao-4000

        bots_vencidos/=2000

        print(f"você venceu {bots_vencidos} bots")

        os.system("pause")
