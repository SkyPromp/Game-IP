import pygame as pg
from Resize import Rescale as rs
from Settings import Settings


class Room2:
    def __init__(self):
        self.deuropen = False  # is voorwaarde als de deur open mag of niet
        assets = ["open_door", "closed_door", "key", ]
        self.asset_positions = [
            {"left": rs.mapCoords(0), "right": rs.mapCoords(10), "up": rs.mapCoords(0), "down": rs.mapCoords(10)},
            {"left": rs.mapCoords(310), "right": rs.mapCoords(320), "up": rs.mapCoords(55), "down": rs.mapCoords(77)},
            {"left": rs.mapCoords(72), "right": rs.mapCoords(90), "up": rs.mapCoords(23), "down": rs.mapCoords(31)}]
        self.objects = [pg.image.load(f"img/room assets/{item}.png") for item in assets]
        self.objects = [pg.transform.scale(pg.image.load(f"img/Room assets/{item}.png"), (rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_width()), rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_height()))) for item in assets]

        self.collided = []  # initialization

    def drawAll(self, SCREEN):
        if self.deuropen == True:
            SCREEN.blit(self.objects[0], (rs.mapCoords(312 - 41), rs.mapCoords(53)))  # deuropen

        else:
            SCREEN.blit(self.objects[1], (rs.mapCoords(312), rs.mapCoords(55)))  # deurtoe
            SCREEN.blit(self.objects[2], (rs.mapCoords(72), rs.mapCoords(23)))  # sleutel mag je weg doen als je geen sleutel hebt
        return SCREEN

    def hasCollisions(self, x, y, character_height, character_width):
        left, right, up, down = [0, 0, 0, 0]  # temp value

        def hasCollision():
            # print(down,">", y,">", up, "and", left,"<", x,"<", right)
            return down > y > up - character_height and left - character_width < x < right


        self.collided = []
        for item in self.asset_positions[:2]:
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            self.collided.append(hasCollision())

        self.sleutelvast = []
        left, right, up, down = [rs.mapCoords(72), rs.mapCoords(90), rs.mapCoords(23),
                                     rs.mapCoords(31)]  # hier zijn de coordinaten waar je de sleutel oppakt
        self.sleutelvast.append(hasCollision())

        if any(self.sleutelvast) == True:  # hier gewoon de voorwaarde als de deur open mag of niet
            try:
                pg.mixer.init()
                door_sound = pg.mixer.Sound("sounds/deurgeluid.wav")
                door_sound.set_volume(Settings.getSoundVolume())
                pg.mixer.Channel(1).play(door_sound)
            except FileNotFoundError:
                pass

            self.deuropen = True
            self.asset_positions = [{"left": rs.mapCoords(278), "right": rs.mapCoords(320), "up": rs.mapCoords(53),
                                     "down": rs.mapCoords(60)},
                                    {"left": rs.mapCoords(0), "right": rs.mapCoords(10), "up": rs.mapCoords(0),
                                     "down": rs.mapCoords(10)},
                                    {"left": rs.mapCoords(72), "right": rs.mapCoords(90), "up": rs.mapCoords(23),
                                     "down": rs.mapCoords(31)}]

        # print(any(self.sleutelvast))

        return any(self.collided)

