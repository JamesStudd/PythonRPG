import pygame as pg
from Data.images import *
pg.init()


def draw_minimap(surface, player):
    pg.draw.rect(surface, pg.Color("black"), (595, 0, 205, 205), 0)
    surface.blit(pg.transform.scale(player.level.background, (200, 200)), (600,0))

    surface.blit(IMAGES['minimap_player'], \
                 ((600 + ((player.rect.x - player.level.world_shift_x) / 16)), \
                  (((player.rect.y - player.level.world_shift_y) / 16))))
    for NPC in player.level.NPC_list:
        surface.blit(IMAGES['minimap_NPC'], \
            ((600 + ((NPC.rect.x - player.level.world_shift_x) / 16)), \
             (((NPC.rect.y - player.level.world_shift_y) / 16))))
