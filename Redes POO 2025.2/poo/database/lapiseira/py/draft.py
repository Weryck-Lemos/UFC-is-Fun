class Lead:
    def __init__(self, thickness:float, hardness:str, size:int):
        self.__thickness : float = thickness
        self.__hardness : str = hardness
        self.__size : int = size

    def usagePerSheet(self):
        if self.__hardness == "HB": return 1
        if self.__hardness == "2B": return 2
        if self.__hardness == "4B": return 4
        return 6
    
    def set_size(self, size):
        self.__size = size

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
    def get_thickness(self):
        return self.__thickness
    
    def get_hardeness(self):
        return self.__hardness
    
    def get_size(self):
        return self.__size


class Pencil:
    def __init__(self, thickness: float = 0, lead: Lead | None = None):
        self.__thickness = thickness
        self.__lead = lead
        self.__barrel = []


    def hasGrafite(self):
        return self.__lead != None
    
    def insert(self, lead: Lead):
        if(self.__thickness != lead.get_thickness()):
            print("fail: calibre incompatível")
            return
        
        if(self.hasGrafite()):
            print("fail: ja existe grafite")
            return
        
        self.__barrel.append(lead)

    def pull(self):
        if self.__lead is not None:
            print("fail: ja existe grafite no bico")
            return
        
        if len(self.__barrel) == 0:
            print("fail: nao existe grafite no tambor")
            return
        
        self.__lead = self.__barrel[0]
        self.__barrel.pop(0)


    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite no bico")
            return
        
        self.__lead = None
    
    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite no bico")
            return
        
        if self.__lead.get_size() <= 10:
            print("fail: tamanho insuficiente")
            return
        
        n = self.__lead.usagePerSheet()

        if self.__lead.get_size() - n <10:
            print("fail: folha incompleta")
            self.__lead.set_size(10)
            return
        
        self.__lead.set_size(self.__lead.get_size() - n)

    def __str__(self):
        lead = "[]" if self.__lead is None else str(self.__lead)
        ans = f"calibre: {self.__thickness}, bico: {lead}, tambor: <"
        for i , p in enumerate(self.__barrel):
            if p is not None:
                ans += str(p)
        ans += ">"
        return ans
        


def main():
    pencil = Pencil()
    while(1):
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0]=="end":
            break
        elif args[0] == "init":
            pencil = Pencil(float(args[1]))
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "insert":
            lead = Lead(float(args[1]), str(args[2]), int(args[3]))
            pencil.insert(lead)
        elif args[0] == "remove":
            pencil.remove()
        elif args[0] == "write":
            pencil.write()
        elif args[0] == "pull":
            pencil.pull()
        else:
            print("fail: comando invalido")
main()    