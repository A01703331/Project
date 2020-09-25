player_lv = int(input("Nivel del jugador "))
enemy_lv = int(input("Nivel del primer enemigo en la zona "))
levels_needed = enemy_lv - player_lv

# Random hace que haya una ligera variación en el nivel de los Kuribakes
import random

"""
Esta función define la cantidad de experiencia necesaria para subir de
nivel actualmente
"""


def player_exp_needed(player_lv):
    return int(100 + 20 ** ((player_lv - 1) * 0.1))


"""
Esta función define la cantidad de experiencia que los Kuribake otorgan al
ser derrotados, y también dice con cual iniciar la caza
"""


def bake_param(player_lv):
    silver_bake_lv = random.randint(player_lv + 4, player_lv + 6)
    gold_bake_Lv = random.randint(player_lv + 9, player_lv + 11)
    plati_bake_lv = random.randint(player_lv + 14, player_lv + 16)
    if player_lv <= 25:
        return (int(100 + 5 ** ((silver_bake_lv - 1) * 0.1)),
                "KuriBake Plateado")
    elif player_lv <= 50:
        return (int(100 + 10 ** ((gold_bake_Lv - 4) * 0.1)),
                "KuriBake Dorado")
    else:
        return (int(100 + 15 ** ((plati_bake_lv - 15) * 0.1)),
                "KuriBake Platino")


"""
Esta función define la cantidad de experiencia total para llegar al nivel
del monstruo de la zona nueva
"""


def total_exp_needed(levels_needed, player_lv):
    count = 0
    total_needed = 0
    while count < levels_needed:
        total_needed += player_exp_needed(player_lv)
        player_lv += 1
        count += 1
    return int(total_needed)


"""
Esta función determina la cantidad de Kuribakes que se deben cazar, e
indicará si se debe hacer un cambio a media caza
"""


def total_bake_needed(player_lv, total_exp):
    count = 0
    while total_exp > 0:
        total_exp -= bake_param(player_lv)[0]
        count += 1
    return count


# Esto le dice al jugador si debe o no hacer grind
if enemy_lv < player_lv:
    print("No necesitas hacer grind para esta zona")
elif enemy_lv == player_lv:
    print("Es seguro entrar a esta zona")
else:
    if levels_needed == 1:
        print("Necesitas subir solo 1 nivel, ¡Ya casi llegas!")
    else:
        print("Necesitas subir " + str(levels_needed) + " niveles")
    print("Para subir de nivel, necesitas " +
          str(player_exp_needed(player_lv)) + " puntos de experiencia")
    print("En tu nivel actual, el " + str(bake_param(player_lv)[1]) + " te " +
          "podría dar " + str(bake_param(player_lv)[0]) + " puntos de" +
          " experiencia")
    total_exp = total_exp_needed(levels_needed, player_lv)
    print("Necesitas " + str(total_exp) + " puntos de experiencia para llegar"
          + " al nivel " + str(enemy_lv))
    total_bake = total_bake_needed(player_lv, total_exp)
    print("Puede que debas cazar " + str(total_bake) + " Kuribakes para " +
          "obtener la experiencia necesaria")
