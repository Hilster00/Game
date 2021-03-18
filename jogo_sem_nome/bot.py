from random import choice
from random import randint


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

def bot(mao_do_bot,vida_do_bot,mana_do_bot,vida_do_jogador,escudo,dobro):

    if mana_do_bot < 1200:

        if mao_do_bot>1:

            mana_do_bot+=1000

            mao_do_bot-=1

            mensagem="Recuperou 1000 de mana"

    if vida_do_bot >= vida_do_jogador:

        if mao_do_bot >= 3:

            efeito=choice(magia_dano_nv3)

            if custo_dano_nv3[magia_dano_nv3.index(efeito)] <= mana_do_bot:

                if escudo == 0:
                    dano=efeito_dano_nv3[magia_dano_nv3.index(efeito)]

                    if dobro != 0:     

                        dano/=2

                    vida_do_jogador-=dano

                    mensagem=f"Causou {dano} de dano ao jogador"

                else:

                    escudo-=1

                    mensagem=f"Destruiu 1 escudo do jogador, restam {escudo} escudos"

                mana_do_bot-=custo_dano_nv3[magia_dano_nv3.index(efeito)]

                mao_do_bot-=3

        elif mao_do_bot == 2:

            efeito=choice(magia_dano_nv2)

            if custo_dano_nv2[magia_dano_nv2.index(efeito)] <= mana_do_bot: 

                if escudo == 0:

                    dano=efeito_dano_nv2[magia_dano_nv2.index(efeito)]

                    if dobro != 0:

                        dano/=2

                    vida_do_jogador-=dano

                    mensagem=f"Causou {dano} de dano ao jogador"

                else:

                    escudo-=1

                    mensagem=f"Destruiu 1 escudo do jogador, restam {escudo} escudos"

                mana_do_bot-=custo_dano_nv2[magia_dano_nv2.index(efeito)]

                mao_do_bot-=2
                        
    else:

        apelacao=0

        if mao_do_bot >= 2 and vida_do_bot <= 100:

                apelacao=randint(1,4)

        if apelacao == 2:

            vida_do_bot+=3900

            mensagem=f"bot ficou furioso e recuperou 3900 de vida"   

            apelacao=randint(1,2)

            if apelacao == 2:

                vida_do_jogador-=3900

                mensagem=f"bot ficou muito furioso, recuperou 3900 de vida e causou 3900 de dano"

            mao_do_bot=0

        else:

            if mao_do_bot >= 3:

                efeito=choice(magia_vida_nv3)

                if custo_vida_nv3[magia_vida_nv3.index(efeito)] <= mana_do_bot:

                    w=magia_vida_nv3.index(efeito)

                    vida_do_bot+=efeito_vida_nv3[w]

                    mana_do_bot-=custo_vida_nv3[w]

                    mao_do_bot-=3

                    mensagem=f"Recuperou {efeito_vida_nv3[magia_vida_nv3.index(efeito)]} de vida"

            elif mao_do_bot ==2:

                efeito=choice(magia_vida_nv2)

                if custo_vida_nv2[magia_vida_nv2.index(efeito)] <= mana_do_bot:

                    w=magia_vida_nv2.index(efeito)

                    vida_do_bot+=efeito_vida_nv2[w]

                    mana_do_bot-=custo_vida_nv2[w]

                    mao_do_bot-=2

                    mensagem=f"Recuperou {efeito_vida_nv2[magia_vida_nv2.index(efeito)]} de vida"
                    
    return [mao_do_bot,vida_do_bot,mana_do_bot,vida_do_jogador,escudo,mensagem]
