#Combate
import random, atributes
from atraso import delay


class Combat:

    enemy = atributes.Monster(40, 15, 13, 16, 10, 12, 7, 3)
    player = atributes.Atributos.escolha()
    
    
    def turns(enemy, player):
        if player.spd > enemy.mon_spd:
            x = 1
        else:
            x = 2
        while enemy.mon_hp > 0:
            if x == 1:
                action()
                x = 2
            elif x == 2:
                print("O inimigo avança!\n-")
                delay()
                inimigo()
                x = 1
    
def action(enemy, player):
    print(f"A vida do monstro é de {enemy.mon_hp}, vamos ver se você consegue...")
    delay()
    decision = input("ATACAR[1]      DEFENDER[2]       FUGIR[3]\n")
    delay()
    if decision == '1':
        print("Você decide atacar o monstro\n")
        delay()
        if player.pre_f > player.pre_m:
            acerto = random.randint(1,20) + player.pre_f
            print(f"seu acerto foi igual à {acerto}\n-")
            delay()
            if acerto < enemy.mon_defense_f:
                print(f"O monstro defendeu seu ataque! Ele tem {enemy.mon_defense_f} de defesa física!\n-")
                delay()
            else:
                print(f"Você acerta! O monstro sofre {dano_f()} de dano\n-")
                delay()
        else:
            acerto = random.randint(1,20) + player.pre_m
            print(f"seu acerto foi igual à {acerto}")
            delay()
            if acerto < enemy.mon_defense_m:
                print(f"O Orc defendeu seu ataque! Ele tem {enemy.mon_defense_m} de defesa mágica!\n-")
                delay()
            else:
                print(f"Você acerta! O monstro sofre {dano_m()} de dano\n-")
                delay()
    
def inimigo(enemy, player):
    chance = random.randint(1,100)
    if chance <= 75:
        print("Um ataque vem na sua direção!")
        delay()
        acerto_inimigo = random.randint(1,20) + enemy.mon_pre_f
        if acerto_inimigo > player.defense_f:
            dmg_inimigo = random.randint(1,6) + enemy.mon_atk_f/2
            print(f"Ele te acerta e causa {dmg_inimigo} de dano!\n-")
            player.hp -= dmg_inimigo
            delay()
            if player.hp <= 0:
                print("Você morreu :/")
                exit()
        else:
            print("Mas você desvia majestosamente\n-")
            delay()
    else:
        print("O monstro ergue seu escudo e espera sua investida\n-")
        delay()