class Towel:
    def __init__(self, color: str, size : str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness(self):
        if(self.size == 'P'):return 10
        elif(self.size == 'M'): return 20
        else: return 30

    def isDry(self):
        return self.wetness == 0

    def dry(self, amout : int):
        self.wetness += amout
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wrigOut(self):
        self.wetness = 0

    
