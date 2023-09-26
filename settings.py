import pygame as pg
import os

FPS = 60
WIDTH = 960
HEIGHT = 640
PLAYER_INITIAL_POSITION = pg.math.Vector2(WIDTH // 2, HEIGHT // 2)
MAP_DIR = f'assets/map/my_example_map/'
PLAYER_INITIAL_POSITION = pg.math.Vector2(WIDTH // 2, HEIGHT // 2)
ENEMY_HEALTH = 100
lance_weapon = {
    'side': ['down', 'full', 'left', 'right', 'up']
}

def load_image(path):
    images = []
    for image_name in os.listdir(path):
        image = pg.image.load(path + os.sep + image_name).convert_alpha()
        images.append(image)
    return images


WIDTH = 900
HEIGHT = 600
PLAYER_INITIAL_POSITION = pg.math.Vector2(WIDTH // 2, HEIGHT // 2)
