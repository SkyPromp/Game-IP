import pygame as pg


class Movement:
    def __init__(self):
        self.framecount = 0

    def move(self, SCREEN_SIZE, pos, speed, OBJ_SIZE):
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE
        x, y = pos
        width, height = OBJ_SIZE
        keys = pg.key.get_pressed()
        pg.event.pump()

        if keys[pg.K_LEFT] and x > 0:
            x -= speed

        if keys[pg.K_RIGHT] and x < SCREEN_WIDTH - width:
            x += speed

        if keys[pg.K_DOWN] and y < SCREEN_HEIGHT - height:
            y += speed

        if keys[pg.K_UP] and y > 0:
            y -= speed

        return x, y

