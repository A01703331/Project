Player_Lv=int(input("Nivel del jugador "))
Enemy_Lv=int(input("Nivel del primer enemigo en la zona "))
SilverBake_Lv=Player_Lv+5
Levels_Needed=Enemy_Lv-Player_Lv

#Esta función define la cantidad de experiencia necesaria para subir de nivel actualmente
def Player_ExpNeeded(Player_Lv):
    ExpPerLv=100+10**((Player_Lv-1)*0.1)
    return ExpPerLv

#Esta función define la cantidad de experiencia que el monstruo plateado otorga al ser derrotado
def SilverBake_ExpGift (SilverBake_Lv):
    SilverBake_Exp=50+10**((SilverBake_Lv-1)*0.1)
    return SilverBake_Exp

#Esto le dice al jugador si debe o no hacer grind
if Enemy_Lv<Player_Lv:
    print("No necesitas hacer grind para esta zona")
elif Enemy_Lv==Player_Lv:
    print("Es seguro entrar a esta zona")
else:
    print("Necesitas subir",Levels_Needed,"niveles")
    print("Para subir de nivel, necesitas",int(Player_ExpNeeded(Player_Lv)),"puntos de experiencia")
    print("En tu nivel actual, el monstruo plateado te dará",int(SilverBake_ExpGift(SilverBake_Lv)),"puntos de experiencia")


