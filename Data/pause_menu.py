import pygame as pg
from Data.images import *
pg.init()


def draw_pause_menu(surface):

     surface.blit(IMAGES['pause_menu'], (200, 200))
