import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, position, surface, groups):
        super().__init__(groups)
        self.screen = pg.display.get_surface()
        self.image = surface
        self.rect = self.image.get_rect(topleft=position)

    # def draw(self):
    #     self.screen.blit(self.image, self.rect)


