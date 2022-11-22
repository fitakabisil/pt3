import random
import time
import arcade
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 750
#WINDOW_TITLE = 'Combat des monstres!'

#arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

#arcade.set_background_color((238, 197, 132))

#arcade.start_render()

#arcade.draw_lrtb_rectangle_filled(200, 599, 800, 0, (150, 102, 62))

#arcade.draw_lrtb_rectangle_filled(370, 420, 150, 100, (000,000,000))

#arcade.draw_lrtb_rectangle_filled(180, 200, 400, 300, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(599, 619, 400, 300, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(599, 619, 200, 100, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(180, 200, 200, 100, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(180, 200, 600, 500, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(180, 200, 800, 700, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(599, 619, 600, 500, (97, 50, 12))

#arcade.draw_lrtb_rectangle_filled(599, 619, 800, 700, (97, 50, 12))

#arcade.finish_render()

niveau_vie = 20
mini = 1
maxi = 6
nombre_victoires = 0
nombre_défaites = 0
nombre_adversaires = 0
boss = 6


jouer = input('vouler vous jouez a combat de monstres? (o) ou (n).')

while jouer == 'o':
    force_adversaire = random.randint(int(mini), 5)
    print('Vous tombez face à face avec un adversaire de difficulté :', force_adversaire,)
    time.sleep(0.5)
    choix = input('Que voulez vous faire?\n'
          '1.Combattre cet adversaire\n'
          '2.Contourner cet adversaire et aller ouvrir une autre porte\n'
          '3.Afficher les règles du jeu\n'
          '4.Quitter la partie')
    if choix == 1:

arcade.run()

niveau_vie = 20

force_adversaire = 0
