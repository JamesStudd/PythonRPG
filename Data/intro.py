import pygame as pg
import os
from Data.images import *
from Data.classes import *
pg.init()

class Dialogue():

    def __init__(self, background, char, filename):
        self.background = background
        self.char = char
        self.filename = filename
        self.state = 1
        check = open("Resources\\Scripts\\" + self.filename)
        self.num_lines = sum(1 for line in check)
        self.font_dialogue = pg.font.SysFont('Terminal', 20, False, False)
        
    def draw(self, surface):
        self.surface = surface
        self.surface.blit(IMAGES[self.background], (0, 0))
        self.surface.blit(IMAGES[self.char], (375, 400))
        self.surface.blit(IMAGES["bborder"], (247, 450))

        show = open("Resources\\Scripts\\" + self.filename)
        count = 0
        for lines in show:
            count += 1
            if count == self.state:
                if len(lines) >= 28:
                    count = 0
                    for letters in lines:
                        if count >= 28 and letters == " ":
                            break
                        count += 1
                    line1 = self.font_dialogue.render(lines[:count], True, pg.Color('black'))
                    line2 = self.font_dialogue.render(lines[count:-1], True, pg.Color('black'))
                    line1rect = line1.get_rect()
                    line2rect = line2.get_rect()

                    line1rect.centerx = 396
                    line1rect.y = 516

                    line2rect.centerx = 396
                    line2rect.y = 540

                    screen.blit(line1, line1rect)
                    screen.blit(line2, line2rect)

                else:
                
                    line = self.font_dialogue.render(lines[:-1], True, pg.Color('black'))
                    linerect = line.get_rect()
                    linerect.centerx = 396
                    linerect.y = 516
                    screen.blit(line, (linerect))
                

    def update(self, event):
        
        self.script = open("Resources\\Scripts\\" + self.filename)
        for lines in self.script:
            if self.state == self.num_lines:
                return True
            else:
                if event.type == pg.KEYUP:
                    self.state += 1
                    break
                
def show_intro():
    intro = Dialogue('intro', 'prof_croak', 'prof_croak_intro.txt')
    done = False
    gotrans = False
    trans = 0
    fader = IMAGES['fader']
    fader.convert_alpha()

    def blit_alpha(target, source, location, opacity):
        # http://www.nerdparadise.com/tech/python/pygame/blitopacity/
        x = location[0]
        y = location[1]
        temp = pg.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

    while done == False:
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYUP:
                if intro.update(event):
                    gotrans = True



        intro.draw(screen)
        
        if gotrans == True:
            blit_alpha(screen, fader, (0, 0), trans)
            trans += 1
            if trans == 255:
                done = True
            
        pg.display.flip()

    


