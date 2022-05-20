import pygame as pg
from Resize import Rescale as rs
from random import randint as ri
from random import shuffle
from Settings import Settings


class Room3:
    CHAR = ""
    PROGRESS = ""
    KEY = ""
    IS_CLOSED = True

    def __init__(self):
        assets = ["open_port", "closed_port", "bush", "bush", "bush", "bush", "bush", "bush", "bush", "bush", "bush", "bush"]
        self.is_closed = True
        Room3.KEY = "Einde!"
        key_len = len(Room3.KEY)
        self.ENCRYPT_KEY = list(range(key_len))
        shuffle(self.ENCRYPT_KEY)

        self.asset_positions = [{"left": rs.mapCoords(312), "right": rs.mapCoords(323), "up": rs.mapCoords(60 + 21), "down": rs.mapCoords(100 + 21)}]
        upperx = 305//key_len
        for i in range(key_len):
            x = ri(upperx - 280//key_len, upperx)
            y = ri(20, 160)
            upperx += 280//key_len
            self.asset_positions.append({"left": rs.mapCoords(20 + x), "right": rs.mapCoords(20 + x+21//2), "up": rs.mapCoords(-29 + y),
                                 "down": rs.mapCoords(-29 + y+20//2)})

        self.objects = [pg.transform.scale(pg.image.load(f"img/Room assets/{item}.png"), (rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_width()) // 2, rs.mapCoords(pg.image.load(f"img/Room assets/{item}.png").get_height()) // 2)) for item in assets]
        self.objects[0] = pg.transform.scale(self.objects[0], (self.objects[0].get_width() * 2, self.objects[0].get_height() * 2))
        self.objects[1] = pg.transform.scale(self.objects[1], (self.objects[1].get_width() * 2, self.objects[1].get_height() * 2))

        self.collided = []  # initialization

    def drawAll(self, SCREEN):
        pos = self.asset_positions[0]
        SCREEN.blit(self.objects[Room3.IS_CLOSED], (pos["left"], pos["up"]))

        for object, pos in zip(self.objects[2:], self.asset_positions[1:]):
            SCREEN.blit(object, (pos["left"], pos["up"]))

        return SCREEN

    def hasCollisions(self, x, y, character_height, character_width):
        left, right, up, down = [0, 0, 0, 0]  # temp value
        char = ""  # initialize char

        def hasCollision():
            return (down > y > up - character_height and left - character_width < x < right) and Room3.IS_CLOSED

        self.collided = []
        for item in self.asset_positions[0:1]:
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            self.collided.append(hasCollision())

        for i, item in enumerate(self.asset_positions[1:]):
            left, right, up, down = [item["left"], item["right"], item["up"], item["down"]]
            if hasCollision():
                char = Room3.KEY[self.ENCRYPT_KEY[i]]


        if char:
            Room3.setChar(char)

        return any(self.collided)

    @classmethod
    def setChar(cls, char):
        if char != cls.CHAR:
            cls.CHAR = char
            if cls.PROGRESS + char in cls.KEY:
                if cls.PROGRESS + char == cls.KEY:
                    try:
                        pg.mixer.init()
                        door_sound = pg.mixer.Sound("sounds/deurgeluid.wav")
                        door_sound.set_volume(Settings.getSoundVolume())
                        pg.mixer.Channel(1).play(door_sound)
                    except FileNotFoundError:
                        pass
                    cls.IS_CLOSED = False
                else:
                    cls.PROGRESS += char

            else:
                cls.PROGRESS = ""


    @classmethod
    def blitChar(cls, SCREEN):
        text = pg.font.Font('freesansbold.ttf', 32).render(cls.CHAR, True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.topleft = (rs.mapCoords(10), rs.mapCoords(10))
        SCREEN.blit(text, textrect)

        return SCREEN
