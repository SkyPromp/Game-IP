import pygame as pg
from Movement import Movement
from Character import Character
from World import World


def main():
    pg.init()
    SCREEN = pg.display.set_mode((320, 180), pg.FULLSCREEN)  # Keep aspect ratio 16:9
    move = Movement()
    character = Character()
    world = World()
    running = True

    while running:
        SCREEN = world.draw(SCREEN)
        coords = move.move()
        SCREEN = character.draw(coords, SCREEN)
        pg.display.update()


if __name__ == '__main__':
    main()

