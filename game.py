import sys
from settings import *
import os.path as op
from player import *
import pytmx
from tile import *


class Game:
    def __init__(self):
        self.initialize_game()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        map_filename = 'my_room'
        self.tmx_data = pytmx.load_pygame(op.join(MAP_DIR, map_filename + '.tmx'))
        self.visible_group = pg.sprite.Group()
        self.obstacle_group = pg.sprite.Group()
        self.player = Player(PLAYER_INITIAL_POSITION, self.obstacle_group)

        for layer in self.tmx_data.visible_layers:
            for x, y, gid in layer:
                tile = self.tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    if layer.name == 'black':
                        self.black_tile = Tile((x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight), tile, self.obstacle_group)
                    else:
                        self.tile = Tile((x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight), tile, self.visible_group)



    def initialize_game(self):
        pg.init()

    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.obstacle_group.draw(self.screen)
            self.player.set_collision()
            self.draw()
            self.clock.tick(FPS)

    def handle_input(self):
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            self.player.handle_player_input()


    def process_game_logic(self):
        pass

    def draw(self):
        self.screen.fill((209, 187, 186))
        self.obstacle_group.draw(self.screen)
        self.visible_group.draw(self.screen)
        self.player.draw()
        pg.display.flip()



if __name__ == '__main__':
    game = Game()
    game.main_loop()

