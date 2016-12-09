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

    direction = "R"

    level = None
    name = None
    inside = False

    def __init__(self, gender):
        super().__init__()

        self.gender = gender
        
        if self.gender == "male":
            sprite_sheet = SpriteSheet('Resources\\male.png')
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
            
        elif self.gender == "female":
            sprite_sheet = SpriteSheet('Resources\\dark.png')
            image = sprite_sheet.get_image(97, 193, 31, 48)
            self.walking_frames_d.append(image)
            image = sprite_sheet.get_image(129, 193, 31, 48)
            self.walking_frames_d.append(image)
            image = sprite_sheet.get_image(161, 193, 31, 48)
            self.walking_frames_d.append(image)
            image = sprite_sheet.get_image(129, 193, 31, 48)
            self.walking_frames_d.append(image)

            image = sprite_sheet.get_image(99, 241, 31, 48)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(131, 241, 31, 48)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(163, 241, 31, 48)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(131, 241, 31, 48)
            self.walking_frames_l.append(image)

            image = sprite_sheet.get_image(96, 289, 31, 48)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(128, 289, 31, 48)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(160, 289, 31, 48)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(128, 289, 31, 48)
            self.walking_frames_r.append(image)

            image = sprite_sheet.get_image(97, 336, 31, 48)
            self.walking_frames_u.append(image)
            image = sprite_sheet.get_image(129, 336, 31, 48)
            self.walking_frames_u.append(image)
            image = sprite_sheet.get_image(162, 336, 31, 48)
            self.walking_frames_u.append(image)
            image = sprite_sheet.get_image(129, 336, 31, 48)
            self.walking_frames_u.append(image)
            
        elif self.gender == "bill":
            sprite_sheet = SpriteSheet('Resources\\bill.png')
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

    def update(self):

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        posx = self.rect.x + self.level.world_shift_x
        posy = self.rect.y + self.level.world_shift_y
        
        if self.direction == "R":
            frame = (posx // 20) % len(self.walking_frames_r)
            self.image= self.walking_frames_r[frame]
        if self.direction == "L":
            frame = (posx // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.direction == "U":
            frame = (posy // 20) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        if self.direction == "D":
            frame = (posy // 20) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]


        if self.rect.right > SCREEN_RECT.right:
            self.rect.x -= 5
            self.change_x = 0
            self.change_y = 0

        if self.rect.left < SCREEN_RECT.left:
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

        if key == 97:
            self.change_x = -self.speed
            self.change_y = 0
            self.direction = "L"
        elif key == 100:
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
        if key == 0:
            self.change_x = 0
            self.change_y = 0
 
global invisblocks
invisblocks = pg.sprite.Group()

class Invis(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = IMAGES[image]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

class Block(pg.sprite.Sprite):
    
    def __init__(self, tmx, x, y, rectx, recty, layer):
        super().__init__()
        self.tmx = tmx
        self.x = x
        self.y = y
        self.layer = layer
        self.image = tmx.get_tile_image(self.x,self.y,self.layer)
        self.image.set_colorkey((255,0,255))
        
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty
        
        collide = tmx.get_tile_properties(self.x, self.y, self.layer)
        #for image in IMAGES:
        #   print(image)

        #for key in collide:
        #    print(key)
        # single tile properties IE Grass
        # collide['Collision'] ==
        # 1 - Top of block
        # 2 - Bottom of block
        # 3 - Left of block
        # 4 - Right of block
        # 5 - Full block

        #SPECIFIC
        # 6 - Roof TOP
        if collide != None:
            if 'Collision' in collide:
                if collide['Collision'] == '1':
                    collision = Invis(self.rect.x, self.rect.y, 'collisionupDEBUG')
                    invisblocks.add(collision)
                if collide['Collision'] == '2':
                    collision = Invis(self.rect.x, self.rect.y + 40, 'collisionupDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '3':
                    collision = Invis(self.rect.x, self.rect.y, 'collisionleftDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '4':
                    collision = Invis(self.rect.x + 40, self.rect.y, 'collisionleftDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '5':
                    collision = Invis(self.rect.x, self.rect.y, 'collisionboxDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '6':
                    collision = Invis(self.rect.x, self.rect.y + 40, 'collisionupDEBUG')
                    invisblocks.add(collision)
                    collision = Invis(self.rect.x, self.rect.y + 30, 'collisionupDEBUG')
                    invisblocks.add(collision)

class GoInside(pg.sprite.Sprite):

    movement = {}

    def __init__(self, tmx, x, y, rectx, recty, layer):
        super().__init__()
        self.tmx = tmx
        self.x = x
        self.y = y
        self.layer = layer
        self.image = tmx.get_tile_image(self.x,self.y,self.layer)
        self.image.set_colorkey((255,0,255))
        
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty


class NPC(pg.sprite.Sprite):

    level = None
    walking_frames_l= []
    walking_frames_u = []
    walking_frames_d = []
    walking_frames_r = []
    
    direction = {"R":[1,0], "U":[0,-1], "D":[0,1], "L":[-1,0], "S":[0,0]}
    
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

    change_x = 0
    change_y = 0
    
    directionAnimate = "R"
    
    controller = 0
    animater = 0

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
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_r[0]
            else:
                self.image = self.walking_frames_r[self.animater]
                
        if self.directionAnimate == "L":
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_l[0]
            else:
                self.image = self.walking_frames_l[self.animater]
                
        if self.directionAnimate == "U":
            if self.change_x == 0 and self.change_y == 0:
                self.image = self.walking_frames_u[0]
            else:
                self.image = self.walking_frames_u[self.animater]
                
        if self.directionAnimate == "D":
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

class CivRoom():

    background = None
    NPC_list = None

    room_shift_x = 0
    room_shift_y = 0

    world_shift_x = 0
    world_shift_y = 0


    def __init__(self, player, x, y):

        self.NPC_list = pg.sprite.Group()
        self.player = player
        player.rect.x = x
        player.rect.y = y
        player.direction = "U"

    def update(self, player):

        self.NPC_list.update()


    def draw(self, screen):

        screen.fill(pg.Color('black'))
        screen.blit(self.background, (self.room_shift_x, self.room_shift_y))
        self.NPC_list.draw(screen)
                                
class Level():

    enemy_list = None
    background = None
    invis_list = None
    transition_list = None
    NPC_list = None

    world_shift_x = 0
    world_shift_y = 0
    level_limit_x = -1000
    level_limit_y = -1000
    level_limit_xleft = 1000
    level_limit_yup = 900

    stop_move_x = False
    stop_move_y = False

    check_right = False
    check_left = False
    check_top = False
    check_bottom = False

    def __init__(self, player):

        self.enemy_list = pg.sprite.Group()   # Lists of enemies
        self.invis_list = invisblocks
        self.transition_list = pg.sprite.Group()
        self.NPC_list = pg.sprite.Group()
        self.player = player


    def draw(self, screen):

        screen.blit(self.background, (self.world_shift_x, self.world_shift_y))
        self.enemy_list.draw(screen)
        self.invis_list.draw(screen)
        self.NPC_list.draw(screen)
        self.transition_list.draw(screen)

        # c
        for block in self.transition_list:
            pg.draw.rect(screen, pg.Color('black'), (block.rect.x, block.rect.y, 50, 50), 0)

    def shift_world(self, shift_x, shift_y):

        self.world_shift_x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        for invis in self.invis_list:
            invis.rect.x += shift_x
        for NPC in self.NPC_list:
            NPC.rect.x += shift_x
        for trans in self.transition_list:
            trans.rect.x += shift_x

        self.world_shift_y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y
        for invis in self.invis_list:
            invis.rect.y += shift_y
        for NPC in self.NPC_list:
            NPC.rect.y += shift_y
        for trans in self.transition_list:
            trans.rect.x += shift_x

    def update(self, player):


        if self.stop_move_x == False:
            if player.rect.right >= 375:
                diff = player.rect.right - 375
                player.rect.right = 375
                self.shift_world(-diff, 0)

            if player.rect.left <= 375:
                diff = 375 - player.rect.left
                player.rect.left = 375
                self.shift_world(diff, 0)

        if self.stop_move_y == False:
            if player.rect.top >= 375:
                diff = 375 - player.rect.top
                player.rect.top = 375
                self.shift_world(0, diff)

            if player.rect.bottom <= 473:
                diff = 473 - player.rect.bottom
                player.rect.bottom = 473
                self.shift_world(0, diff)

        current_position_x = player.rect.x + self.world_shift_x
        current_position_y = player.rect.y + self.world_shift_y

        if current_position_x < self.level_limit_x:
            self.stop_move_x = True
            self.check_right = True

        if player.rect.right < SCREEN_RECT.centerx and self.check_right == True:
            self.stop_move_x = False
            self.check_right = False
        # --------------------------------------------------------------------

        if current_position_x > self.level_limit_xleft:
            self.stop_move_x = True
            self.check_left = True

        if player.rect.right > SCREEN_RECT.centerx and self.check_left == True and player.direction == "R":
            self.stop_move_x = False
            self.check_left = False
        # --------------------------------------------------------------------

        if current_position_y < self.level_limit_y:
            self.stop_move_y = True
            self.check_top = True

        if (player.rect.bottom - 75) < SCREEN_RECT.centery and self.check_top == True and player.direction == "U":
            self.stop_move_y = False
            self.check_top = False
        # --------------------------------------------------------------------

        if current_position_y > self.level_limit_yup and player.direction == "U":
            self.stop_move_y = True
            self.check_bottom = True

        if (player.rect.top - 20) > SCREEN_RECT.centery and self.check_bottom == True and player.direction == "D":
            self.stop_move_y = False
            self.check_bottom = False

        invisblock_hit_list = pg.sprite.spritecollide(player, invisblocks, False)

        for block in invisblock_hit_list:
            if player.change_x < 0:
                player.move(0)
                player.rect.left = block.rect.right
            elif player.change_x > 0:
                player.move(0)
                player.rect.right = block.rect.left
            elif player.change_y < 0:
                player.move(0)
                player.rect.top = block.rect.bottom
            elif player.change_y > 0:
                player.move(0)
                player.rect.bottom = block.rect.top

        #for block in self.transition_list:
            #print(block.rect.x, block.rect.y, current_position_x, current_position_y)

        transitioner = pg.sprite.spritecollide(player, self.transition_list, False)

        #for block in transitioner:
            #print("askdasd")


class InsideLevel_01(CivRoom):

    def __init__(self, player):

        CivRoom.__init__(self, player, 385, 545)

        self.room_shift_x = 150
        self.room_shift_y = 200
        self.background = IMAGES['insidehouse1']

        
class Level_01(Level):

    def __init__(self, player):

        Level.__init__(self, player)
        self.level_limit_x = -2000
        self.level_limit_y = -1900
        self.level_limit_xleft = 320
        self.level_limit_yup = 368
        self.background = IMAGES['overworld_main']

        self.invis_list.empty()
        invisblocks.empty()

        gameMap = load_pygame("Resources\\Overworld_main.tmx")
        self.blocksprites = pg.sprite.Group()
        self.fgblocksprites = pg.sprite.Group()

        for y in range(64):
            for x in range(64):
                test = gameMap.get_tile_image(x,y,1)
                testprop = gameMap.get_tile_properties(x,y,0)
                if testprop != None:
                    if 'Collision' in testprop:
                        block = Block(gameMap,x,y,x*50,y*50,0)
                        self.blocksprites.add(block)
                        
                if test != None:
                    block = Block(gameMap,x,y,x*50,y*50,1)
                    self.fgblocksprites.add(block)

                testprop = gameMap.get_tile_properties(x,y,2)
                if testprop != None:
                    if 'Transition' in testprop:
                        inside = GoInside(gameMap,x,y,x*50,y*50,2)
                        self.transition_list.add(inside)
                        #print(self.transition_list)



        oldman1 = Interactable('oldman1', 2000, 2000, 'civi1.png', 100, 1)
        oldman1.level = self
        self.NPC_list.add(oldman1)


class Level_02(Level):

    def __init__(self, player):

        Level.__init__(self, player)
        self.background = IMAGES['insidehouse1']

        self.invis_list.empty()
        invisblocks.empty()

        gameMap = load_pygame("Resources\\Overworld_main.tmx")
        self.blocksprites = pg.sprite.Group()
        self.fgblocksprites = pg.sprite.Group()

        for y in range(64):
            for x in range(64):
                test = gameMap.get_tile_image(x,y,1)
                testprop = gameMap.get_tile_properties(x,y,0)
                if testprop != None:
                    if 'Collision' in testprop:
                        block = Block(gameMap,x,y,x*50,y*50,0)
                        self.blocksprites.add(block)
                if test != None:
                    block = Block(gameMap,x,y,x*50,y*50,1)
                    self.fgblocksprites.add(block)

        
