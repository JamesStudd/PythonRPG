import pygame as pg
from Data.spritesheet_functions import SpriteSheet
from Data.images import *
from pytmx import *
import random
pg.init()


class NPC(pg.sprite.Sprite):
    """ NPC super class, allowing for movement and a few basic properties """
    level = None
    walking_frames_l = []
    walking_frames_u = []
    walking_frames_d = []
    walking_frames_r = []
    talk_approved = False
    talk_line = ""
    talk_line_index_at = 1

    direction = {"R": [1, 0], "U": [0, -1], "D": [0, 1], "L": [-1, 0], "S": [0, 0]}

    def __init__(self, name, x, y, sheet, health, damage):
        super().__init__()

        sprite_sheet = SpriteSheet('Resources\\' + sheet)
        image = sprite_sheet.get_image(0, 0, 32, 48)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(32, 0, 32, 48)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(64, 0, 32, 48)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(96, 0, 31, 48)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(0, 48, 32, 48)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(32, 48, 32, 48)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(64, 48, 32, 48)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(96, 48, 31, 48)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 96, 32, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(96, 96, 31, 48)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(0, 144, 32, 48)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(32, 144, 32, 48)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(64, 144, 32, 48)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(96, 144, 31, 48)
        self.walking_frames_u.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.health = health
        self.damage = damage

        self.ticker = 0


class Interactable(NPC):
    """ Currently unused """
    change_x = 0
    change_y = 0

    directionAnimate = "R"
    actualDirection = "R"

    controller = 0
    animater = 0
    text_filename = ""

    def talk(self, text_filename):
        self.text_filename = text_filename
        self.script = open("Resources\\Scripts\\" + self.text_filename + ".txt")
        count = 0
        for lines in self.script:
            self.talk_approved = True
            count += 1
            if count == self.talk_line_index_at:
                self.talk_line = return_talk_font().render(lines[0:len(lines) - 1], True, pg.Color("white"))
        self.talk_line_index_at += 1
        if self.talk_line_index_at == count + 1:
            self.talk_line_index_at = 1
        self.script.close()

    ##    def talk(self, text_filename):
    ##
    ##        if self.reward == False:
    ##            self.text_filename = text_filename
    ##            self.script = open("Resources\\Scripts\\" + self.text_filename)
    ##            count = 0
    ##            for lines in self.script:
    ##                count += 1
    ##                if count == self.NPC_text_state:
    ##                    self.NPC_talk = font_talk.render(lines[0:len(lines) - 1], True, pg.Color("white"))
    ##            self.NPC_text_state_limit = count
    ##            self.script.close()
    ##
    ##        if self.has_quest == True and self.reward == False:
    ##            self.quest_filename = self.name + "_quest" + ".txt"
    ##            self.quest_script = open("Resources\\Scripts\\" + self.quest_filename)
    ##            for lines in self.quest_script:
    ##                check = lines.split()
    ##                count = 0
    ##                if len(check) > 4:
    ##                    for letters in lines:
    ##                        count += 1
    ##                        if count >= len(lines) / 2 and letters == " ":
    ##                            self.quest_text_one = lines[0:count-1]
    ##                            self.quest_text_two = lines[count:]
    ##                            break
    ##                self.length_of_line = len(lines) * 4
    ##                self.NPC_quest_talk = font_talk.render(lines, True, pg.Color('white'))
    ##            self.quest_script.close()
    ##
    ##        if self.reward == True:
    ##            self.reward_filename = self.name + "_reward" + ".txt"
    ##            self.reward_script = open("Resources\\Scripts\\" + self.reward_filename)
    ##            for lines in self.reward_script:
    ##                self.length_of_line = len(lines) * 4
    ##                self.NPC_reward_talk = font_talk.render(lines, True, pg.Color('white'))
    ##            self.reward_script.close()
    ##
    ##            if self.item == True:
    ##                self.item_filename = self.name + "_item" + ".txt"
    ##                self.give_item = open("Resources\\Scripts\\" + self.item_filename)
    ##                count = 0
    ##                for line in self.give_item:
    ##                    count += 1
    ##                    if count == 1:
    ##                        one = line[:len(line)-1]
    ##                    elif count == 2:
    ##                        two = line[:len(line)-1]
    ##                    elif count == 3:
    ##                        three = line[:len(line)-1]
    ##                    elif count == 4:
    ##                        four = line[:len(line)-1]
    ##                    elif count == 5:
    ##                        five = int(line[:len(line)-1])
    ##                    else:
    ##                        pass
    ##
    ##                self.give_item.close()
    ##                add_to_inv(one, two, three, four, five)


    def update(self, player):
        """ Randomly chooses a direction to move in. Upon collision with player, stops. """
        if self.controller != 6:
            self.controller += 1
        elif self.controller == 6:
            self.animater += 1
            self.controller = 0

        if self.animater == 4:
            self.animater = 0

        if self.ticker == 0:
            move = random.choice(list(self.direction.keys()))

            self.stop = random.choice((4, 5, 6, 7, 8, 9, 10))
            self.ticker += 1
            self.change_x = self.direction[move][0]
            self.change_y = self.direction[move][1]
            self.directionAnimate = move

        elif self.ticker < (self.stop * 30) and self.ticker != 0:
            self.ticker += 1

        elif self.ticker == (self.stop * 30):
            self.ticker = 0

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        Nposx = self.rect.x + self.level.world_shift_x
        Nposy = self.rect.y + self.level.world_shift_y

        if self.directionAnimate == "R":
            self.actualDirection = "R"
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_r[0]
            else:
                self.image = self.walking_frames_r[self.animater]

        if self.directionAnimate == "L":
            self.actualDirection = "L"
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_l[0]
            else:
                self.image = self.walking_frames_l[self.animater]

        if self.directionAnimate == "U":
            self.actualDirection = "U"
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_u[0]
            else:
                self.image = self.walking_frames_u[self.animater]

        if self.directionAnimate == "D":
            self.actualDirection = "D"
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_d[0]
            else:
                self.image = self.walking_frames_d[self.animater]

        if pg.sprite.collide_rect(player, self):

            if player.change_x < 0:
                player.rect.left = self.rect.right + 1

            elif player.change_x > 0:
                player.rect.right = self.rect.left - 1

            elif player.change_y < 0:
                player.rect.top = self.rect.bottom + 1

            elif player.change_y > 0:
                player.rect.bottom = self.rect.top - 1

            player.move(0)
            self.change_x = 0
            self.change_y = 0

