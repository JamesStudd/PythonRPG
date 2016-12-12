import pygame as pg
import os
from Data.level_classes import *
from Data.images import *
from Data.player_related import *
from Data.interactables_npcs import *
from Data.menu import Menu, char_create
from Data.intro import Dialogue, show_intro


def main():
    pg.init()
    pg.display.set_caption("RPG")
    clock = pg.time.Clock()
    #show_intro()

    player = char_create()

    active_sprite_list = pg.sprite.Group()
    active_sprite_list.add(player)

    player.level = Level_01(player)
    player.inside = False

    # This bit will eventually use threads, one for updating and one for rendering
    while True:
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                player.move(event.key)
            elif event.type == pg.KEYUP:
                player.move(0)

        active_sprite_list.update()
        player.level.update(player)
        for NPC in player.level.NPC_list:
            NPC.update(player)

        if player.transitionhit == True:
            if player.inside:
                player.level = Level_01(player)
                player.inside = False
            else:
                if player.transitiontogoto == 1:
                    player.level = InsideLevel_01(player)
                player.inside = True
            player.transitionhit = False;



        #print(player.rect.x - player.level.world_shift_x, player.rect.y - player.level.world_shift_y)

        # --- DRAW
        player.level.draw(screen)
        active_sprite_list.draw(screen)
        pg.display.flip()
        # --- END DRAW

        clock.tick(30)

if __name__ == "__main__":
    main()
