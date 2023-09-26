import pygame as pg

class Bullet(pg.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.x = position[0] + 25
        self.y = position[1] + 50
        self.screen = pg.display.get_surface()
        self.position = position
        self.velocity = velocity
        self.image = pg.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        # self.rect += self.velocity
        self.rect.move_ip(self.velocity)

