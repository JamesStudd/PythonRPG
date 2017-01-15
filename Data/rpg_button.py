import pygame as pg
from Data.images import *
pg.init()


class RpgButton():

    clicked = False
    x = 0
    y = 0
    image = None

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, surface):
        self.surface = surface
        self.surface.blit(IMAGES[self.image], (self.x, self.y))

    def update(self, pos):
        if pg.mouse.get_pressed()[0]:
            if all((pos[0] >= self.x, pos[0] <= self.x + 100, pos[1] >= self.y, pos[1] <= self.y + 30)):
                print("it happened")
