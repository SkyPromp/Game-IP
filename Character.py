import pygame as pg
from Resize import Rescale as rs
from World import World
from Settings import Settings
import sys



class Character:
    def __init__(self):
        path = 'img/Main Character/Stand.png'
        self.imgFrames = []
        self.stand = pg.image.load(path)
        self.standwidth, self.standheight = (rs.mapCoords(self.stand.get_width())//2, rs.mapCoords(self.stand.get_height())//2)
        self.stand = pg.transform.scale(self.stand, (self.standwidth, self.standheight))
        self.imgFrames.append(self.stand)
        paths = [f'img/Main Character/Walkframe{i}.png' for i in range(2)]
        self.imgFrames = [pg.transform.scale(pg.image.load(i), (
        rs.mapCoords(pg.image.load(i).get_width()) // 2, rs.mapCoords(pg.image.load(i).get_height()) // 2)) for i in
                          paths]
        self.movement_framecount = {"left": 0, "right": 0, "down": 0, "up": 0}
        self.looking_direction_function = self.drawRight
        self.frame = 0
        self.frames = 0

    def draw(self, *args):
        return self.looking_direction_function(*args)

    def drawNeutral(self, coords: tuple, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.stand, coords)
        return SCREEN

    def drawRight(self, coords: tuple, SCREEN: pg.Surface) -> pg.Surface:
        SCREEN.blit(self.imgFrames[self.frame], coords)

        return SCREEN

    def drawLeft(self, coords: tuple, SCREEN: pg.Surface) -> pg.Surface:
        image = self.imgFrames[self.frame]
        flip = pg.transform.flip(image, True, False)
        SCREEN.blit(flip, coords)
        return SCREEN

    def nextImg(self):
        self.frame = (self.frame + 1) % len(self.imgFrames)

    def defaultImg(self):
        self.frame = 0
        print(self.frame)

    def calculateFrame(self):
        self.frames = max(
            [self.movement_framecount["left"], self.movement_framecount["right"], self.movement_framecount["down"],
             self.movement_framecount["up"]])

    def checkFrameUpdate(self):
        if self.frames > 15:
            self.movement_framecount = {"left": 0, "right": 0, "down": 0, "up": 0}
            self.nextImg()
        # elif self.frames ==0:
        #     self.defaultImg()

    def move(self, pos, speed: int, OBJ_SIZE, worldobj, room):
        x, y = pos
        width, height = OBJ_SIZE
        keys = pg.key.get_pressed()
        self.eventHandler()
        collisions = World(1).getCollisions()
        isMoving = False

        if keys[pg.K_LEFT] and x > collisions["x0"]  and not room.hasCollisions(x - speed, y, self.standheight, self.standwidth):
            x -= speed
            self.movement_framecount["left"] += 1
            self.looking_direction_function = self.drawLeft
            isMoving = True

        else:
            self.movement_framecount["left"] = 0

        if keys[pg.K_RIGHT] and ((x < collisions["xm"] - width) or (collisions["door_y0"] < y < collisions["door_ym"])) and not room.hasCollisions(x + speed, y, self.standheight, self.standwidth):
            x += speed
            self.movement_framecount["right"] += 1
            self.looking_direction_function = self.drawRight
            isMoving = not isMoving

        else:
            self.movement_framecount["right"] = 0

        if keys[pg.K_DOWN] and y < collisions["ym"] - height and not room.hasCollisions(x, y + speed, self.standheight, self.standwidth):
            y += speed
            self.movement_framecount["down"] += 1

        else:
            self.movement_framecount["down"] = 0

        if keys[pg.K_UP] and y > collisions["y0"]  and not room.hasCollisions(x, y - speed, self.standheight, self.standwidth):
            y -= speed
            self.movement_framecount["up"] += 1

        else:
            self.movement_framecount["up"] = 0

        if x > collisions["xm"]:
            worldobj.nextRoom()
            x = 100  # x of exit door
            # y of exit door

        if isMoving:
            self.looking_direction_function = self.drawNeutral

        return x, y

    @staticmethod
    def eventHandler():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_j:
                    volume = round(Settings.getGeneralVolume() - 0.1, 1)
                    Settings.setGeneralVolume(volume)
                if event.key == pg.K_k:
                    volume = round(Settings.getGeneralVolume() + 0.1, 1)
                    Settings.setGeneralVolume(volume)

