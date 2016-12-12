import pygame as pg
from Data.spritesheet_functions import SpriteSheet
from Data.images import *
from pytmx import *
from Data.interactables_npcs import *
from main import *
import random
pg.init()

global invisblocks  # This will be changed eventually to not be a global variable
invisblocks = pg.sprite.Group()

global transition_list
transition_list = pg.sprite.Group()


class Invis(pg.sprite.Sprite):
    """ Invis blocks - provide collision between player and any terrain I don't want traversable """
    def __init__(self, x, y, image):
        super().__init__()

        self.image = IMAGES[image]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Block(pg.sprite.Sprite):
    
    def __init__(self, tmx, x, y, rectx, recty, layer):
        super().__init__()
        self.tmx = tmx  # TMX is the import that allows for tile properties - collisions.
        self.x = x
        self.y = y
        self.layer = layer  # Background, House layer, House Decor, etc.
        self.image = tmx.get_tile_image(self.x,self.y,self.layer)
        self.image.set_colorkey((255,0,255))
        
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty
        
        collide = tmx.get_tile_properties(self.x, self.y, self.layer)
        # The following key is for which type of block to create. For example, a bridge is 2 blocks wide
        # and will need collision on those blocks so that the player can't 'fall' off the bridge. BUT, we can't
        # have a full 50x50 block of collision as then the player can't walk onto the bridge, so a  "collisionleft"
        # is created on the left blocks, and a "collisonright" on the right block,
        # which allows for the player to walk onto the bridge, and not fall off the left or right side.

        # collide['Collision'] ==
        # 1 - Top of block
        # 2 - Bottom of block
        # 3 - Left of block
        # 4 - Right of block
        # 5 - Full block

        # SPECIFIC
        # 6 - Roof TOP
        # 7 - Left and bottom of block
        # 8 - Right and bottom of block

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
                    collision = Invis(self.rect.x + 40, self.rect.y, 'collisionleftDEBUG')  # DEBUG is so the collision
                    invisblocks.add(collision)                                              # block is visible.

                elif collide['Collision'] == '5':
                    collision = Invis(self.rect.x, self.rect.y, 'collisionboxDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '6':
                    collision = Invis(self.rect.x, self.rect.y + 40, 'collisionupDEBUG')
                    invisblocks.add(collision)
                    collision = Invis(self.rect.x, self.rect.y + 30, 'collisionupDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '7':
                    collision = Invis(self.rect.x, self.rect.y, 'collisionleftDEBUG')
                    invisblocks.add(collision)
                    collision = Invis(self.rect.x, self.rect.y + 40, 'collisionupDEBUG')
                    invisblocks.add(collision)

                elif collide['Collision'] == '8':
                    collision = Invis(self.rect.x + 40, self.rect.y, 'collisionleftDEBUG')
                    invisblocks.add(collision)
                    collision = Invis(self.rect.x, self.rect.y + 40, 'collisionupDEBUG')
                    invisblocks.add(collision)

            if 'Transition' in collide:
                if collide['Transition'] == '1':
                    collision = TransitionBlock(self.rect.x, self.rect.y)
                    transition_list.add(collision)


class TransitionBlock(pg.sprite.Sprite):
    """ Transition blocks are the blocks that teleport the player to inside a house """

    def __init__(self, x, y):
        super().__init__()
        self.image = IMAGES['collisionboxDEBUG']
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class CivRoom:
    """ Currently unused """
    background = IMAGES['insidehouse1']
    NPC_list = None
    invis_list = None
    transition_list = None
    shiftdone = False

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
        self.invis_list = invisblocks
        self.transition_list = transition_list

    def update(self, player):

        self.NPC_list.update()
        if self.shiftdone == False:
            for invis in self.invis_list:
                invis.rect.x += self.room_shift_x
                invis.rect.y += self.room_shift_y
            for trans in self.transition_list:
                trans.rect.x += self.room_shift_x
                trans.rect.y += self.room_shift_y
            self.shiftdone = True

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

        transition_hit_list = pg.sprite.spritecollide(player, transition_list, False)
        for block in transition_hit_list:
            player.transitionhit = True

    def draw(self, screen):

        screen.fill(pg.Color('black'))
        screen.blit(self.background, (self.room_shift_x, self.room_shift_y))
        self.NPC_list.draw(screen)
        self.invis_list.draw(screen)
        self.transition_list.draw(screen)


class InsideLevel_01(CivRoom):

    def __init__(self, player):

        CivRoom.__init__(self, player, 460, 400)

        self.room_shift_x = 150
        self.room_shift_y = 200
        self.background = IMAGES['insidehouse1']

        self.invis_list.empty()
        invisblocks.empty()
        self.transition_list.empty()
        transition_list.empty()

        gameMap = load_pygame("Resources\\insidehouse1.tmx")
        self.blocksprites = pg.sprite.Group()
        self.fgblocksprites = pg.sprite.Group()

        for y in range(8):
            for x in range(10):
                testprop = gameMap.get_tile_properties(x, y, 0)
                if testprop != None:
                    if 'Collision' in testprop:
                        block = Block(gameMap, x, y, x * 50, y * 50, 0)
                        self.blocksprites.add(block)



class Level:
    """ Super Class for a level """
    enemy_list = None
    background = None  # Map basically
    invis_list = None  # Collidable blocks
    transition_list = None  #
    NPC_list = None

    world_shift_x = 0  # How far has the map moved
    world_shift_y = 0  # ""
    level_limit_x = -1000  # Limits of map movement X left
    level_limit_y = -1000  # Limits of map movement Y up
    level_limit_xleft = 1000  # Limits of map movement X right
    level_limit_yup = 900 # Limits of map movement Y down

    stop_move_x = False  # If the player moves all the way left or right, the map will stop shifting
    stop_move_y = False  # If the player moves all the way up or down, the map will stop shifting

    check_right = False
    check_left = False
    check_top = False
    check_bottom = False

    def __init__(self, player):

        self.enemy_list = pg.sprite.Group()  # Lists of enemies
        self.invis_list = invisblocks  # Lists of obstacles
        self.transition_list = transition_list
        self.NPC_list = pg.sprite.Group()
        self.player = player

    def draw(self, screen):

        screen.blit(self.background, (self.world_shift_x, self.world_shift_y))
        self.enemy_list.draw(screen)
        self.invis_list.draw(screen)
        self.NPC_list.draw(screen)
        self.transition_list.draw(screen)

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
            trans.rect.y += shift_y

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

        transition_hit_list = pg.sprite.spritecollide(player, transition_list, False)
        for block in transition_hit_list:
            player.transitionhit = True


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
        transition_list.empty()

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
                        inside = Block(gameMap,x,y,x*50,y*50,2)
                        transition_list.add(inside)

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

