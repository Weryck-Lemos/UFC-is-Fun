class Camisa:
    def __init__(self):
        self.__tamanho: str =""

    def __str__(self)->str:
        return f"esse é seu tamanho: {self.__tamanho}"

    def set_tamanho(self, tam: str) :
        if tam== "PP" or tam== "P" or tam=="M" or tam=="G" or tam=="GG" or tam=="XG":
            self.__tamanho= tam
            return
        print (f" tamanho despropocional")
    
    def get_tamanho(self):
        return self.__tamanho

def main():
    camisa=Camisa()
    while True:
        n= input()
        camisa.set_tamanho(n)
        if camisa.get_tamanho() != "":
            break

    print(camisa)
    
main()