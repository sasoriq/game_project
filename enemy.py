import pygame as pg
from settings import *
import math
from bullet import *

class Enemy(pg.sprite.Sprite):
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 5
    def __init__(self, pos, visible, create_bullet_callback, groups):
        self.create_bullet_callback = create_bullet_callback
        super().__init__(groups)
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.screen = pg.display.get_surface()
        path = 'assets/graphics/enemy/'
        self.images = load_image(path)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.image)
        self.image_cp = self.image.copy()

        self.visible = visible
        self.blink_timer = 0
        self.blink_duration = 500

        self.health = 100
        self.speed = 2
        self.add(groups)

        self.vulnerability = False
        self.damage_time = pg.time.get_ticks()
        self.damage_cooldown = 1000
        self.last_hit_time = pg.time.get_ticks()

        self.attacking = False
        self.attack_time = pg.time.get_ticks()
        self.attack_cooldown = 2000

    def draw(self):
        if self.visible:
            self.screen.blit(self.image, self.rect)

    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage


    def set_damage_cooldown(self):
        current_time = pg.time.get_ticks()
        if self.vulnerability:
            if current_time - self.last_hit_time >= self.damage_cooldown:
                self.vulnerability = False

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def get_direction_distance(self, player):
        distance_vector = pg.math.Vector2(player.rect.x - self.rect.x,
                                   player.rect.y - self.rect.y)
        distance = math.hypot(distance_vector[0], distance_vector[1])
        direction = distance_vector
        return distance, direction

    def move_after_player(self, distance, direction):
        if distance <= 230 and distance >= 150:
            if direction:
                direction.normalize()
                direction.scale_to_length(self.speed)
            self.rect.move_ip(direction)
            if not self.attacking:
                self.attacking = True
                self.attack_time = pg.time.get_ticks()
                self.shoot(direction)
            # print(self.shoot)

    def shoot(self, direction, distance):
        # normalization (cause of different bullet speed)
        if distance == 0.0:
            direction = (0, -1)
        else:
            direction = (direction[0] / distance, direction[1] / distance)
        bullet = Bullet(self.rect, direction)
        if not self.attacking:
            self.attacking = True
            self.attack_time = pg.time.get_ticks()
            self.create_bullet_callback(bullet)


    def update(self, player):
        self.set_damage_cooldown()
        distance = self.get_direction_distance(player)[0]
        direction = self.get_direction_distance(player)[1]
        # self.move_after_player(distance, direction)
        self.shoot(direction, distance)
        if not self.visible:
            self.blink_timer = pg.time.get_ticks()
            if self.blink_timer >= self.blink_duration:
                self.visible = True
                self.blink_timer = 0

