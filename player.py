from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, position, create_weapon, destroy_weapon, obstacle_group):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.image = pg.image.load('assets/graphics/player/idle/down/tile000_changed.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (58, 70))
        self.rect = self.image.get_rect(center=position)
        self.mask = pg.mask.from_surface(self.image)
        self.status = 'down'

        self.obstacle_group = obstacle_group

        self.directions = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
        self.direction = pg.math.Vector2()
        self.speed = 10

        self.create_weapon = create_weapon
        self.destroy_weapon = destroy_weapon
        self.attacking = False
        self.attack_time = pg.time.get_ticks()
        self.attack_cooldown = 200

        self.player_damage = 1
        self.lance_damage = 2


    def draw(self):
        self.screen.blit(self.image, self.rect)
        # pg.draw.rect(self.screen, (0, 0, 255), self.rect, 1)
        # pg.draw.line(self.screen, (255, 0, 0), self.rect.topright, self.rect.topleft)

    def handle_player_input(self):
        if not self.attacking:
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
        if not self.attacking:
            if keys[pg.K_e]:
                self.attacking = True
                self.attack_time = pg.time.get_ticks()
                self.create_weapon()


    def set_status(self):
        if self.direction == pg.math.Vector2(self.directions['up']):
            self.status = 'up'
        elif self.direction == pg.math.Vector2(self.directions['down']):
            self.status = 'down'
        elif self.direction == pg.math.Vector2(self.directions['right']):
            self.status = 'right'
        elif self.direction == pg.math.Vector2(self.directions['left']):
            self.status = 'left'

    def run(self, direction):
        if direction.magnitude() != 0:
            direction = direction.normalize()
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

    def set_attack_cooldown(self):
        current_time = pg.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_weapon()

    def set_damage(self):
        whole_damage = self.player_damage + self.lance_damage
        return whole_damage

    def update(self):
        self.set_status()
        self.set_attack_cooldown()

    def set_collision(self, sprite):
        if self.direction == pg.math.Vector2(self.directions['up']):
            self.rect.top = sprite.rect.bottom
        elif self.direction == pg.math.Vector2(self.directions['down']):
            self.rect.bottom = sprite.rect.top
        elif self.direction == pg.math.Vector2(self.directions['left']):
            self.rect.left = sprite.rect.right
        elif self.direction == pg.math.Vector2(self.directions['right']):
            self.rect.right = sprite.rect.left
