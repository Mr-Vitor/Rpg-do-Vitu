#Atributos

class Atributos:
    def __init__(self, hp, atk_f, atk_m, spd, defense_f, defense_m, pre_f, pre_m):
        self.hp = hp
        self.atk_f = atk_f
        self.atk_m = atk_m
        self.spd = spd
        self.defense_f = defense_f
        self.defense_m = defense_m
        self.pre_f = pre_f
        self.pre_m = pre_m


    def escolha():
        print("Qual a sua classe?")
        classe = int(input("Guerreiro[1]   Mago[2]   Assassino[3]\n"))

        if classe == 1:
            return Atributos(31,18,3,14,20,5,8,0)
            
        elif classe == 2:
            return Atributos(21,4,18,10,5,17,1,7)
            
        elif classe == 3:
            return Atributos(26,10,8,16,19,16,9,4)

class Monster:
    def __init__(self, mon_hp, mon_atk_f, mon_atk_m, mon_spd, mon_defense_f, mon_defense_m, mon_pre_f, mon_pre_m):
        self.mon_hp = mon_hp
        self.mon_atk_f = mon_atk_f
        self.mon_atk_m = mon_atk_m
        self.mon_spd = mon_spd
        self.mon_defense_f = mon_defense_f
        self.mon_defense_m = mon_defense_m
        self.mon_pre_f = mon_pre_f
        self.mon_pre_m = mon_pre_m
