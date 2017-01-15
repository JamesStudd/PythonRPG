import pygame as pg
from Data.images import *
from Data.rpg_button import RpgButton
pg.init()

def draw_pause_menu(surface):

    surface.blit(IMAGES['pause_menu'], (200, 200))
    list_of_buttons = []
    inventory_button = RpgButton(300, 300, 'temp_button_inventory')
    list_of_buttons.append(inventory_button)

    save_button = RpgButton(300, 340, 'temp_button_save')
    list_of_buttons.append(save_button)

    load_button = RpgButton(300, 380, 'temp_button_load')
    list_of_buttons.append(load_button)

    options_button = RpgButton(300, 420, 'temp_button_options')
    list_of_buttons.append(options_button)

    quit_button = RpgButton(300, 460, 'temp_button_quit')
    list_of_buttons.append(quit_button)

    for b in list_of_buttons:
        b.draw(surface)
        b.update(pg.mouse.get_pos())