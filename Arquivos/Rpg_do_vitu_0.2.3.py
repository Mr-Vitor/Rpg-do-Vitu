import random, time, atributes, Monster_Atributes

def delay():
    time.sleep(0.8)

def ação():
    print(f"A vida do monstro é de {ms_stts[0]}, vamos ver se você consegue...")
    delay()
    action = input("ATACAR[1]      DEFENDER[2]       FUGIR[3]\n")
    delay()
    if action == '1':
        print("Você decide atacar o monstro\n")
        delay()
        if classe == 1:
            acerto = random.randint(1,20) + stts[6]
            print(f"seu acerto foi igual à {acerto}\n-")
            delay()
            if acerto < ms_stts[3]:
                print(f"O monstro defendeu seu ataque! Ele tem {ms_stts[3]} de defesa física!\n-")
                delay()
            elif acerto >= ms_stts[3]:
                print(f"Você acerta! O monstro sofre {dano_f()} de dano\n-")
                delay()
        elif classe == 2:
            acerto = random.randint(1,20) + stts[7]
            print(f"seu acerto foi igual à {acerto}")
            delay()
            if acerto < ms_stts[4]:
                print(f"O Orc defendeu seu ataque! Ele tem {ms_stts[4]} de defesa mágica!\n-")
                delay()
            elif acerto >= ms_stts[4]:
                print(f"Você acerta! O monstro sofre {dano_m()} de dano\n-")
                delay()
        elif classe == 3:
            acerto = random.randint(1,20) + stts[6]
            print(f"Seu acerto foi igual à {acerto}")
            delay()
            if acerto < ms_stts[3]:
                print(f"O monstro defendeu seu ataque! Ele tem {ms_stts[3]} de defesa física!\n-")
                delay()
            elif acerto >= ms_stts[3]:
                print(f"Você acerta! O monstro sofre {dano_f()} de dano\n-")
                delay()
        
    elif ação == '2':
        print("Você decide se defender e levanta seu escudo\n-")
        delay()
            
    elif ação == '3':
        print("Você decidiu fugir da batalha e tentar de novo outra hora")
        exit()

    else:
        print("Ação inadequada")
        ação = input("ATACAR[1]      DEFENDER[2]       FUGIR[3]\n")
        delay()



def dano_f():
    dmg = random.randint(1,6) + stts[1]/2
    ms_stts[0] -= dmg
    return dmg

def dano_m():
    dmg = random.randint(1,6) + stts[2]/2
    ms_stts[0] -= dmg
    return dmg

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print("Bem vindo à cidade mágica de Themitas")

jogador_1 = input("Qual seu nome? ")

print(f"Olá {jogador_1}! Vamos começar a aventura")
delay()
print("Veja, um Orc apareceu! Vamos acabar com ele!")
delay()


enemy = Monster_Atributes.MonsArt(40, 15, 13, 16, 10, 12)

#'combate'
turno()
if enemy.hp <= 0:
    print("O monstro possui 0 de vida")
    delay()
    print("Você derrotou o monstro! :D")
