class Time:
    def __init__(self, hour:int=0, minute:int=0, second:int=0):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_second(second)

    def __str__(self)->str:
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"
    
    def get_hour(self)->int:
        return self.__hour
    
    def get_minute(self)->int:
        return self.__minute
    
    def get_second(self)->int:
        return self.__second
    
    def set_hour(self, h:int):
        if h>=0 and h<=23:
            self.__hour = h
            return
        print("fail: hora invalida")

    def set_minute(self, m:int):
        if m>=0 and m<=59:
            self.__minute = m
            return
        print("fail: minuto invalido")

    def set_second(self, s:int):
        if s>=0 and s<=59:
            self.__second = s
            return
        print("fail: segundo invalido")

    def next_second(self):
        self.__second += 1
        if(self.__second >=60):
            self.__minute +=1
            self.__second = 0
            if(self.__minute >=60):
                self.__hour +=1
                self.__minute=0
                if(self.__hour >= 24):
                    self.__hour = 0


    
    
def main():
    time = Time()
    
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            time = Time(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "set":
            time.set_hour(int(args[1]))
            time.set_minute(int(args[2]))
            time.set_second(int(args[3])) 
        elif args[0] == "show":
            print(time)
        elif args[0] == "next":
            time.next_second()
        else:
            print("comando invalido")

main()