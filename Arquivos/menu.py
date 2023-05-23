#menu
from atributes import Atributos
from atraso import delay

class Menu:

    menu_status = Atributos

    def status(menu_status):
        print("""   {0}\n   {1}\n   {0}""".format("=".center(12,"="),"STATUS".center(12)))
        delay()
        print(f"""
    - vida:       {menu_status.hp}
    - atk físico: {menu_status.atk_f}
    - atk mágico: {menu_status.atk_m}
    - velocidade: {menu_status.spd}
    - def física: {menu_status.defense_f}
    - def mágica: {menu_status.defense_m}
    - act físico: {menu_status.pre_f}
    - act mágico: {menu_status.pre_m} \n""")
        delay()
        seguir = input("Clique Enter para continuar\n")
        while seguir != '':
            delay()
            seguir = input("Clique Enter para continuar\n")
        pass
    
    #def inventory():
        