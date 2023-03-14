import sys

from map import *
from player import *
from settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('My RayCasting')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.player.update()

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.map.draw()
        self.player.draw()
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = Game()
    app.run()
