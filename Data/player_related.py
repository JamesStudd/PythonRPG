import pygame as pg
from Data.spritesheet_functions import SpriteSheet
from Data.images import *
from pytmx import *
import random
pg.init()

class Player(pg.sprite.Sprite):
    """ My Main Player """
    speed = 10

    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []
    quests_accepted = []

    direction = "R"  # Direction is important for animations

    level = None  # Only 1 level so far - overworld_main
    name = None  # Name is set on the main character creation screen
    inside = False
    transitionhit = False
    transitiontogoto = 0;
    interact_button_hit = False

    def __init__(self, gender):
        super().__init__()  # Super class is pygame sprite

        self.gender = gender

        self.walking_frames_l = sort_player_spritesheet("left", self.gender)
        self.walking_frames_r = sort_player_spritesheet("right", self.gender)
        self.walking_frames_u = sort_player_spritesheet("up", self.gender)
        self.walking_frames_d = sort_player_spritesheet("down", self.gender)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()

    def update(self):

        self.rect.x += self.change_x  # Move the player left (-) or right (+)
        self.rect.y += self.change_y  # Move the player up (-) or down (+)

        posx = self.rect.x + self.level.world_shift_x  # Absolute position
        posy = self.rect.y + self.level.world_shift_y  # Absolute position

        if self.direction == "R":
            frame = (posx // 20) % (len(self.walking_frames_r) - 1)  # If the player is moving right we
            self.image = self.walking_frames_r[frame+1]  # want the correct animation, etc for next lines
        if self.direction == "L":                        # - 1 and + 1 is used so that I can include the
            frame = (posx // 20) % (len(self.walking_frames_l) - 1)  # "Stood still" image without including
            self.image = self.walking_frames_l[frame+1]              # it into the animation of the character
        if self.direction == "U":
            frame = (posy // 20) % (len(self.walking_frames_u) - 1)
            self.image = self.walking_frames_u[frame+1]
        if self.direction == "D":
            frame = (posy // 20) % (len(self.walking_frames_d) - 1)
            self.image = self.walking_frames_d[frame+1]

        if self.change_x == 0 and self.change_y == 0:
            if self.direction == "R":
                self.image = self.walking_frames_r[0]
            elif self.direction == "L":
                self.image = self.walking_frames_l[0]
            elif self.direction == "U":
                self.image = self.walking_frames_u[0]
            elif self.direction == "D":
                self.image = self.walking_frames_d[0]

        if self.rect.right > SCREEN_RECT.right:  # If the player moves all the way to the end of the screen
            self.rect.x -= 5  # we need to stop the player from moving and also set their
            self.change_x = 0  # position to a little bit left of the edge
            self.change_y = 0

        if self.rect.left < SCREEN_RECT.left:  # etc
            self.rect.x += 5
            self.change_x = 0
            self.change_y = 0

        if self.rect.top < SCREEN_RECT.top:
            self.rect.y += 5
            self.change_x = 0
            self.change_y = 0

        if self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.y -= 5
            self.change_x = 0
            self.change_y = 0

    def move(self, key):

        if key == 97:  # Key - Values
            self.change_x = -self.speed  # 97      A
            self.change_y = 0  # 100     D
            self.direction = "L"  # 119     W
        elif key == 100:  # 115     S
            self.change_x = self.speed
            self.change_y = 0
            self.direction = "R"
        elif key == 119:
            self.change_y = -self.speed
            self.change_x = 0
            self.direction = "U"
        elif key == 115:
            self.change_y = self.speed
            self.change_x = 0
            self.direction = "D"
        elif key == 32:
            self.interact_button_hit = True
            self.check_npc_surrounding()
        if key == 0:
            self.change_x = 0
            self.change_y = 0

    def check_npc_surrounding(self):
        for Interactable in self.level.NPC_list:
            #print(Interactable.actualDirection, " - ", self.direction)
            # If the player is in a vicinity of 70 pixels from the NPC
            if all((Interactable.rect.x >= self.rect.x - 70, Interactable.rect.x <= self.rect.x + 70,
                    Interactable.rect.y >= self.rect.y - 70, Interactable.rect.y <= self.rect.y + 70)):
            # Make the NPC face the player
                if self.direction == "D": Interactable.directionAnimate = "U"
                elif self.direction == "L": Interactable.directionAnimate = "R"
                elif self.direction == "R": Interactable.directionAnimate = "L"
                elif self.direction == "U": Interactable.directionAnimate = "D"
                Interactable.change_x = 0
                Interactable.change_y = 0
                Interactable.talk("oldman1_talk")
