class Leitor:
    def __init__(self, nome: str, magia: int):
        self.__nome = nome
        self.__magia = magia

    def get_nome(self):
        return self.__nome

    def get_magia(self):
        return self.__magia

    def ganhar_magia(self, qtd: int):
        self.__magia += qtd

    def gastar_magia(self, qtd: int):
        self.__magia -= qtd

    def __str__(self):
        return f"{self.__nome} ({self.__magia} magia)"

class LivroMagico:
    def __init__(self, energia: int):
        self.__energia = energia
        self.__leitor = None
        self.__capitulos_lidos = 0

    def entrar(self, leitor: Leitor):
        if self.__leitor is not None:
            print("fail: livro ja esta sendo lido")
            return False
        
        if leitor.get_magia() < 5:
            print("fail: magia insuficiente para ler")
            return False

        leitor.gastar_magia(5)
        self.__leitor = leitor
        self.__capitulos_lidos = 0
        return True

    def ler_capitulo(self):
        if self.__leitor is None:
            print("fail: ninguem esta lendo o livro")
            return False
        
        if self.__energia <= 0:
            print("fail: o livro esta sem energia")
            self.sair()
            return False

        self.__energia -= 2
        self.__leitor.ganhar_magia(1)
        self.__capitulos_lidos += 1

        if self.__energia <= 0:
            print("fail: o livro ficou sem energia e se fechou sozinho")
            self.sair()

        return True

    def sair(self):
        if self.__leitor is None:
            print("fail: ninguem esta lendo o livro")
            return None
        
        leitor = self.__leitor
        self.__leitor = None
        print(f"{leitor.get_nome()} terminou de ler. Capitulos lidos: {self.__capitulos_lidos}")
        return leitor

    def __str__(self):
        nome = self.__leitor.get_nome() if self.__leitor else "ninguem"
        return f"LivroMagico energia:{self.__energia}, lendo:{nome}"

