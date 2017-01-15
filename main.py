import pygame as pg
import os
from Data.level_classes import *
from Data.images import *
from Data.player_related import *
from Data.interactables_npcs import *
from Data.menu import Menu, char_create
from Data.intro import Dialogue, show_intro
from Data.pause_menu import draw_pause_menu
from Data.timed_messages import timed_message
from Data.HUD import hud
from Data.minimap import draw_minimap


def main():
    pg.init()
    pg.display.set_caption("RPG")
    clock = pg.time.Clock()
    #show_intro()

    player = char_create()
    playerhud = hud(player)

    active_sprite_list = pg.sprite.Group()
    active_sprite_list.add(player)

    player.level = Level_01(player)
    player.inside = False
    paused = False
    paused_font = pg.font.SysFont("monospace", 30)
    display_font = pg.font.SysFont("monospace", 20)
    display_fps = display_coords = False
    list_of_timed_messages = []


    # This bit will eventually use threads, one for updating and one for rendering
    while True:
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if(event.key == pg.K_ESCAPE):
                    paused = not paused
                if not paused:
                    player.move(event.key)
                if(event.key == pg.K_F1):  # This will be cleaned up eventually
                    display_fps = True
                    display_coords = True
            elif event.type == pg.KEYUP:
                if not paused:
                    player.move(0)

        if not paused:
            #print(player.rect.x - player.level.world_shift_x, player.rect.y - player.level.world_shift_y)
            active_sprite_list.update()
            player.level.update(player)
            for NPC in player.level.NPC_list:
                NPC.update(player)
            if player.transitionhit == True:
                if player.inside:
                    player.rect.x = player.level.exit_coord_x
                    player.rect.y = player.level.exit_coord_y
                    player.level = Level_01(player)
                    player.inside = False
                else:
                    print("Player transition to go to: ", player.transitiontogoto)
                    if player.transitiontogoto == 1:
                        player.level = InsideLevel_01(player)
                    if player.transitiontogoto == 3:
                        player.level = InsideLevel_03(player)
                    if player.transitiontogoto == 5:
                        player.level = InsideLevel_05(player)
                    if player.transitiontogoto == 7:
                        player.level = InsideLevel_07(player)
                    if player.transitiontogoto == 9:
                        player.level = InsideLevel_09(player)
                    if player.transitiontogoto == 11:
                        player.level = InsideLevel_11(player)
                    player.inside = True
                player.transitionhit = False


        #print(player.rect.x - player.level.world_shift_x, player.rect.y - player.level.world_shift_y)

        # --- DRAW
        player.level.draw(screen)
        active_sprite_list.draw(screen)
        for NPC in player.level.NPC_list:
            if NPC.talk_approved:
                #tm = timed_message(screen, NPC.talk_line, NPC.rect.x + 30, NPC.rect.y + 30, 90)
                #list_of_timed_messages.append(tm)
                NPC.display_message(screen)
                # This just needs to be timed now (only on the screen for 5 seconds or so)

        for t in list_of_timed_messages:
            t.draw()
            
        if paused:
            draw_pause_menu(screen)

        if display_fps == True:  # This will be cleaned up eventually
            text = display_font.render("FPS: "+(str(clock.get_fps())[0:2]), True, pg.Color("white"))
            screen.blit(text, (600, 210))
            text = display_font.render(str(player.rect.x - player.level.world_shift_x)+", "+str(player.rect.y - player.level.world_shift_y), True, pg.Color('white'))
            screen.blit(text, (600, 240))

        playerhud.draw(screen)
        if not player.inside:
            draw_minimap(screen, player)

        pg.display.flip()
        # --- END DRAW



        clock.tick(30)

if __name__ == "__main__":
    main()
