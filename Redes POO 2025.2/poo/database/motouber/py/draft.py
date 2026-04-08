class Pessoa():
    def __init__(self, nome:str, dinheiro:int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"
    
    def get_nome(self):
        return self.__nome
    
    def get_dinheiro(self):
        return self.__dinheiro
    
    def set_dinheiro(self, valor:int):
        self.__dinheiro = valor

class Moto():
    def __init__(self,):
        self.__custo = 0
        self.__motorista = None
        self.__passageiro = None
    
    def __str__(self):

        if self.__motorista != None:
            motorista = self.__motorista
        else:
            motorista = "None"
        
        if self.__passageiro != None:
            passageiro = self.__passageiro
        else:
            passageiro = "None"

        return f"Cost: {self.__custo}, Driver: {motorista}, Passenger: {passageiro}"
    
    def setDrive(self, nome:str, dinheiro:int):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome:str, dinheiro:int):
        if self.__motorista == None:
            print("fail: sem motorista")
            return
        
        self.__passageiro = Pessoa(nome, dinheiro)
        
    def leavePass(self):
        if self.__passageiro == None:
            print(f"fail: sem passageiro")
            return
        
        if self.__passageiro.get_dinheiro()> self.__custo:
            print(f"{self.__passageiro.get_nome()}:{self.__custo} left")
            
        else:
            print("fail: Passenger does not have enough money")
            print(f"{self.__passageiro.get_nome()}:0 left")

        self.__motorista.set_dinheiro(self.__motorista.get_dinheiro() + self.__custo)
        self.__custo = 0        
        self.__passageiro = None

    def drive(self, distancia:int):
        self.__custo += distancia

def main():
    moto = Moto()
    while 1:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            moto.setDrive(args[1], int(args[2]))
        elif args[0] == "setPass":
            moto.setPass(args[1], int(args[2]))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "leavePass":
            moto.leavePass()
        else:
            print("comando inválido")



main()