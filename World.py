import pygame as pg


class World:
    def __init__(self):
        self.background = pg.image.load("img/background.png")

    def draw(self, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.background, (0, 0))

        return SCREEN
