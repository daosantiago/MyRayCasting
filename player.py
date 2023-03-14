import math

import pygame as pg

from settings import *


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE


def move(self):
    pass


def update(self):
    pass


@property
def pos(self):
    return self.x, self.y


@property
def map_pos(self):
    return int(self.x), int(self.y)
