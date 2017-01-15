import pygame as pg
from Data.images import *
pg.init()


class RpgButton():

    clicked = False
    x = 0
    y = 0
    image = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        self.surface = surface
        self.image = image
        self.surface.blit(IMAGES[self.image], (self.x, self.y))

    def update(self, pos):
        print(pos)
