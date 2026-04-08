class Player:
    def __init__(self, label:int = 0):
        self.__label = label
        self.__pos = 0
        self.__free = True

    def isFree(self):
        return self.__free
    
    def getLabel(self):
        return self.__label
    
    def getPos(self):
        return self.__pos
    
    def setPos(self, pos: int):
        self.__pos = pos

    def setFree(self, free:bool):
        self.__free = free
