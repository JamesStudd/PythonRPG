import pygame as pg
import os
from Data.classes import *
from Data.images import *
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

    level_list = []
    level_list.append(Level_01(player))
    #inside_list = []
    #inside_list.append(InsideLevel_01(player))
    #test
    current_level_no_overworld = 0
    current_level_overworld = level_list[current_level_no_overworld]

    #current_level_no_inside = 0
    #current_level_inside = inside_list[current_level_no_inside]
    
    player.level = current_level_overworld
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
        if player.inside == False:
            current_level_overworld.update(player)
            for NPC in current_level_overworld.NPC_list:
                NPC.update(player)
        else:
            current_level_inside.update(player)
            for NPC in current_level_inside.NPC_list:
                NPC.update(player)

        # --- DRAW
        if player.inside == False:
            current_level_overworld.draw(screen)
        elif player.inside == True:
            current_level_inside.draw(screen)
        active_sprite_list.draw(screen)
        pg.display.flip()
        # --- END DRAW

        clock.tick(30)


if __name__ == "__main__":
    main()
