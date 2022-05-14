import pygame as pg
from Character import Character
from World import World
from Resize import Rescale as rs
from Settings import Settings
import json


def settingsHandler():
    global ROOM_AMOUNT
    with open('Settings.json') as json_file:
        data = json.load(json_file)
        rs.setFactor(data['Display_size'][1]/180)
        ROOM_AMOUNT = data['Room_amount']
        Settings.setGeneralVolume(data['General_volume'])
        Settings.setMusicVolume(data['Music_volume'])
        Settings.setSoundVolume(data['Sounds_volume'])


def main():
    pg.init()
    settingsHandler()
    SCREEN = pg.display.set_mode((rs.mapCoords(320), rs.mapCoords(180)))  # Keep aspect ratio 16:9
    CLOCK = pg.time.Clock()
    character = Character()
    world = World(ROOM_AMOUNT)
    running = True
    coords = (rs.mapCoords(100), rs.mapCoords(100))
    music = ""
    try:
        pg.mixer.init()
        music = pg.mixer.Sound("sounds/achtergrondgeluid.wav")
        pg.mixer.Channel(0).play(music, loops=-1)
    except FileNotFoundError:
        pass

    while running:
        music.set_volume(Settings.getMusicVolume())
        SCREEN = world.draw(SCREEN)
        try:
            coords = character.move(coords, 10, (character.standwidth, character.standheight), world, world.rooms[world.roomid])
        except IndexError:
            running = False
        character.checkFrameUpdate()
        character.calculateFrame()
        SCREEN = character.draw(coords, SCREEN)
        pg.display.update()
        CLOCK.tick(30)


if __name__ == '__main__':
    # Settings constants
    ROOM_AMOUNT = 0
    main()

