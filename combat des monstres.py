import random
import time
import arcade # Je n'ai pas pu faire fonctioner les graphismes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
WINDOW_TITLE = 'Combat des monstres!'

# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

# arcade.set_background_color((238, 197, 132))

# arcade.start_render()

# arcade.draw_lrtb_rectangle_filled(200, 599, 800, 0, (150, 102, 62))

# arcade.draw_lrtb_rectangle_filled(370, 420, 150, 100, (000, 000, 000))

# arcade.draw_lrtb_rectangle_filled(180, 200, 400, 300, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(599, 619, 400, 300, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(599, 619, 200, 100, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(180, 200, 200, 100, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(180, 200, 600, 500, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(180, 200, 800, 700, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(599, 619, 600, 500, (97, 50, 12))

# arcade.draw_lrtb_rectangle_filled(599, 619, 800, 700, (97, 50, 12))

# arcade.finish_render()

# arcade.run()

niveau_vie = 20
nombre_victoires = 0
nombre_defaites = 0
numero_combat = 0
numero_adversaire = 0

jouer = input('vouler vous jouez a combat de monstres? (o) ou (n).')

while jouer == 'o':

    if nombre_victoires == 3:

        print('le boss est apparue, vous devez le battre! il faudrait que le score du dé soi égale a 6.')
        time.sleep(1.0)
        score_dé = random.randint(1, 6)
        print('le score du dé est de', score_dé)

        if score_dé < 6:

            print('bravo! Tu as battu le boss!')
            time.sleep(0.5)

            rejouer = input('veut tu rejouer? (o) ou (n)')
            if rejouer == 'o':
                continue
            else:
                print("merci d'avoir jouer!")
                break

        else:
            print('tu as perdu contre le boss')

    force_adversaire = random.randint(1, 5)
    print('Vous tombez face à face avec un adversaire de difficulté :', force_adversaire,)
    time.sleep(0.5)

    choix = input('Que voulez vous faire?\n'
          '1.Combattre cet adversaire\n'
          '2.Contourner cet adversaire et aller ouvrir une autre porte\n'
          '3.Afficher les règles du jeu\n'
          '4.Quitter la partie')

    if choix == '1':
        numero_adversaire = numero_adversaire + 1
        score_dé = random.randint(1, 6)

        print('adversaire:', numero_adversaire)
        print("force de l'adversaire:", force_adversaire)
        print("niveau de vie", niveau_vie)
        print(numero_combat, ':', nombre_victoires, 'vs', nombre_defaites)
        time.sleep(1.0)

        print('lancer du dé:', score_dé)

        if score_dé > force_adversaire:
            print(score_dé, '>', force_adversaire)

            print('voctoire!')
            nombre_victoires = nombre_victoires + 1
            time.sleep(0.5)

            niveau_vie = niveau_vie + force_adversaire
            print(niveau_vie)
            force_adversaire = 0
            time.sleep(0.5)

        elif score_dé <= force_adversaire:
            print(score_dé, '<=', force_adversaire)
            


            niveau_vie = niveau_vie + force_adversaire
            print(niveau_vie)

    elif choix == '2':
        print(1)
