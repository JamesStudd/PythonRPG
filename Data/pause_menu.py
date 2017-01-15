import pygame as pg
from Data.images import *
from Data.rpg_button import RpgButton
pg.init()

def draw_pause_menu(surface):

    surface.blit(IMAGES['pause_menu'], (200, 200))
    r = RpgButton(200, 200)
    r.draw(surface, 'temp_button')
    r.update(pg.mouse.get_pos())