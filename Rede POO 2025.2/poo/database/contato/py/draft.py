class Fone:
    def __init__(self, id:str, number:str):
        self.__id = id
        self.__number = number

    def isValid(self):
        permitidos = "0123456789()."
        return all(c in permitidos for c in self.__number)
    
    def getId(self):
        return self.__id
    
    def getNumber(self):
        return self.__number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name:str):
        self.__favorited = False
        self.__List = []
        self.__name = name

    def __str__(self):
        flag = "@" if self.__favorited else "-"
        return f"{flag} {self.__name} ["+ ", ".join(str(c) for c in self.__List) +"]"   

    def addFone(self, id:str, number:str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__List.append(fone)
            return
        print("fail: invalid number")

    def rmFone(self, index: int):
        try:
            self.__List.pop(index)
        except:
            print("fail, indice invalido")

    def tfav(self):
        self.__favorited = False if self.__favorited else True

def main():
    contact = Contact("")

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            contact = Contact(args[1])
        elif args[0] == "add":
            contact.addFone(args[1], args[2])
        elif args[0] == "rm":
            contact.rmFone(int(args[1]))
        elif args[0] == "show":
            print(contact)
        elif args[0] == "tfav":
            contact.tfav()
        else:
            print("comando invalido")
    
main()
