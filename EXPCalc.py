import random
'''
De la biblioteca random, uso la función random.randint(X,Y) que elige
un número entero que se encuentre entre los valores X y Y, esto hace
que haya una variación entre los niveles de los monstruos en los que se va a
hacer grind, por consecuencia hace que se cree una variación en los datos
calculados, ya que esto es un juego cuyos desarrolladores querían que no
fuera tan predecible
'''

player_lv = int(input("Nivel del jugador "))
enemy_lv = int(input("Nivel del primer enemigo en la zona "))
levels_needed = enemy_lv - player_lv


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


def total_bake_needed(player_lv, total_exp, enemy_lv):
    '''
    Esta función determina la cantidad de Kuribakes de cada tipo que se deben
    cazar, además hace cálculos extras si detecta que se requiere uno o varios
    cambios a media caza
    '''
    var = 1
    count = 0
    count2 = 0
    count3 = 0
    player_lv_dummy = 0
    levels_needed_dummy = 0
    total_exp_dummy = 0
    player_lv_dummy2 = 0
    levels_needed_dummy2 = 0
    total_exp_dummy2 = 0
    if ((enemy_lv <= 25 and player_lv < 25) or
            (enemy_lv <= 50 and player_lv >= 25) or
            (enemy_lv > 50 and player_lv >= 50)):
        while total_exp > 0:
                total_exp -= bake_param(player_lv)[0]
                count += 1
    elif ((50 > enemy_lv > 25 and player_lv < 25) or
            (enemy_lv > 50 and player_lv >= 25)):
        if enemy_lv > 50:
            var = 2
        player_lv_dummy = 25*var
        levels_needed_dummy = enemy_lv - player_lv_dummy
        total_exp_dummy = total_exp_needed(levels_needed_dummy,
                                           player_lv_dummy)
        while total_exp > 0:
            total_exp -= bake_param(player_lv)[0]
            count += 1
        while total_exp_dummy > 0:
            total_exp_dummy -= bake_param(player_lv_dummy)[0]
            count2 += 1
    elif (enemy_lv > 50 and player_lv < 25):
        player_lv_dummy = 25
        levels_needed_dummy = enemy_lv - player_lv_dummy
        total_exp_dummy = total_exp_needed(levels_needed_dummy,
                                           player_lv_dummy)
        player_lv_dummy2 = 50
        levels_needed_dummy2 = enemy_lv - player_lv_dummy2
        total_exp_dummy2 = total_exp_needed(levels_needed_dummy2,
                                            player_lv_dummy2)
        while total_exp > 0:
            total_exp -= bake_param(player_lv)[0]
            count += 1
        while total_exp_dummy > 0:
            total_exp_dummy -= bake_param(player_lv_dummy)[0]
            count2 += 1
        while total_exp_dummy2 > 0:
            total_exp_dummy2 -= bake_param(player_lv_dummy2)[0]
            count3 += 1
    return (str(count), str(count2), str(count3))


'''
Esto le dice al jugador si debe o no hacer grind, o si los datos son inválidos
'''
if player_lv < 1:
    print("Nivel de jugador inválido")
elif enemy_lv < 1:
    print("Nivel de enemigo inválido")
elif player_lv < 1 and enemy_lv < 1:
    print("Ambos datos son inválidos")
else:
    if enemy_lv < player_lv:
        print("No necesitas hacer grind para esta zona")
    elif enemy_lv == player_lv:
        print("Es seguro entrar a esta zona")
    else:
        '''
        Valores guardados para que al final todas las líneas a imprimir se
        muestren sin pausar
        '''
        total_exp = total_exp_needed(levels_needed, player_lv)
        t_bake, t_bake2, t_bake3 = (total_bake_needed(player_lv, total_exp,
                                                      enemy_lv))
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
              bake_param(player_lv)[1] +
              " te podría dar " +
              str(bake_param(player_lv)[0]) +
              " puntos de experiencia")
        print("Necesitas " +
              str(total_exp) +
              " puntos de experiencia para llegar al nivel " +
              str(enemy_lv))
        # De aqúi en adelante son todos los posibles resultados
        if t_bake2 == '0' and t_bake3 == '0':
            print("Puede que debas cazar " +
                  t_bake +
                  " Kuribakes para obtener la experiencia necesaria")
        elif t_bake2 != '0' and t_bake3 == '0':
            print("Puede que debas cazar " +
                  t_bake +
                  " Kuribakes para obtener la experiencia necesaria," +
                  " pero se recomienda que cuando llegues al siguiente" +
                  " rango, busques algún " +
                  bake_param(player_lv + 25)[1] +
                  " para que solo debas cazar alrededor de " +
                  t_bake2)
        elif t_bake2 != '0' and t_bake3 != '0':
            print("Puede que debas cazar " +
                  t_bake +
                  " Kuribakes para obtener la experiencia necesaria," +
                  " pero se recomienda que cuando llegues al siguiente" +
                  " rango, busques algún " +
                  bake_param(player_lv + 25)[1] +
                  " para que solo debas cazar alrededor de " +
                  t_bake2 +
                  " de esos, y finalmente, cuando llegues al último rango" +
                  " busques algún " +
                  bake_param(player_lv + 50)[1] +
                  " para que solo debas cazar alrededor de " +
                  t_bake3)
