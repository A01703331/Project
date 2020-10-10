player_lv = int(input("Nivel del jugador "))
enemy_lv = int(input("Nivel del primer enemigo en la zona "))
levels_needed = enemy_lv - player_lv

# Random hace que haya una ligera variación en el nivel de los Kuribakes
import random


def player_exp_needed(player_lv):
    """
    Esta función define la cantidad de experiencia necesaria para subir de
    nivel actualmente
    """
    return int(100 + 20 ** ((player_lv - 1) * 0.1))


def bake_param(player_lv):
    """
    Esta función define la cantidad de experiencia que los Kuribake otorgan
    al ser derrotados
    """
    silver_bake_lv = random.randint(player_lv + 4, player_lv + 6)
    gold_bake_Lv = random.randint(player_lv + 9, player_lv + 11)
    plati_bake_lv = random.randint(player_lv + 14, player_lv + 16)
    bake_exp = 0
    bake_type = ""
    if player_lv < 25:
        bake_exp = int(100 + 5 ** ((silver_bake_lv - 1) * 0.1))
        bake_type = "Kuribake Plateado"
        return (bake_exp, bake_type)
    elif player_lv < 50:
        bake_exp = int(100 + 10 ** ((gold_bake_Lv - 4) * 0.1))
        bake_type = "Kuribake Dorado"
        return (bake_exp, bake_type)
    else:
        bake_exp = int(100 + 15 ** ((plati_bake_lv - 15) * 0.1))
        bake_type = "Kuribake Platino"
        return (bake_exp, bake_type)


def total_exp_needed(levels_needed, player_lv):
    """
    Esta función define la cantidad de experiencia total para llegar al nivel
    del monstruo de la zona nueva
    """
    i = 0
    total_needed = 0
    while i < levels_needed:
        total_needed += player_exp_needed(player_lv)
        player_lv += 1
        i += 1
    return int(total_needed)


def total_bake_needed(player_lv, total_exp):
    # Esta función determina la cantidad de Kuribakes que se deben cazar
    i = 0
    while total_exp > 0:
        i += 1
        total_exp -= bake_param(player_lv)[0]
    return i


# Esto le dice al jugador si debe o no hacer grind
if player_lv < 1:
    print("Nivel de jugador inválido")
elif enemy_lv < 1:
    print("Nivel de enemigo inválido")
else:
    if enemy_lv < player_lv:
        print("No necesitas hacer grind para esta zona")
    elif enemy_lv == player_lv:
        print("Es seguro entrar a esta zona")
    else:
        if levels_needed == 1:
            print("Necesitas subir solo 1 nivel, ¡Ya casi llegas!")
        else:
            print("Necesitas subir " +
                    str(levels_needed) +
                    " niveles")
        print("Para subir de nivel, necesitas " +
                str(player_exp_needed(player_lv)) +
                " puntos de experiencia")
        print("En tu nivel actual, un " +
                str(bake_param(player_lv)[1]) +
                " te podría dar " +
                str(bake_param(player_lv)[0]) +
                " puntos de experiencia")
        total_exp = total_exp_needed(levels_needed, player_lv)
        print("Necesitas " +
                str(total_exp) +
                " puntos de experiencia para llegar al nivel " +
                str(enemy_lv))
        total_bake = total_bake_needed(player_lv, total_exp)
        if enemy_lv <= 25 and player_lv < 25:
            print("Puede que debas cazar " +
                    str(total_bake) +
                    " Kuribakes Plateados para obtener la experiencia " +
                    "necesaria")
        elif enemy_lv <= 50 and player_lv < 25:
            print("Puede que debas cazar " +
                    str(total_bake) +
                    " Kuribakes Plateados para obtener la experiencia " +
                    "necesaria")
            print("Se recomienda rehacer el cálculo cuando llegues al" +
                    " nivel 25")
        elif enemy_lv > 50 and player_lv < 25:
            print("Puede que debas cazar " +
                    str(total_bake) +
                    " Kuribakes Plateados para obtener la experiencia " +
                    "necesaria")
            print("Se recomienda rehacer el cálculo cuando llegues al" +
                    " nivel 25 y una vez más al nivel 50")
        elif enemy_lv <= 50 and player_lv >= 25:
            print("Puede que debas cazar " +
                    str(total_bake) +
                    " Kuribakes Dorados para obtener la experiencia " +
                    "necesaria")
        elif enemy_lv > 50 and player_lv < 50:
            print("Puede que debas cazar " +
                    str(total_bake) +
                    " Kuribakes Dorados para obtener la experiencia " +
                    "necesaria")
            print("Se recomienda rehacer el cálculo cuando llegues al" +
                    " nivel 50")
        elif enemy_lv > 50 and player_lv >= 50:
            print("Puede que debas cazar " +
                    str(total_bake) +
                    " Kuribakes Platino para obtener la experiencia " +
                    "necesaria")
