import math

import pygame as pg

from settings import *


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_s]:
            dx += -speed_sin
            dy += speed_cos
        if keys[pg.K_a]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_d]:
            dx += speed_cos
            dy += speed_sin

        self.x += dx
        self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'white',
                       (self.x * 100, self.y * 100), 15)

    def update(self):
        self.move()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
