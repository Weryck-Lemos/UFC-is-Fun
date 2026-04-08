class Kid:
    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name
    
    def setAge(self, age: int):
        self.__age = age

    def setName(self, name: str):
        self.__name = name

    def __str__(self):
        return f"{self.__name}:{self.__age}"
    

class Trampoline:
    def __init__(self):
        self.__playing = []
        self.__waiting = []

    def arrive(self, name: str, age:int):
        kid = Kid(name, age)
        self.__waiting.insert(0, kid)

    def enter(self):
        if not self.__waiting:
            raise Exception ("fail: fila vazia")
        self.__playing.insert(0,self.__waiting[len(self.__waiting)-1])
        self.__waiting.pop(len(self.__waiting)-1)

    def remove(self, name:str):
        for i, kid in enumerate(self.__playing):
            if kid.getName() == name:
                self.__playing.pop(i)
                return
        for i, kid in enumerate(self.__waiting):
            if kid.getName() == name:
                self.__waiting.pop(i)
                return
            
        print(f"fail: {name} nao esta no pula-pula")
    
    def leave(self):
        if not self.__playing:
            return
        self.__waiting.insert(0, self.__playing[len(self.__playing)-1])
        self.__playing.pop(len(self.__playing)-1)

    def __str__(self):
        playing_str = ", ".join(str(k) for k in self.__playing)
        waiting_str = ", ".join(str(k) for k in self.__waiting)
        return f"[{waiting_str}] => [{playing_str}]"
    
def main():
    trampoline = Trampoline()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(trampoline)
        elif args[0] == "arrive":
            trampoline.arrive(args[1], int(args[2]))
        elif args[0] == "enter":
            trampoline.enter()
        elif args[0] == "leave":
            trampoline.leave()
        elif args[0] == "remove":
            trampoline.remove(args[1])
        else:
            print("fail: comando invalido")
main()    