import pygame as pg
pg.init()

font_talk = pg.font.SysFont("monospace", 20)


class timed_message:

    def __init__(self, surface, text_to_display, x, y, time):
        self.surface = surface
        self.text_to_display = text_to_display
        self.x = x
        self.y = y
        self.time = time

    def draw(self):
        if self.time > 0:
            self.surface.blit(self.text_to_display, (self.x, self.y))
            self.time -= 1
