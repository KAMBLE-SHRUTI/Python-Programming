class addition:
    def __init__(self):
        self._a=10
        self.b=20

class substrction(addition):
    def __init__(self):
        self.c=78
        self.d=43
        addition.__init__(self)
        print("this is varible from parent class",self._a)
        self._a=45
        print("this is varible from parent class",self._a)
        self.a=12

c=substrction()
print(c._a)