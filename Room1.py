import pygame as pg
from Resize import Rescale as rs


class Room1:
    def __init__(self):
        assets = ["Deur", "deurtoe", "sleutel"]
        self.asset_positions = [
            {"left": rs.mapCoords(120), "right": rs.mapCoords(200), "up": rs.mapCoords(60), "down": rs.mapCoords(100)}]
        self.objects = [pg.image.load(f"img/Room assets/{item}.png") for item in assets]
        self.collided = []  # initialization

    def drawAll(self, SCREEN):
        for object, pos in zip(self.objects, self.asset_positions):
            pg.draw.rect(SCREEN, 0,
                         pg.Rect(pos["left"], pos["up"], pos["right"] - pos["left"], pos["down"] - pos["up"]))  #

            # SCREEN.blit(object, leftup)

        return SCREEN

    def hasCollisions(self, x, y, character_height, character_width):
        left, right, up, down = [0, 0, 0, 0]  # temp value

        def hasCollision():
            # print(down,">", y,">", up, "and", left,"<", x,"<", right)
            return down > y > up - character_height and left - character_width < x < right

        self.collided = []
        for item in self.asset_positions:
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            self.collided.append(hasCollision())
        # print(any(self.collided))
        return any(self.collided)