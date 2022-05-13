class Settings:
    GENERAL_VOLUME = 1.0
    MUSIC_VOLUME = 1.0
    SOUND_VOLUME = 1.0

    @classmethod
    def setGeneralVolume(cls, volume):
        cls.GENERAL_VOLUME = volume

    @classmethod
    def setMusicVolume(cls, volume):
        cls.MUSIC_VOLUME = volume

    @classmethod
    def setSoundVolume(cls, volume):
        cls.SOUND_VOLUME = volume

    @classmethod
    def getGeneralVolume(cls):
        return cls.GENERAL_VOLUME

    @classmethod
    def getMusicVolume(cls):
        return cls.MUSIC_VOLUME * cls.GENERAL_VOLUME

    @classmethod
    def getSoundVolume(cls):
        return cls.SOUND_VOLUME * cls.GENERAL_VOLUME

