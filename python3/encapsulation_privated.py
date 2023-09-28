class  addition:
    def __init__(self):
        self._a=20
        self.__b=39
        print("this is my prvate varible from parent class",self.__b)
        self._b=70
        print("this is my prvate varible from parent class", self._b)

class subsraction(addition):
    def __init__(self):
        self.c=50
        self.d=76
        addition.__init__(self)
        print("this is varible from parent class",self._a)
        self._a=45
        print("this is varible from parent class",self._a)


add=addition()
print(add.__b)
b=subsraction()
print(b._a)