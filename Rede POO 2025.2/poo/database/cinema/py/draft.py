class Client:
    def __init__(self, id:str , phone:int):
        self.__id = id
        self.__phone = phone

    def getPhone(self) ->int:
       return self.__phone
        
    def getId(self) -> str:
        return self.__id
    
    def setPhone(self, phone:int) -> None:
        self.__phone = phone

    def setId(self, id:str) -> None:
        self.__id = id

    def __str__(self) -> str:
        return f"{self.__id}:{self.__phone}"

        
class Theater:
    def __init__(self, capacity:int = 0):
        self.__seats = [None]*capacity
        self.__search = [None]*capacity
        self.__verifyIndex = capacity

    def __str__(self):
        print("[", end="")
        ans = " ".join('-' if seat is None else str(seat) for seat in self.__seats)  
        ans +="]"
        return ans
        
    def reserve(self, id:str, phone:int, index: int) ->bool:
        if index <0 or index >= self.__verifyIndex:
            print("fail: cadeira nao existe")
            return False

        elif self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False

        elif id in self.__search:
            print("fail: cliente ja esta no cinema")
            return False

        client = Client(id, phone)
        self.__seats[index] = client
        self.__search.append(client.getId())
        return True

    def cancel(self, id: str):
        if id not in self.__search:
            print("fail: cliente nao esta no cinema")
            return
        
        self.__search.remove(id)
        for  i, client in enumerate(self.__seats):
            if client.getId() == id:
                self.__seats[i] = None
                return


    


def main():
    theater = Theater()

    while True:
        line = input()
        print(f"${line}")

        args = line.split()

        if args[0] ==  "end":
            break
        elif args[0] == "init":
            theater = Theater(int(args[1]))
        elif args[0] == "show":
            print(theater)
        elif args[0] == "reserve":
            theater.reserve(args[1], int(args[2]), int(args[3]))
        elif args[0] == "cancel":
            theater.cancel(args[1])
        else:
            print("fail: comando invalido")
main()