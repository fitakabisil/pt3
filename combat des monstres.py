import random
import time
import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
WINDOW_TITLE = 'Combat des monstres!'

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color((238, 197, 132))

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(200, 599, 800, 0, (150, 102, 62))

arcade.draw_lrtb_rectangle_filled(370, 420, 150, 100, (000,000,000))

arcade.draw_lrtb_rectangle_filled(180, 200, 400, 300, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(599, 619, 400, 300, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(599, 619, 200, 100, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(180, 200, 200, 100, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(180, 200, 600, 500, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(180, 200, 800, 700, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(599, 619, 600, 500, (97, 50, 12))

arcade.draw_lrtb_rectangle_filled(599, 619, 800, 700, (97, 50, 12))

arcade.finish_render()

arcade.run()

niveau_vie = 20

force_adversaire = 0
