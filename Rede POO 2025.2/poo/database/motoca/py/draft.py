class Person:
    def __init__(self, name:str, age:int):
        self.__age = age
        self.__name = name

    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
class Motorcycle:
    def __init__(self, power:int=1):
        self.__power = power
        self.__time = 0
        self.__person = None

    def insert(self, person: Person):
        if self.__person != None:
            print("fail: busy motorcycle")
            return False

        self.__person = person
        return True
    
    def remove(self):
        if self.__person == None:
            print("fail: empty motorcycle")
            return None
        
        person = self.__person
        self.__person = None
        return person
    
    def buy_time(self, time:int):
        self.__time += time

    def drive(self, time:int):
        if self.__time <= 0:
            print("fail: buy time first")
            return
    
        if self.__person == None:
            print("fail: empty motorcycle")
            return
        
        if self.__person.get_age() > 10:
            print("fail: too old to drive")
            return

        if time >= self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
            return

        self.__time -= time

    def honk(self):
        print("P" + ("e"*self.__power) + "m")

    def __str__(self):
        if self.__person==None: return f"power:{self.__power}, time:{self.__time}, person:(empty)"
        return f"power:{self.__power}, time:{self.__time}, person:({self.__person})"

def main():
    moto = Motorcycle()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            moto = Motorcycle(int(args[1]))
        elif args[0] == "leave":
            person = moto.remove()
            if person != None: print(person)
        elif args[0] == "enter":
            person = Person(args[1], int(args[2]))
            moto.insert(person)
        elif args[0] == "buy":
            moto.buy_time(int(args[1]))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "honk":
            moto.honk()
        elif args[0]=="show":
            print(moto)

main()        