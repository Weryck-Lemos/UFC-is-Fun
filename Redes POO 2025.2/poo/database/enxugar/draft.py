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

    def __str__(self):
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

    
def main():
    towel = None

    while True:
        line = input()
        print(f"${line}")
        part = line.split()

        cmd = part[0]
        if cmd == "end":
            break
        elif cmd == "criar":
            color = part[1]
            size = part[2]
            towel = Towel(color, size)
        elif cmd == "mostrar":
            print(towel)
        elif cmd == "enxugar":
            amout = int(part[1])
            towel.dry(amout)
        elif cmd == "torcer":
            towel.wrigOut()
        elif cmd == "seca":
            if(towel.isDry()):
                print("sim")
            else:
                print("nao")
        else:
            print("fail: comando invalido")

main()