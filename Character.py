import pygame as pg
from Resize import Rescale as rs


class Character:
    def __init__(self):
        path = 'img/Main Character/Stand.png'
        self.imgFrames = []
        stand = pg.image.load(path)
        stand = pg.transform.scale(stand, (rs.mapCoords(stand.get_width()), rs.mapCoords(stand.get_height())))
        self.imgFrames.append(stand)

        self.frame = 0

    def draw(self, coords: tuple, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.imgFrames[self.frame], coords)

        return SCREEN

    def nextImg(self):
        self.frame = (self.frame + 1) % len(self.imgFrames)

    def defaultImg(self):
        self.frame = 0
