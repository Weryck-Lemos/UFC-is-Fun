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
        self.__favorited =not self.__favorited

    def isFav(self):
        return self.__favorited
    
    def getFones(self):
        return self.__List
    
    def getName(self):
        return self.__name
    
    def setName(self, name:str):
        self.__name = name

class Agenda:
    def __init__(self):
        self.__contatos = []

    def findPosByName(self, name:str):
        for i, c in enumerate(self.__contatos):
            if c.getName() == name:
                return i
        return -1
    
    def addContact(self, name:str, fones: list[Fone]):
        pos = self.findPosByName(name)
        if pos != -1:
            contact = self.__contatos[pos]
        else:
            contact = Contact(name)
            self.__contatos.append(contact)

        for f in fones:
            if f.isValid():
                contact.addFone(f.getId(), f.getNumber())
            else:
                print(f"fail: invalid number {f}")
        
        self.__contatos.sort(key = lambda c : c.getName())

    def getContact(self, name:str):
        pos = self.findPosByName(name)
        if pos == -1:
            return None
        return self.__contatos[pos]
    
    def rmContact(self, name:str):
        pos = self.findPosByName(name)
        if pos != -1:
            self.__contatos.pop(pos)

    def rmFone(self, name:str, index:int):
        contato = self.getContact(name)
        if contato:
            contato.rmFone(index)
        else:
            print("fail: contato nao existe")

        

    def search(self, pattern: str):
        res = []
        for c in self.__contatos:
            if pattern in str(c):
                res.append(c)

        return res
    
    def getFavorited(self) -> list[Contact]:
        return "\n".join(str(c) for c in self.__contatos if c.isFav())

    def getContacts(self) -> list[Contact]:
        return self.__contatos

    def __str__(self):
        return "\n".join(str(c) for c in self.__contatos)

def main():
    agenda = Agenda()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "add":
            name = args[1]
            fones = []
            for par in args[2:]:
                id, num = par.split(":")
                fones.append(Fone(id, num))
            agenda.addContact(name, fones)
        elif args[0] == "rm":
            agenda.rmContact(args[1])
        elif args[0] == "search":
            res = agenda.search(args[1])
            for c in res:
                print(c)
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "tfav":
            contato = agenda.getContact(args[1])
            if contato:
                contato.tfav()
        elif args[0]=="rmFone":
            agenda.rmFone(args[1], int(args[2]))
        elif args[0] == "favs":
            print(agenda.getFavorited())
        else:
            print("comando invalido")
main()