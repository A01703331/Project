PlayerLv = int(input("Nivel del jugador "))
EnemyLv = int(input("Nivel del primer enemigo en la zona "))
LevelsNeeded = EnemyLv - PlayerLv

# Random hace que haya una ligera variación en el nivel de los Kuribakes
import random

"""
Esta función define la cantidad de experiencia necesaria para subir de
nivel actualmente
"""


def PlayerExpNeeded(PlayerLv):
    return int(100 + 20 ** ((PlayerLv - 1) * 0.1))


"""
Esta función define la cantidad de experiencia que los Kuribake otorgan al
ser derrotados, y también dice con cual iniciar la caza
"""


def BakeParam(PlayerLv):
    SilverBakeLv = random.randint(PlayerLv + 4, PlayerLv + 6)
    GoldBakeLv = random.randint(PlayerLv + 9, PlayerLv + 11)
    PlatiBakeLv = random.randint(PlayerLv + 14, PlayerLv + 16)
    if PlayerLv <= 25:
        return int(100 + 5 ** ((SilverBakeLv - 1) * 0.1)), "KuriBake Plateado"
    elif PlayerLv <= 50:
        return int(100 + 10 ** ((GoldBakeLv - 4) * 0.1)), "KuriBake Dorado"
    else:
        return int(100 + 15 ** ((PlatiBakeLv - 15) * 0.1)), "KuriBake Platino"


"""
Esta función define la cantidad de experiencia total para llegar al nivel
del monstruo de la zona nueva
"""


def TotalExpNeeded(LevelsNeeded, PlayerLv):
    Count = 0
    TotalNeeded = 0
    while Count < LevelsNeeded:
        TotalNeeded += PlayerExpNeeded(PlayerLv)
        PlayerLv += 1
        Count += 1
    return int(TotalNeeded)


"""
Esta función determina la cantidad de Kuribakes que se deben cazar, e indica
si se debe hacer un cambio a media caza
"""


def TotalBakeNeeded(PlayerLv, TotalExp):
    Count = 0
    while TotalExp > 0:
        Count += 1
        TotalExp -= BakeParam(PlayerLv)[0]
    return Count
    

# Esto le dice al jugador si debe o no hacer grind
if EnemyLv < PlayerLv:
    print("No necesitas hacer grind para esta zona")
elif EnemyLv == PlayerLv:
    print("Es seguro entrar a esta zona")
else:
    if LevelsNeeded == 1:
        print("Necesitas subir solo 1 nivel, ¡Ya casi llegas!")
    else:
        print("Necesitas subir", LevelsNeeded, "niveles")
    print("Para subir de nivel, necesitas", PlayerExpNeeded(PlayerLv),
            "puntos de experiencia")
    print("En tu nivel actual, el", BakeParam(PlayerLv)[1], "te podría dar",
            BakeParam(PlayerLv)[0], "puntos de experiencia")
    TotalExp = TotalExpNeeded(LevelsNeeded, PlayerLv)
    print("Necesitas", TotalExp, "puntos de experiencia para llegar al nivel",
            EnemyLv)
    TotalBake = TotalBakeNeeded(PlayerLv, TotalExp)
    print("Puede que debas cazar", TotalBake, "Kuribakes para obtener la",
            "experiencia necesaria")
