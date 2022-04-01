import pygame as pg


class Character:
    def __init__(self):
        paths = [f'img/character{i}.png' for i in range(3)]
        self.imgFrames = []
        for path in paths:
            self.imgFrames.append(pg.image.load(path))

        self.frame = 0

    def draw(self, coords: tuple, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.imgFrames[self.frame], coords)

        return SCREEN

    def nextImg(self):
        self.frame = (self.frame + 1) % len(self.imgFrames)

    def defaultImg(self):
        self.frame = 0
