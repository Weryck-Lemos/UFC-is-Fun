class Roupa:
    def __init__(self):
        self.__size: str = ""

    def __str__(self):
        return f"size: ({self.__size})"
    
    def set_tamanho(self, size:str):
        if size in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__size = size
            return
        print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
    
def main():
    roupa = Roupa()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            roupa = Roupa(args[1])
        elif args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            roupa.set_tamanho(args[1])
        else:
            print("comando inválido")

main()