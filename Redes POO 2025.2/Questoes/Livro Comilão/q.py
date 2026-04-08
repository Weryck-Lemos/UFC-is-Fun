class Leitor:
    def __init__(self, nome: str, magia: int = 0):
        self.nome = nome
        self.magia = magia
    
    def get_nome(self):
        return self.nome
    
    def get_magia(self):
        return self.magia
    
    def ganhar_magia(self, qtd: int):
        self.magia += qtd

class LivroMagico:
    def __init__(self, energia: int):
        self.energia = energia
        self.leitor = None
        self.capitulos_lidos = 0
    
    def entrar(self, leitor: Leitor):
        if self.leitor:
            return "fail: livro já está sendo lido"
        self.leitor = leitor
        return True
    
    def sair(self):
        return "fail: impossível parar de ler"
    
    def ler_capitulos(self, numero: int):
        if not self.leitor:
            return "fail: ninguém está lendo o livro"
        
        for i in range(numero):
            if self.energia > 1:
                self.energia -= 2
                self.leitor.ganhar_magia(5)
                self.capitulos_lidos += 1
            else:
                print(f"Leitor {self.leitor.get_nome()} foi engolido pelo livro")
                self.leitor = None
                self.capitulos_lidos = 0
                break
    
    def __str__(self):
        nome_leitor = self.leitor.get_nome() if self.leitor else "ninguém"
        magia_leitor = self.leitor.get_magia() if self.leitor else 0
        return f"Magia do Livro: {self.energia}, Lendo: {nome_leitor}, Magia do Leitor: {magia_leitor}, Capitulos Lidos: {self.capitulos_lidos}"