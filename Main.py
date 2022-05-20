import pygame as pg
from Character import Character
from World import World
from Resize import Rescale as rs
from Settings import Settings
from Room3 import Room3
import json
import Minigame0


def settingsHandler():
    with open('Settings.json') as json_file:
        data = json.load(json_file)
        rs.setFactor(data['Display_size'][1]/180)
        Settings.setRoomAmount(data['Room_amount'])
        Settings.setGeneralVolume(data['General_volume'])
        Settings.setMusicVolume(data['Music_volume'])
        Settings.setMusicVolume(data['Sounds_volume'])
        Settings.setRoomAmount(data['Room_amount'])


def main():
    settingsHandler()
    try:
        Minigame0.gameloop()
        pass
    except Exception:
        pass
    try:
        pg.mixer.init()
        door_sound = pg.mixer.Sound("sounds/deurgeluid.wav")
        door_sound.set_volume(Settings.getSoundVolume())
        pg.mixer.Channel(1).play(door_sound)
    except FileNotFoundError:
        pass
    pg.init()
    SCREEN = pg.display.set_mode((rs.mapCoords(320), rs.mapCoords(180)))  # Keep aspect ratio 16:9
    CLOCK = pg.time.Clock()
    character = Character()
    world = World()
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

        # Blit character to screen from Room3
        SCREEN = Room3.blitChar(SCREEN)

        character.checkFrameUpdate()
        character.calculateFrame()
        SCREEN = character.draw(coords, SCREEN)
        pg.display.update()
        CLOCK.tick(30)


if __name__ == '__main__':
    main()
