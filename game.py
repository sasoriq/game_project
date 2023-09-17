import sys
from settings import *
from player import *


class Game:
    def __init__(self):
        self.initialize_game()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.player = Player(PLAYER_INITIAL_POSITION)

    def initialize_game(self):
        pg.init()

    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def handle_input(self):
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            self.player.handle_player_input()


    def process_game_logic(self):
        print(self.player.rect.x)
        print(self.player.rect.y)

    def draw(self):
        self.screen.fill((209, 187, 186))
        self.player.draw()
        pg.display.flip()



if __name__ == '__main__':
    game = Game()
    game.main_loop()

