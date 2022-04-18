import pygame as pg
from Movement import Movement
from Character import Character
from World import World
from Resize import Rescale as rs



def main():
    pg.init()
    rs.setFactor(720/180)
    SCREEN = pg.display.set_mode((rs.mapCoords(320), rs.mapCoords(180)))  # Keep aspect ratio 16:9
    CLOCK = pg.time.Clock()
    move = Movement()
    character = Character()
    world = World()
    running = True
    coords = (rs.mapCoords(100), rs.mapCoords(100))

    while running:
        SCREEN = world.draw(SCREEN)
        coords = move.move(SCREEN.get_size(), coords, 1, (64, 64))
        SCREEN = character.draw(coords, SCREEN)
        pg.display.update()
        CLOCK.tick(30)


if __name__ == '__main__':
    main()

