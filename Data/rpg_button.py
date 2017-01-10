import pygame as pg
from Data.images import *
pg.init()


class RpgButton():

    clicked = False
    x, y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        self.surface = surface
        self.surface.blit(IMAGES[image], (self.x, self.y))

