import pygame as pg
from Resize import Rescale as rs


class Room0:
    DIALOG = False
    def __init__(self):
        assets = ["open_door", "counter"]
        self.asset_positions = [
            {"left": rs.mapCoords(312-41), "right": rs.mapCoords(323), "up": rs.mapCoords(55-1), "down": rs.mapCoords(96)},
            {"left": rs.mapCoords(139), "right": rs.mapCoords(182), "up": rs.mapCoords(180 - 38 - 9), "down": rs.mapCoords(180 - 9)},
            {"left": rs.mapCoords(129), "right": rs.mapCoords(192), "up": rs.mapCoords(170 - 38 - 9), "down": rs.mapCoords(170 - 9)}]
        self.objects = [pg.transform.scale(pg.image.load(f"img/Room assets/{item}.png"), (rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_width()), rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_height()))) for item in assets]
        self.collided = []  # initialization

    def drawAll(self, SCREEN):
        pos = self.asset_positions[0]
        SCREEN.blit(self.objects[0], (pos["left"], pos["up"]))
        i = 0
        for object, pos in zip(self.objects[1:], self.asset_positions[1:]):
            SCREEN.blit(object, (pos["left"], pos["up"]))

            i += 1

        return SCREEN

    def hasCollisions(self, x, y, character_height, character_width):
        left, right, up, down = [0, 0, 0, 0]  # temp value

        def hasCollision():
            return down > y > up - character_height and left - character_width < x < right

        self.collided = []
        for item in self.asset_positions[1:2]:
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            self.collided.append(hasCollision())
        for item in self.asset_positions[2:]:
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            if hasCollision() and not Room0.DIALOG:
                self.setDialog()
                pg.init()
                SCREEN = pg.display.set_mode((rs.mapCoords(320), rs.mapCoords(180)))
                CLOCK = pg.time.Clock()
                try:
                    with open("Dialog.txt", "r") as f:
                        for text in f:
                            for i in range(4):
                                SCREEN.fill(0)
                                font = pg.font.Font('freesansbold.ttf', 32).render(text[0:-1], True, (255, 255, 255))
                                textrect = font.get_rect()
                                textrect.topleft = (rs.mapCoords(10), rs.mapCoords(10))
                                SCREEN.blit(font, textrect)
                                pg.display.update()
                                CLOCK.tick(1)

                except FileNotFoundError:
                    pass

                print("bonk")

        # print(any(self.collided))
        return any(self.collided)

    @classmethod
    def setDialog(cls):
        cls.DIALOG = True
