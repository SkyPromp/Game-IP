import pygame as pg
from Resize import Rescale as rs
from random import randint as ri
import Minigame1


class Room1:
    IS_CLOSED = True
    PILLS_AMOUNT = 0
    TOTAL_PILLS = 5

    def __init__(self):
        assets = ["open_door", "closed_door", "pills", "pills", "pills", "pills", "pills"]
        self.asset_positions = [
            {"left": rs.mapCoords(312), "right": rs.mapCoords(323), "up": rs.mapCoords(55), "down": rs.mapCoords(96)},
            {"left": rs.mapCoords(158), "right": rs.mapCoords(164), "up": rs.mapCoords(102), "down": rs.mapCoords(171)}]

        for i in range(Room1.TOTAL_PILLS):
            x = ri(20, 305)
            y = ri(20, 165)
            self.asset_positions.append({"left": rs.mapCoords(x), "right": rs.mapCoords(x + 15), "up": rs.mapCoords(y), "down": rs.mapCoords(y + 16)})

        self.objects = [pg.transform.scale(pg.image.load(f"img/Room assets/{item}.png"), (rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_width()), rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_height()))) for item in assets]
        self.show_pill = [True] * 5
        self.collided = []  # initialization

    def drawAll(self, SCREEN):
        pos = self.asset_positions[0]
        SCREEN.blit(self.objects[Room1.IS_CLOSED], (pos["left"], pos["up"]))
        i = 0
        for object, pos in zip(self.objects[2:], self.asset_positions[2:]):
            if self.show_pill[i]:
                SCREEN.blit(object, (pos["left"], pos["up"]))

            i += 1

        return SCREEN

    def hasCollisions(self, x, y, character_height, character_width):
        left, right, up, down = [0, 0, 0, 0]  # temp value

        def hasCollision():
            return (down > y > up - character_height and left - character_width < x < right) and Room1.IS_CLOSED

        self.collided = []
        for item in self.asset_positions[0:2]:
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            self.collided.append(hasCollision())

        for i, item in enumerate(self.asset_positions[2:]):
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            if hasCollision() and self.show_pill[i]:
                self.show_pill[i] = False
                self.updatePillAmount()

        return any(self.collided)

    @classmethod
    def updatePillAmount(cls):
        cls.PILLS_AMOUNT += 1
        if cls.PILLS_AMOUNT == cls.TOTAL_PILLS:  # code that runs when all pills have been collected
            cls.IS_CLOSED = False
            Minigame1.gameloop()
