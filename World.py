import pygame as pg
from Resize import Rescale as rs
from Room0 import Room0
from Room1 import Room1
from Room2 import Room2
from Room3 import Room3
from Settings import Settings


class World:
    def __init__(self):
        self.backgrounds = [pg.image.load(f"img/rooms/background{i}.png") for i in range(Settings.getRoomAmount())]
        self.background_collisions = [
            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170),
             "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)},

            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170),
             "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)},

            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170),
             "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)},

            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170),
             "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)}
        ]
        self.background = self.backgrounds[0]
        self.background = pg.transform.scale(self.background, (
        rs.mapCoords(self.background.get_width()), rs.mapCoords(self.background.get_height())))
        self.roomid = 0
        self.rooms = [Room0(), Room1(), Room2(), Room3()]

    def draw(self, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.background, (0, 0))
        SCREEN = self.rooms[self.roomid].drawAll(SCREEN)

        return SCREEN

    def nextRoom(self):
        self.roomid += 1
        self.background = self.backgrounds[self.roomid]
        self.background = pg.transform.scale(self.background, (
        rs.mapCoords(self.background.get_width()), rs.mapCoords(self.background.get_height())))

    def getCollisions(self):
        return self.background_collisions[self.roomid]

    def getRoom(self):
        return self.rooms[self.roomid]
