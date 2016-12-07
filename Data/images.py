import pygame as pg
import os

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
