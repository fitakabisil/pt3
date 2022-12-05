import random
import time
import arcade # Je n'ai pas pu faire fonctioner les graphismes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
WINDOW_TITLE = 'Combat des monstres!'

# je n'ai pa pu faire fonctionner les graphismes

# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

# arcade.set_background_color((238, 197, 132))

# arcade.start_render()

# arcade.draw_lrtb_rectangle_filled(200, 599, 800, 0, (150, 102, 62))

# arcade.draw_lrtb_rectangle_filled(370, 420, 150, 100, (000, 000, 000))

# arcade.finish_render()

# arcade.run()

niveau_vie = 20
nombre_victoires = 0
nombre_defaites = 0
numero_combat = 0
numero_adversaire = 0

# la variable pour enclancher le jeu
jouer = input('vouler vous jouez a combat de monstres? (o) ou (n).')

# si le joueur veut jouer. la boucle fait en sort que le jeu va continuer jusqu'à ce que le joueur fini le jeu
while jouer == 'o':

    # si le n_v est plus petit ou égale à 0, le jouer perd la partie
    if niveau_vie <= 0:
        print('vous avez perdu :(')
        break

    # le combat contre le bosse va ce lancer quand le joueur va avoir 3 victoires
    if nombre_victoires == 3:

        print('le boss est apparue, vous devez le battre! il faudrait que le score du dé soi égale a 6.')
        time.sleep(2.0)
        score_dé = random.randint(1, 6)
        print('le score du dé est de', score_dé)
        time.sleep(1.0)

        # si le joueur bat le boss
        if score_dé == 6:

            print('bravo! Tu as battu le boss!')
            time.sleep(0.5)

            # le jouer a le choix de rejouer ou finir la partie
            rejouer = input('veut tu rejouer? (o) ou (n)')
            if rejouer == 'o':
                continue
            else:
                print("merci d'avoir jouer!")
                break

        # si le joueur est battu par le boss, le programe va finir
        else:
            print('tu as perdu contre le boss')
            break

    # fonction qui va déterminer la force du monstre
    force_adversaire = random.randint(1, 5)
    print('Vous tombez face à face avec un adversaire de difficulté :', force_adversaire,)
    time.sleep(0.5)

    # le joueur a quatre choix a faire
    choix = input('Que voulez vous faire?\n'
          '1.Combattre cet adversaire\n'
          '2.Contourner cet adversaire et aller ouvrir une autre porte\n'
          '3.Afficher les règles du jeu\n'
          '4.Quitter la partie')

    # si le joueur choisie de combattre le monstre, le jeu va d'abord montrer les statistiques
    if choix == '1':
        numero_adversaire = numero_adversaire + 1
        score_dé = random.randint(1, 6)
        numero_combat = numero_combat + 1

        print('adversaire:', numero_adversaire)
        print("force de l'adversaire:", force_adversaire)
        print("niveau de vie", niveau_vie)
        print('numero du combat:', numero_combat, ':', 'nombre de victoires:', nombre_victoires, 'vs', 'nombre de défaites:', nombre_defaites)
        time.sleep(2.0)

        print('lancer du dé:', score_dé)

        # si le lancer du dé est plus grand que la force du monstre, le joueur va gagner
        if score_dé > force_adversaire:
            print(score_dé, '>', force_adversaire)
            time.sleep(1.0)

            print('victoire!')
            nombre_victoires = nombre_victoires + 1
            time.sleep(0.5)

            # le joueur va gagner des niveaux de vie égale a la force du monstre
            niveau_vie = niveau_vie + force_adversaire
            print('niveau de vie:', niveau_vie)
            force_adversaire = 0
            time.sleep(0.5)

        # si le lancer du dé est plus petit ou égale à la force de du monstre, le joueur perd et la force du monstre est sousttraite de ces niveaux de vie
        else:
            print('défait!')
            print(score_dé, '<=', force_adversaire)
            niveau_vie -= force_adversaire
            time.sleep(2.0)
            print('niveau de vie:', niveau_vie)

    # le joueur évite le monstre mais 1 niveau de vie est soustrait
    elif choix == '2':
        print('vous avez eviter le monstre mais, vous perdez 1 niveau de vie')
        niveau_vie = niveau_vie - 1
        time.sleep(1.0)
        print('niveau de vie:', niveau_vie)

    # le programe va expliquer comment le jeu fonctione
    elif choix == '3':
        print('Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n'
              'Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n'
              'Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n'
              'ans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n'
              'La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n'
              'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n')
        time.sleep(10.5)

    # le programme va s'arreter
    elif choix == '4':
        print('merci et au revoir...')
