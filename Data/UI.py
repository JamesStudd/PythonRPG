from Data.images import *
import pygame as pg
pg.init()

font_talk = pg.font.SysFont("monospace", 20)


class ui:

    current_text = None

    def __init__(self, player, minimap):
        self.player = player
        self.minimap = minimap


    def draw(self, surface):
        surface.blit(IMAGES['tempUI'], (0, 665))
        surface.blit(IMAGES['tempUIPlayer'], (30, 690))
        if self.current_text != None:
            surface.blit(self.current_text, (210, 700))

    def update(self, text):
        self.current_text = text
