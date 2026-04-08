class Pet:
    def __init__(self, energyMax:int, cleanMax:int):
        self.__energy = energyMax
        self.__energyMax = energyMax
        self.__clean = cleanMax
        self.__cleanMax = cleanMax
        self.__age = 0
        self.__alive = True

    def setEnergy(self, n:int):
        self.__energy += n
        self.__energy = min(self.__energyMax, self.__energy)
        self.__energy = max(self.__energy,0)

    def setClean(self, n:int):
        self.__clean += n
        self.__clean = min(self.__cleanMax, self.__clean)
        self.__clean = max(0, self.__clean)

    def setAge(self, n:int):
        self.__age +=n 

    def setAlive(self):
        self.__alive = False

    def isAlive(self):
        return self.__alive

    def getClean(self):
        return self.__clean
    
    def getCleanMax(self):
        return self.__cleanMax
    
    def getEnergy(self):
        return self.__energy
    
    def getEnergyMax(self):
        return self.__energyMax
    
    def getAge(self):
        return self.__age
    
    def __str__(self):
        return f"E:{self.__energy}/{self.__energyMax}, L:{self.__clean}/{self.__cleanMax}, I:{self.__age}"
    
class Game:
    def __init__(self, arg1:int=0, arg2:int=0):
        self.__pet = Pet(arg1, arg2)

    def verificar(self):
        if not self.__pet.isAlive():
            print("fail: pet esta morto")
            return True

        if self.__pet.getEnergy() == 0:
            print("fail: pet morreu de fraqueza")
            self.__pet.setAlive()
            return False
        
        if self.__pet.getClean() == 0:
            print("fail: pet morreu de sujeira")
            self.__pet.setAlive()
            return False

    def play(self):
        if self.verificar(): return

        self.__pet.setEnergy(-2)
        self.__pet.setClean(-3)
        self.__pet.setAge(1)
        self.verificar()

    def sleep(self):
        if self.verificar(): return

        if self.__pet.getEnergy() >= self.__pet.getEnergyMax()-5:
            print("fail: nao esta com sono")
            return
        
        turnos = self.__pet.getEnergyMax() - self.__pet.getEnergy() 
        self.__pet.setEnergy(turnos)
        self.__pet.setAge(turnos)

    def shower(self):
        self.verificar()

        self.__pet.setEnergy(-3)
        self.__pet.setClean(self.__pet.getCleanMax())
        self.__pet.setAge(2)

    def __str__(self):
        return f"{self.__pet}"

def main():
    tamagochi = Game()

    while True:
        line = input()
        print(f"${line}")

        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(tamagochi)
        elif args[0] == "init":
            tamagochi= Game(int(args[1]), int(args[2]))
        elif args[0] == "shower":
            tamagochi.shower()
        elif args[0] == "play":
            tamagochi.play()
        elif args[0] == "sleep":
            tamagochi.sleep()
        else:
            print("comando inválido")
        
main()