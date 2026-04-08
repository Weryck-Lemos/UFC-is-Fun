class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")


class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCapacidade(self):
        return self.__capacidade

    def getCarga(self):
        return self.__carga

    def setCarga(self, n: int):
        if n<0:
            n =0
        if n>self.__capacidade:
            n=self.__capacidade
        self.__carga = n

    def alterarCarga(self, delta: int):
        self.setCarga(self.__carga + delta)

    def __str__(self):
        return f"{self.__carga}/{self.__capacidade}"

class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria = None
        self.__carregador = None 
        self.__uso = 0

    def ligar(self):
        if self.__ligado:
            print("fail: ja esta ligado")
            return
        if not self.__bateria and not self.__carregador:
            print("fail: não foi possível ligar")
            return
        if self.__bateria and self.__bateria.getCarga() == 0 and not self.__carregador:
            print("fail: não foi possível ligar")
            return
        self.__ligado = True

    def desligar(self):
        if not self.__ligado:
            print("fail: ja esta desligado")
            return
        self.__ligado = False

    def usar(self, time: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        if self.__bateria and not self.__carregador:
            carga = self.__bateria.getCarga()
            if time < carga:
                self.__bateria.setCarga(carga - time)
                self.__uso += time
            else:
                print("fail: descarregou")
                self.__uso += carga
                self.__bateria.setCarga(0)
                self.__ligado = False
        elif self.__bateria and self.__carregador:
            ganho = self.__carregador.getPotencia() * time
            self.__bateria.alterarCarga(ganho)
            self.__uso += time
        elif not self.__bateria and self.__carregador:
            self.__uso += time
        else:
            print("fail: sem energia")
            self.__ligado = False

    def setBateria(self, bateria: Bateria):
        if self.__bateria is not None:
            print("fail: bateria já conectada")
            return
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        bateria = self.__bateria
        self.__bateria = None
        print(f"Removido {bateria}")
        if self.__carregador is None: self.__ligado = False
        return bateria

    def setCarregador(self, carregador: Carregador):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return
        self.__carregador = carregador

    def rmCarregador(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        carregador = self.__carregador
        print(f"Removido {self.__carregador.getPotencia()}W")
        self.__carregador = None
        if  self.__bateria is not None and self.__bateria.getCarga() == 0 : self.__ligado = False
        if self.__bateria is None: self.__ligado = False
        return carregador
    
    def __str__(self):

        ans = ""
        if self.__ligado:
            ans += f"Notebook: ligado por {self.__uso} min"
        else:
            ans += "Notebook: desligado"

        if self.__carregador is not None:
            ans +=  f", Carregador {self.__carregador.getPotencia()}W"

        if self.__bateria is not None:
            ans += f", Bateria {self.__bateria.getCarga()}/{self.__bateria.getCapacidade()}"
        
        return ans

def main():
    notebook = Notebook()
    while True:
        line = input()
        print(f"${line}")

        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(notebook)
        elif args[0] == "use":
            notebook.usar(int(args[1]))
        elif args[0] == "turn_off":
            notebook.desligar()
        elif args[0] == "turn_on":
            notebook.ligar()
        elif args[0] == "rm_charger":
            notebook.rmCarregador()
        elif args[0] == "set_battery":
            notebook.setBateria(Bateria(int(args[1])))
        elif args[0] == "set_charger":
            notebook.setCarregador(Carregador(int(args[1])))
        elif args[0] == "rm_battery":
            notebook.rmBateria()
        else:
            print("comando inválido")
main()