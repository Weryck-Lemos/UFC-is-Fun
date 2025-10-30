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

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria = None
        self.__carregador = None

    def ligar(self):
        if self.__ligado:
            print("fail: ja esta ligado")
            return
        if not self.__bateria and not self.__carregador:
            print("não foi possível ligar")
            return
        if self.__bateria and self.__bateria.getCarga() == 0 and not self.__carregador:
            print("não foi possível ligar")
            return
        self.__ligado = True
        print("notebook ligado")

    def desligar(self):
        if not self.__ligado:
            print("fail: ja esta desligado")
            return
        self.__ligado = False
        print("notebook desligado")

    def usar(self, time: int):
        if not self.__ligado:
            print("notebook desligado")
            return
        if self.__bateria and not self.__carregador:
            carga = self.__bateria.getCarga()
            if time < carga:
                print(f"Usando por {time} minutos")
                self.__bateria.setCarga(carga - time)
            else:
                print(f"Usando por {carga} minutos, notebook descarregou")
                self.__bateria.setCarga(0)
                self.__ligado = False
        elif self.__bateria and self.__carregador:
            ganho = self.__carregador.getPotencia() * time
            self.__bateria.alterarCarga(ganho)
            print("Notebook utilizado com sucesso")
        elif not self.__bateria and self.__carregador:
            print("Notebook utilizado com sucesso")
        else:
            print("fail: sem energia")
            self.__ligado = False

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        bateria = self.__bateria.mostrar() if self.__bateria else print(f"Status: {status}, Bateria: Nenhuma, Carregador: {(self.__carregador.mostrar() if self.__carregador else 'Desconectado')}")
        if self.__bateria:
            b = f"({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})"
            if self.__carregador:
                print(f"Status: {status}, Bateria: {b}, Carregador: (Potência {self.__carregador.getPotencia()})")
            else:
                print(f"Status: {status}, Bateria: {b}, Carregador: Desconectado")

    def setBateria(self, bateria: Bateria):
        if self.__bateria is not None:
            print("fail: ja tem bateria")
            return
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria is None:
            print("fail: nao tem bateria para remover")
            return
        bateria = self.__bateria
        self.__bateria = None
        print("bateria removida")
        return bateria

    def setCarregador(self, carregador: Carregador):
        if self.__carregador is not None:
            print("fail: ja tem carregador")
            return
        self.__carregador = carregador

    def rmCarregador(self):
        if self.__carregador is None:
            print("fail: nao tem carregador para remover")
            return
        carregador = self.__carregador
        self.__carregador = None
        print("carregador removido")
        return carregador


def main():
    
    notebook = Notebook() # criando notebook
    notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado
    notebook.ligar()      # msg: não foi possível ligar
    notebook.usar(10)     # msg: notebook desligado

    bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
    bateria.mostrar()     # (50/50)
    notebook.setBateria(bateria) # coloca a bateria no notebook

    notebook.mostrar() # msg: Status: Desligado, Bateria: (50/50), Carregador: Desconectado
    notebook.ligar()   # msg: notebook ligado
    notebook.mostrar() # msg: Status: Ligado, Bateria: (50/50), Carregador: Desconectado
    notebook.usar(30)  # msb: Usando por 30 minutos
    notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: Desconectado
    notebook.usar(30)  # msb: Usando por 20 minutos, notebook descarregou
    notebook.mostrar() # msg: Status: Desligado, Bateria: (0/50), Carregador: Desconectado

    bateria = notebook.rmBateria() # msg: bateria removida
    bateria.mostrar()  # (0/50)
    notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado

    carregador = Carregador(2) # criando carregador com 2 de potencia
    carregador.mostrar() # (Potência 2)

    notebook.setCarregador(carregador) # adicionando carregador no notebook
    notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: (Potência 2)
    notebook.ligar()   # msg: notebook ligado
    notebook.mostrar() # msg: Status: Ligado, Bateria: Nenhuma, Carregador: (Potência 2)

    notebook.setBateria(bateria)
    notebook.mostrar() # msg: Status: Ligado, Bateria: (0/50), Carregador: (Potência 2)
    notebook.usar(10)  # msg: Notebook utilizado com sucesso
    notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: (Potência 2)


main()
