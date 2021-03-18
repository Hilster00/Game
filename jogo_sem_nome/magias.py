#magias

import os

magia_vida_nv2=["12","13","14","15","21","23","24","25","11","22"]

efeito_vida_nv2=[250,300,350,400,180,150,120,90,450,500]

custo_vida_nv2=[125,150,175,200,60,50,40,30,200,225]

magia_vida_nv3=["123","124","125","213","214","215","111","222", "225","115"]

efeito_vida_nv3=[2000,1400,1200,3600,3000,2700,1200,1200,3900,3500]

custo_vida_nv3=[1000,700,600,1200,1000,900,500,400,2000,1800]

magia_dano_nv2=["31","32","34","35","41","42","43","45","44","33"]

efeito_dano_nv2=[250,300,350,400,180,150,120,90,450,500]

custo_dano_nv2=[125,150,175,200,60,50,40,30,200,225]

magia_dano_nv3=["341","342","345","431","432","435","333","444","335","445"]

efeito_dano_nv3=[2000,1400,1200,3600,3000,2700,1200,1200,3500,3900]

custo_dano_nv3=[1000,700,600,1200,1000,900,500,400,1800,2000]

from random import choice

def magia(campo,mana_do_jogador,vida_do_jogador,vida_do_oponente,mao_do_jogador,dobro,escudo):

    while "" in campo:
        campo.remove("")
    cartas=["1","2","3","4","5"]

    #recarga de mana

    if len(campo) == 1:

        if campo[0] == "5":

            mana_do_jogador+=1000

        elif campo[0] == "4" :

            mana_do_jogador+=400

        elif campo[0] == "3":

            mana_do_jogador+=600

        elif campo[0] == "2":

            mana_do_jogador+=400

        else:

            mana_do_jogador+=600

                #magias de nivel 2

    elif len(campo) == 2:

        campo=f"{campo[0]}{campo[1]}"

        #cura

        if campo[0] =="1" or campo[0] == "2": 

            if campo in magia_vida_nv2:

                w=magia_vida_nv2.index(campo)

                if mana_do_jogador >= custo_vida_nv2[w]:

                    vida_do_jogador+=efeito_vida_nv2[w]

                    mana_do_jogador-=custo_vida_nv2[w]

                    if dobro != 0:

                        dobro-=1

                        vida_do_jogador+=efeito_vida_nv2[w]

                    #dano

        elif campo[0] =="3" or campo[0] == "4":

            if campo in magia_dano_nv2:

                w=magia_dano_nv2.index(campo)   

                if mana_do_jogador >= custo_dano_nv2[w]:

                    vida_do_oponente-=efeito_dano_nv2[w]

                    mana_do_jogador-=custo_dano_nv2[w]

                    if dobro != 0:

                        dobro-=1

                        vida_do_oponente-=efeito_dano_nv2[w]

        #magias secretas   

        else:

            if campo == "55":

                if mana_do_jogador >=500:

                    escudo+=1

                    dobro=0

                    mana_do_jogador-=500

            elif campo == "54" or campo == "53":

                if mana_do_jogador >= 800:

                    dobro+=1

                    escudo=0

                    mana_do_jogador-=800

            elif campo == "52" or campo == "51":

                if mana_do_jogador >= 800:

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))
                               
                    mana_do_jogador-=800
                    
                #magias de nivel 3
    else:

        campo=f"{campo[0]}{campo[1]}{campo[2]}"

        #cura

        if campo[0] == "1" or campo [0] == "2":   
            
            if campo in magia_vida_nv3:

                w=magia_vida_nv3.index(campo)    

                if mana_do_jogador >= custo_vida_nv3[w]:

                    vida_do_jogador+=efeito_vida_nv3[w]

                    mana_do_jogador-=custo_vida_nv3[w]

                    if dobro != 0:

                        vida_do_jogador+=efeito_vida_nv3[w]

                        dobro-=1

        #dano

        elif campo[0] == "3" or campo[0] == "4":                        
                       
            if campo in magia_dano_nv3:

                w=magia_dano_nv3.index(campo) 

                if mana_do_jogador >= custo_dano_nv3[w]:

                    vida_do_oponente-=efeito_dano_nv3[w]

                    mana_do_jogador-=custo_dano_nv3[w]

                    if dobro != 0:

                        dobro-=1

                        vida_do_oponente-=efeito_dano_nv3[w]

        #magias secretas

        else:
            
            if campo == "555":

                if mana_do_jogador >= 900:

                    mana_do_jogador-=900

                    escudo+=2

                    dobro=0

            if campo == "553" or campo == "554":

                if mana_do_jogador >= 1500:

                    dobro+=2

                    escudo=0

                    mana_do_jogador-=1500

            if campo == "551" or campo =="552":

                if mana_do_jogador >= 1500:

                    mana_do_jogador-=1500

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas)) 

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))

                    mao_do_jogador.append(choice(cartas))
                                
    # limpar o campo caso tenha usado ou não uma magia
    
    campo=["","",""]

    

    return [campo,mana_do_jogador,vida_do_jogador,vida_do_oponente,mao_do_jogador,dobro,escudo]

    #recuperar cartas
            
