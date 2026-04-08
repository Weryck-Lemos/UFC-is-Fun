class Animal:
    def __init__(self, specie:str, sound:str):
        self.specie = specie
        self.sound = sound
        self.age = 0
        

    def __str__(self)->str:
        return f"{self.specie}:{self.age}:{self.sound}"
    
    def ageBy(self, increment:int)->int:
        self.age += increment
        if(self.age >= 4): 
            print(f"warning: {self.specie} morreu")
            self.age = 4

    def makeSound(self)->str:
        if(self.age == 0): return("---")
        if(self.age ==4): return("RIP")
        else: return(self.sound)


def main():
    animal = None
        
    while True:
        line = input()
        print(f"${line}")
        
        parts = line.split()
        if not parts:
            continue
        cmd = parts[0]

        if cmd == "end":
            break
        elif cmd == "init":
            species = parts[1]
            sound = parts[2]
            animal = Animal(species, sound)
        elif cmd == "show":
            print(animal)
        elif cmd == "grow":
            increment = int(parts[1])
            animal.ageBy(increment)
        elif cmd == "noise":
            print(animal.makeSound())
        else:
            print("fail: comando invalido")

main()