#jogador

import os

import random

from random import randint

from jogo_sem_nome.compras_de_carta import comprar_carta

from jogo_sem_nome.montar_deck import montar_deck

from jogo_sem_nome.compras_de_carta import comprar_mao_inicial

from jogo_sem_nome.bonus import bonus_de_vitoria

from jogo_sem_nome.magias import magia

def jogador(campo,vida_do_jogador,mana_do_jogador,mao_do_jogador,deck_do_jogador,dobro,escudo,vida_padrao,mana_padrao,compras,vida_do_oponente,mana_do_oponente,mao_do_oponente):
    
    sair="nao"

    if len(mao_do_jogador) == 0:
        
        sair="end"
        
    #mensagem secreta caso tenha alguma carta no campo

    if campo != ["","",""]:

        print('\ndigite "m" para execultar ou "c" para cancelar\n')

    if vida_do_jogador <=100 and len(mao_do_jogador) >= 2: 

        print('\ndigite "apelar" para ativar um efeito secreto.\n')

    if vida_do_oponente <= 100:
            
        print('tome cuidado com o bot, ele pode ficar furioso.\n')

    

    #escolha de carta

    carta_escolhida=input('Digite a carta desejada ou "e" para finalizar o seu turno:')

    #se a carta escolhida estiver na mão, ela pode ir para o campo
    if carta_escolhida == "":

        carta_escolhida=" "            

    if carta_escolhida.lower() == "arrumar":
        
        mao_do_jogador=sorted(mao_do_jogador)

    if vida_do_jogador <= 100 and carta_escolhida.lower() == "apelar":
 
        if len(mao_do_jogador) >= 2:

            mao_do_jogador=[]

            apelar=randint(1,4)

            mensagem="Que pena, o efeito não foi ativo"

            if apelar == 2:

                caracter="%"

                mensagem=f"Que sorte, o efeito foi ativo com 50{caracter} da força"

                vida_do_jogador+=3900               

                mana_do_jogador-=1800

                apelar=randint(1,2)

                if apelar == 2:

                    mensagem=f"Excelente, o efeito foi ativo com 100{caracter} da força"

                    vida_do_oponente-=3900

                    mana_do_jogador/=2
            
            os.system("cls")

            print(mensagem)

            os.system("pause")

    #finalizar turno

    if carta_escolhida[0].upper() == "E" or (mao_do_jogador == [] and campo == ["","",""]):

        #devolver cartas a mão  caso tenha alguma no campo

        while len(campo) != 0:

                if campo[0] != "":

                    mao_do_jogador.append(campo[0])

                campo.remove(campo[0])

                sair="end turn"


    elif carta_escolhida in mao_do_jogador and "" in campo:

        mao_do_jogador.remove(carta_escolhida)

        while "" in campo:

            campo.remove("")

        campo.append(carta_escolhida)

        while len(campo) != 3:

            campo.append("") 

    #caso o campo não eseja vazio, outros comandos ficam disponiveis e podem ser usados

    elif carta_escolhida.lower() == "sair": 

        sair="sair"

    elif carta_escolhida[0].upper() == "M":

        execucao=magia(campo,mana_do_jogador,vida_do_jogador,vida_do_oponente,mao_do_jogador,dobro,escudo)

        campo=execucao[0]

        mana_do_jogador=execucao[1]

        vida_do_jogador=execucao[2]

        vida_do_oponente=execucao[3]

        mao_do_jogador=execucao[4]

        dobro=execucao[5]

        escudo=execucao[6]

    elif carta_escolhida[0].upper() == "C":

        for slot in campo:

            if slot != "":

                mao_do_jogador.append(slot)
        
        campo=["","",""]

        #compra de carta do bot 

        mao_do_oponente+=compras

        #end turn

    #vitoria

    if vida_do_oponente <= 0:

        bonus_desejado=bonus_de_vitoria(vida_do_jogador,mana_do_jogador)

        vida_do_jogador=bonus_desejado[0]

        mana_do_jogador=bonus_desejado[1]

        compras+=1

        mao_do_oponente=3+compras

        #vida e mana do bot

        vida_padrao+=2000

        mana_padrao+=1000

        vida_do_oponente=vida_padrao

        mana_do_oponente=mana_padrao

        configuracoes_iniciais=montar_deck(deck_do_jogador,"1",vida_do_oponente,mana_do_oponente)

        deck_do_jogador=configuracoes_iniciais[0]

        vida_do_oponente=configuracoes_iniciais[1]

        mana_do_oponente=configuracoes_iniciais[2]

        configuracoes_de_deck_e_mao=comprar_mao_inicial(deck_do_jogador,mao_do_jogador)

        deck_do_jogador=configuracoes_de_deck_e_mao[0]

        mao_do_jogador=configuracoes_de_deck_e_mao[1]

        dobro=0

        escudo+=compras

        os.system("title GAME SEM NOME")

    return [campo,vida_do_jogador,mana_do_jogador,mao_do_jogador,dobro,escudo,vida_padrao,mana_padrao,compras,vida_do_oponente,mana_do_oponente,mao_do_oponente,sair]
