import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, position, surface, groups):
        super().__init__(groups)
        self.x = position[0]
        self.y = position[1]
        self.screen = pg.display.get_surface()
        self.image = surface
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pg.mask.from_surface(self.image)

    # def draw(self):
    #     self.screen.blit(self.image, self.rect)


