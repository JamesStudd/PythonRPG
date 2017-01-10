from Data.images import *
import pygame as pg
pg.init()

font_talk = pg.font.SysFont("monospace", 15)


class hud:

    speed = 0
    health = 0
    damage = 0

    def __init__(self, player):
        self.player = player
        self.speed = player.speed
        self.health = player.health
        self.damage = player.damage
        self.name_text = font_talk.render(player.name, True, pg.Color("black"))
        self.speed_text = font_talk.render(("Speed: "+str(self.speed)), True, pg.Color("black"))
        self.health_text = font_talk.render(("Health: "+str(self.health)), True, pg.Color("black"))
        self.damage_text = font_talk.render(("Damage: "+str(self.damage)), True, pg.Color("black"))
        if player.gender == "male":
            self.image = pg.transform.scale(IMAGES['male_icon'], (100,100))
        else:
            self.image = pg.transform.scale(IMAGES['female_icon'], (100,100))

        
    def draw(self, surface):
        surface.blit(IMAGES['tempUI'], (0, 665))
        surface.blit(self.image, (30, 690))
        surface.blit(self.name_text, (150, 700))
        surface.blit(self.speed_text, (150, 715))
        surface.blit(self.health_text, (150, 730))
        surface.blit(self.damage_text, (150, 745))
        
        #if self.current_text != None:
        #    surface.blit(self.current_text, (210, 700))

    def update(self, speed, health, damage):
        self.speed = speed
        self.health = health
        self.damage = damage
        self.speed_text = font_talk.render(("Speed: "+str(self.speed)), True, pg.Color("black"))
        self.health_text = font_talk.render(("Health: "+str(self.health)), True, pg.Color("black"))
        self.damage_text = font_talk.render(("Damage: "+str(self.damage)), True, pg.Color("black"))
