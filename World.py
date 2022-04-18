import pygame as pg
from Resize import Rescale as rs


class World:
    def __init__(self):
        self.background = pg.image.load("img/background.png")
        self.background = pg.transform.scale(self.background, (rs.mapCoords(self.background.get_width()), rs.mapCoords(self.background.get_height())))

    def draw(self, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.background, (0, 0))

        return SCREEN
