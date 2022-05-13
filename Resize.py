class Rescale:
    scale = 1
    
    @classmethod
    def mapCoords(cls, coord):
        return int(cls.scale * coord)

    @classmethod
    def setFactor(cls, factor):
        cls.scale = factor
