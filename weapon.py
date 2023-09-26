import pygame as pg

class Weapon(pg.sprite.Sprite):
    def __init__(self, pos, images, player, weapon_group):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.weapon_group = weapon_group
        self.images = images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.image = pg.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.image)
        self.add(weapon_group)
        status = player.status

        if status == 'left':
            self.index = 2
            self.image = self.images[self.index]
            self.rect.right = player.rect.left - 6
            self.rect.y = player.rect.centery + 5
        elif status == 'right':
            self.index = 3
            self.image = self.images[self.index]
            self.rect.left = player.rect.right - 5
            self.rect.y = player.rect.y + 40
        elif status == 'up':
            self.index = 4
            self.image = self.images[self.index]
            self.rect.bottom = player.rect.top + 8
            self.rect.x = player.rect.x
        elif status == 'down':
            self.index = 0
            self.image = self.images[self.index]
            self.rect.top = player.rect.bottom - 15
            self.rect.x = player.rect.x + 3
