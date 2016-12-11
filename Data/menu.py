import pygame as pg
import os
from Data.spritesheet_functions import SpriteSheet
from Data.images import *
from Data.level_classes import *
from Data.player_related import *
import Data.eztext
pg.init()

class Menu():

    font_name = pg.font.SysFont('Terminal', 22, True, False)
    txtbx = Data.eztext.Input(maxlength=10, color=(0, 0, 0), prompt='Name: ')
    txtbx.set_pos(330, 436)
    txtbx.set_font(font_name)
    
    def __init__(self, background):
        self.rightclicked = 0
        self.background = background
        self.position = 0
        self.left_button = None
        self.right_button = None
        
        sprite_sheet = SpriteSheet('Resources\\main_character.png')
        image = sprite_sheet.get_image(0, 635, 30, 51)
        self.male = image

        sprite_sheet = SpriteSheet('Resources\\main_character_female.png')
        image = sprite_sheet.get_image(0, 635, 30, 51)
        self.female = image

        sprite_sheet = SpriteSheet('Resources\\bill.png')
        image = sprite_sheet.get_image(64, 0, 32, 48)
        image.set_colorkey(pg.Color('white'))
        self.bill = image

    def draw(self, surface):
        self.surface = surface
        self.surface.blit(IMAGES[self.background], (0, 0))

        pg.draw.rect(self.surface, (255, 255, 255), (326, 430, 170, 30), 0)
        self.txtbx.draw(self.surface)
        self.left_button = surface.blit(IMAGES['left_orange'], (325, 383))
        self.right_button = surface.blit(IMAGES['right_orange'], (465, 383))

        if self.position == 0:
            self.surface.blit(self.male, (398, 320))
        elif self.position == 1:
            self.surface.blit(self.female, (398, 320))
        elif self.position == 2:
            self.surface.blit(self.bill, (398, 320))

    def update(self, pos):
        if self.left_button != None:
            if self.left_button.collidepoint(pos):
                self.rightclicked = 0
                if self.position == 0:
                    pass
                elif self.position != 0:
                    self.position -= 1
            elif self.right_button.collidepoint(pos):
                self.rightclicked += 1
                if self.rightclicked >= 50:
                    self.position = 2
                if self.position == 1 or self.position == 2:
                    pass
                elif self.position == 0:
                    self.position += 1
        
    def update_text(self, events):
        self.player_name = self.txtbx.update(events)

        if self.player_name != None:
            if self.position == 0:
                self.gender = "male"
            elif self.position == 1:
                self.gender = "female"
            elif self.position == 2:
                self.gender = "bill"
            return True
            
def char_create():
    main_menu = Menu('main_menu')
    done = False

    while done==False:
        events = pg.event.get()

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                main_menu.update(pg.mouse.get_pos())
            change = main_menu.update_text(events)
            if change:
                done = True

        main_menu.draw(screen)
        pg.display.flip()

    player = Player(main_menu.gender)
    player.name = main_menu.player_name
    player.rect.x = 1800
    player.rect.y = 1800
    return player
        
