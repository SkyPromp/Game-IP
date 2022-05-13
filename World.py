import pygame as pg
from Resize import Rescale as rs
from Room0 import Room0
from Settings import Settings


class World:
    def __init__(self, room_amount: int):
        self.backgrounds = [pg.image.load(f"img/rooms/background{i}.png") for i in range(room_amount)]
        self.background_collisions = [
            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170), "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)},
            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170), "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)},
            {"x0": rs.mapCoords(9), "xm": rs.mapCoords(310), "y0": rs.mapCoords(9), "ym": rs.mapCoords(170), "door_y0": rs.mapCoords(55), "door_ym": rs.mapCoords(70)},
        ]
        self.background = self.backgrounds[0]
        self.background = pg.transform.scale(self.background, (rs.mapCoords(self.background.get_width()), rs.mapCoords(self.background.get_height())))
        self.roomid = 0
        self.rooms = [Room0(), Room0(), Room0()]  # add different room objects here

    def draw(self, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.background, (0, 0))
        SCREEN = self.rooms[self.roomid].drawAll(SCREEN)

        return SCREEN

    def nextRoom(self):
        self.roomid += 1
        self.background = self.backgrounds[self.roomid]
        self.background = pg.transform.scale(self.background, (rs.mapCoords(self.background.get_width()), rs.mapCoords(self.background.get_height())))
        try:
            pg.mixer.init()
            door_sound = pg.mixer.Sound("sounds/deurgeluid.wav")
            door_sound.set_volume(Settings.getSoundVolume())
            pg.mixer.Channel(1).play(door_sound)
        except FileNotFoundError:
            pass

    def getCollisions(self):
        return self.background_collisions[self.roomid]

    def getRoom(self):
        return self.rooms[self.roomid]