import sys
import os.path as op
import pytmx
from tile import *
from weapon import *
from enemy import *
from ui import *
from player import *


class Game:
    def __init__(self):
        self.initialize_game()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        map_filename = 'my_room'
        self.tmx_data = pytmx.load_pygame(op.join(MAP_DIR, map_filename + '.tmx'))
        self.visible_group = pg.sprite.Group()
        self.obstacle_group = pg.sprite.Group()
        self.weapon_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.weapon = None
        self.player = Player(PLAYER_INITIAL_POSITION, self.create_weapon, self.destroy_weapon, self.obstacle_group)

        self.bullets = []

        self.enemy_position = (PLAYER_INITIAL_POSITION[0] - 200, PLAYER_INITIAL_POSITION[1] + 100)
        self.enemy = Enemy(self.enemy_position, True, self.bullets.append, [self.enemy_group])

        self.player_health_bar = playerUI((20, 20), 200, 20, 100, 100)
        self.enemy_self_bar = UI((self.enemy.rect.x - 200 - self.enemy.image.get_width() + 12,
                                 self.enemy.rect.y - self.enemy.image.get_height()),
                                 100,
                                 15,
                                 ENEMY_HEALTH,
                                 100)

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
            self.draw()
            self.clock.tick(FPS)

    def handle_input(self):
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            self.player.handle_player_input()
            for sprite in self.obstacle_group:
                if pg.sprite.collide_mask(self.player, sprite):
                    self.player.set_collision(sprite)
            enemy_hits = pg.sprite.groupcollide(self.weapon_group, self.enemy_group, False, False, pg.sprite.collide_mask)
            if enemy_hits:
                self.enemy.visible = False
                for sprite in self.enemy_group:
                    damage = self.player.set_damage()
                    if not sprite.vulnerability:
                        sprite.vulnerability = True
                        sprite.get_damage(damage)
                        sprite.damage_time = pg.time.get_ticks()
                        print(sprite.health)
                    print(self.bullets)

    def create_weapon(self):
        path = 'assets/graphics/weapons/lance/'
        self.weapon = Weapon((900, 100), load_image(path), self.player, self.weapon_group)

    def destroy_weapon(self):
        if self.weapon:
            self.weapon.kill()
        self.weapon = None

    def draw(self):
        self.screen.fill((209, 187, 186))
        self.obstacle_group.draw(self.screen)
        self.visible_group.draw(self.screen)
        self.weapon_group.draw(self.screen)

        for sprite in self.enemy_group:
            sprite.draw()
            sprite.update(self.player)

        self.enemy.update(self.player)

        for bullet in self.bullets[:]:
            bullet.draw()
            bullet.move()
            if pg.sprite.spritecollide(bullet, self.obstacle_group, False):
                self.bullets.remove(bullet)

        self.player.draw()
        self.player.update()

        self.player_health_bar.draw(100)

        self.enemy_self_bar.draw(self.enemy.health, self.enemy, self.enemy.rect.x, self.enemy.rect.y)
        self.enemy_self_bar.update()

        pg.display.flip()
        self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.main_loop()

