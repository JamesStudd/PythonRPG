import pygame as pg
import os
from Data.spritesheet_functions import SpriteSheet

pg.init()


def init():
    global screen, DIRECT_DICT, SCREEN_RECT
    DIRECT_DICT = {97 : (-1, 0),
                100 : (1, 0),
                119 : (0, -1),
                115 : (0, 1),
                276 : (-1, 0),
                275 : (1, 0),
                274 : (0, 1),
                273 : (0, -1)}

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    SIZE = [800, 800]
    screen = pg.display.set_mode(SIZE)

    SCREEN_RECT = screen.get_rect()


def sort_player_spritesheet(animation, name):
    if name == "male":
        sprite_sheet = SpriteSheet('Resources\\main_character.png')
    elif name == "female":
        sprite_sheet = SpriteSheet('Resources\\main_character_female.png')

    array = []
    walky = 0;
    sizey = 51;
    if animation == "up":
        walky = 511
    elif animation == "left":
        walky = 574
    elif animation == "down":
        walky = 635
        sizey = 54
    elif animation == "right":
        walky = 702

    walkanimation = [0, 64, 128, 192, 256, 320, 384, 448, 512]

    for x in range(0, 9):
        image = sprite_sheet.get_image(walkanimation[x], walky, 30, sizey)
        array.append(image)
    return array


def sort_npc_spritesheet(animation, sheet):
    sprite_sheet = SpriteSheet('Resources\\' + sheet)
    array = []
    walky = 0;
    sizey = 51;
    if animation == "up":
        walky = 511
    elif animation == "left":
        walky = 574
    elif animation == "down":
        walky = 635
        sizey = 54
    elif animation == "right":
        walky = 702

    walkanimation = [0, 64, 128, 192, 256, 320, 384, 448, 512]

    for x in range(0, 9):
        image = sprite_sheet.get_image(walkanimation[x], walky, 30, sizey)
        array.append(image)
    return array

def return_talk_font():
    font_talk = pg.font.SysFont("monospace", 20)
    return font_talk

def load_all_graphics(dirname):
    image_dict = {}
    for filename in os.listdir(dirname):
        name,ext = os.path.splitext(filename)
        if ext.lower() in [".png",".jpg",".bmp"]:
            pathname = os.path.join(dirname, filename)
            image = pg.image.load(pathname).convert_alpha()
            image.set_colorkey(pg.Color("black"))
            image_dict[name] = image
    return image_dict
init()
global IMAGES
IMAGES = load_all_graphics("..\\PythonRpg\\Resources\\")
