class Person:
    def __init__(self, nome):
        self.__nome = nome
    
    def __str__(self):
        return self.__nome

class Market:
    def __init__(self, qtd):
        self.__qtd = qtd
        self.__counters = [None] * qtd
        self.__waiting = []

    def is_valid(self, n):
        return 0 <= n< self.__qtd

    def arrive(self, pessoa):
        self.__waiting.append(pessoa)

    def call(self, index):
        if not self.__waiting:
            print("fail: sem clientes")
            return

        if self.__counters[index] is not None:
            print("fail: caixa ocupado")
            return

        self.__counters[index] = self.__waiting.pop(0)

    def finish(self, index):
        if not self.is_valid(index):
            print("fail: caixa inexistente")
            return

        if self.__counters[index] is None:
            print("fail: caixa vazio")
            return

        self.__counters[index] = None

    def __str__(self):
        sb = "Caixas: ["
        for i, p in enumerate(self.__counters):
            sb += "-----" if p is None else str(p)
            if i < len(self.__counters) - 1:
                sb += ", "
        sb += "]\n"

        sb += "Espera: ["
        for i, p in enumerate(self.__waiting):
            sb += str(p)
            if i < len(self.__waiting) - 1:
                sb += ", "
        sb += "]"

        return sb

def main():
    market = None
    while True:
        line = input()
        print(f"${line}")
        
        par = line.split(" ")
        cmd = par[0]

        if cmd == "end":
            break
        elif cmd == "init":
            qtd_caixas = int(par[1])
            market = Market(qtd_caixas)
        elif cmd == "show":
            print(market)
        elif cmd == "arrive":
            nome = par[1]
            pessoa = Person(nome)
            market.arrive(pessoa)
        elif cmd == "call":
            indice = int(par[1])
            market.call(indice)
        elif cmd == "finish":
            indice = int(par[1])
            market.finish(indice)
        else:
            print("fail: comando invalido")


main()
