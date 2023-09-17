import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.image = pg.image.load('assets/graphics/player/idle/down/tile000.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (170, 170))
        self.rect = self.image.get_rect(center=position)

        self.directions = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}

        self.direction = pg.math.Vector2()
        self.speed = 10

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def handle_player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.direction = pg.math.Vector2(self.directions['up'])
            self.run(self.direction)
        elif keys[pg.K_s]:
            self.direction = pg.math.Vector2(self.directions['down'])
            self.run(self.direction)
        elif keys[pg.K_d]:
            self.direction = pg.math.Vector2(self.directions['right'])
            self.run(self.direction)
        elif keys[pg.K_a]:
            self.direction = pg.math.Vector2(self.directions['left'])
            self.run(self.direction)

    def run(self, direction):
        if direction.magnitude() != 0:
            direction = direction.normalize()
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed




