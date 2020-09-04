Player_Lv = int(input("Nivel del jugador "))
Enemy_Lv = int(input("Nivel del primer enemigo en la zona "))
SilverBake_Lv = Player_Lv + 5
GoldBake_Lv = Player_Lv + 10
PlatiBake_Lv = Player_Lv + 15
Levels_Needed = Enemy_Lv - Player_Lv

#Esta función define la cantidad de experiencia necesaria para subir de nivel
#actualmente
def Player_ExpNeeded(Player_Lv):
    return 100 + 20 ** ((Player_Lv - 1) * 0.1)

#Estas funciones definen la cantidad de experiencia que los Kuribake plateados
#dorados y platinos otorgan al ser derrotados
def SilverBake_ExpGift (SilverBake_Lv):
    return 100 + 5 ** ((SilverBake_Lv - 1) * 0.1)

def GoldBake_ExpGift (GoldBake_Lv):
    return 100 + 10 ** ((GoldBake_Lv - 4) * 0.1)

def PlatiBake_ExpGift (PlatiBake_Lv):
    return 100 + 15 ** ((PlatiBake_Lv - 15) * 0.1)

#Esta función define el tipo de Kuribake que el jugador deberá cazar
def Bake_Definer(Player_Lv):
    if Player_Lv <= 25:
        return 0
    elif Player_Lv <= 50:
        return 1
    else:
        return 2
    
#Esta función definirá la cantidad de experiencia total para llegar al nivel del
#monstruo de la zona nueva
#def Total_ExpNeeded(Player_ExpNeeded,Levels_Needed):
#Ciclo aquí
#Suma de Player_ExpNeeded iniciando desde el nivel actual sumandose por 1
#cada vez que se repita, repitiendo el número de veces que indique la variable
#Levels_Needed 

#Esta condicional determina cual Kuribake dar al jugador
if Bake_Definer(Player_Lv) == 0:
    ExpGift = SilverBake_ExpGift(SilverBake_Lv)
    Bake_Type = "Kuribake Plateado"
elif Bake_Definer(Player_Lv) == 1:
    ExpGift = GoldBake_ExpGift(GoldBake_Lv)
    Bake_Type = "Kuribake Dorado"
else:
    ExpGift = PlatiBake_ExpGift(PlatiBake_Lv)
    Bake_Type = "Kuribake Platino"

#Esto le dice al jugador si debe o no hacer grind
if Enemy_Lv < Player_Lv:
    print("No necesitas hacer grind para esta zona")
elif Enemy_Lv == Player_Lv:
    print("Es seguro entrar a esta zona")
else:
    print("Necesitas subir", Levels_Needed, "niveles")
    print("Para subir de nivel, necesitas", int(Player_ExpNeeded(Player_Lv)),
          "puntos de experiencia")
    print("En tu nivel actual, el",Bake_Type,"te dará", int(ExpGift),
          "puntos de experiencia")
    #print("Necesitas",Total_ExpNeeded(Player_ExpNeeded,Levels_Needed),"para
    #llegar al nivel",Enemy_Lv)
