import random
import time
import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = 'Combat des monstres!'
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
arcade.set_background_color(arcade.color.ARYLIDE_YELLOW)
arcade.start_render()
arcade.finish_render()
arcade.run()

niveau_vie = 20
force_adversaire = 0