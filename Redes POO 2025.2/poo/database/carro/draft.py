class Car:
    def __init__(self):
        self.pas :int = 0
        self.km :int = 0
        self.pasMax :int = 2
        self.gas :int = 0
        self.gasMax :int = 100
    
    def __str__(self):
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def enter(self):
        if(self.pas == self.pasMax): 
            print("fail: limite de pessoas atingido")
            return

        self.pas+=1
    
    def leave(self):
        if(self.pas == 0):
            print("fail: nao ha ninguem no carro")
            return
        
        self.pas -=1

    def fuel(self, increment:int):
        self.gas = increment
        self.gas = min(self.gas, self.gasMax)

    def drive(self, distance:int):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
            return
        
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        
        if distance > self.gas:
            distance = self.gas
            print(f"fail: tanque vazio apos andar {distance} km")

        self.km += distance
        self.gas -= distance
        
def main():
    car = Car()
    while True:
        line = input()
        print(f"${line}")

        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break
        elif cmd == "enter":
            car.enter()
        elif cmd == "show":
            print(car)
        elif cmd == "leave":
            car.leave()
        elif cmd == "fuel":
            increment = int(parts[1])
            car.fuel(increment)
        elif cmd == "drive":
            distance = int(parts[1])
            car.drive(distance)
        else:
            print("fail: comando invalido")

main()