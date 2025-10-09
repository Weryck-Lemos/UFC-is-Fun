class Calculator:
    def __init__(self, batteryMax:int):
        self.batteryMax:int = batteryMax
        self.battery:int = 0
        self.display:float = 0

    def __str__(self)->str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def recarregar(self, increment:int ):
        self.battery+=increment
        self.battery = min(self.battery, self.batteryMax)
    
    def soma(self, a: int, b:int):
        if self.battery==0:
            print("fail: bateria insuficiente")
            return 
        self.display= a+b
        self.battery-=1
        self.battery = max(self.battery, 0)

    def dividir(self, num:float, den:float):
        if self.battery==0:
           print("fail: bateria insuficiente")
           return 
       
        self.battery-=1
        if den==0:
            print("fail: divisao por zero")
            return
        self.display= num/den 

    
def main():
    calculator : Calculator = Calculator(0)
    while True:
        line = input()
        args = line.split() 
        print(f"${line}")
        if args[0]=="end":
            break
        elif args[0]=="init":
            increment:int = int(args[1])
            calculator=Calculator(increment)
        elif args[0]=="show":
            print(calculator)
        elif args[0]=="charge":
            calculator.recarregar(int(args[1]))
        elif args[0]=="sum":
            calculator.soma(int(args[1]), int(args[2]))
        elif args[0]=="div":
            calculator.dividir(float(args[1]), float(args[2]))
        else:
            print("fail: comando invalido")

main()