import pygame as pg

class UI(pg.sprite.Sprite):
    def __init__(self, pos, w, h, cur_amount, max_amount):
        self.screen = pg.display.get_surface()
        self.x = pos[0]
        self.y = pos[1]
        self.height = h
        self.width = w
        self.current_amount = cur_amount
        self.max_amount = max_amount

    def draw(self, cur_am, enemy, x, y):
        bar_x = x - enemy.image.get_width() // 2 + 10
        bar_y = y - enemy.image.get_height() // 2 + 10
        border_width = 2
        self.current_amount = cur_am
        ratio = self.current_amount / self.max_amount
        pg.draw.rect(self.screen, 'black', (bar_x, bar_y, self.width, self.height), border_width)
        pg.draw.rect(self.screen, 'red', (bar_x + border_width,
                                          bar_y + border_width,
                                          self.width - border_width * 2, self.height - border_width * 2))
        pg.draw.rect(self.screen, 'green', (bar_x + border_width,
                                            bar_y + border_width,
                                            self.width * ratio - border_width * 2, self.height - border_width * 2))


class playerUI(UI):
    def __init__(self, pos, w, h, cur_amount, max_amount):
        super().__init__(pos, w, h, cur_amount, max_amount)

    def draw(self, cur_am):
        border_width = 2
        self.current_amount = cur_am
        ratio = self.current_amount / self.max_amount
        pg.draw.rect(self.screen, 'black', (self.x, self.y, self.width, self.height), border_width)
        pg.draw.rect(self.screen, 'red', (self.x + border_width, self.y + border_width,
                                          self.width - border_width * 2, self.height - border_width * 2))
        pg.draw.rect(self.screen, 'green', (self.x + border_width, self.y + border_width,
                                            self.width * ratio - border_width * 2,
                                            self.height - border_width * 2))